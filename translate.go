package main

import (
	"bytes"
	"encoding/json"
	"github.com/atotto/clipboard"
	"gopkg.in/ini.v1"
	"io"
	"log"
	"net/http"
	"net/url"
	"encoding/base64"
	"strings"
	"unicode/utf8"
)

type TranslationRequest struct {
	Text string `json:"text"`
}

type TranslationResponse struct {
	Translations []struct {
		Text string `json:"text"`
	} `json:"translations"`
}

func translateAzure(text string, client *http.Client, apiKey string, endpoint string, location string) (string, error) {
	url := endpoint + "/translate?api-version=3.0&from=ja&to=en"

	headers := map[string]string{
		"Ocp-Apim-Subscription-Key":     apiKey,
		"Ocp-Apim-Subscription-Region":  location,
		"Content-type":                  "application/json",
	}

	body, _ := json.Marshal([]TranslationRequest{{Text: text}})
	req, err := http.NewRequest("POST", url, bytes.NewBuffer(body))
	if err != nil {
		log.Println("Error creating request")
		return "", err
	}
	for k, v := range headers {
		req.Header.Add(k, v)
	}

	resp, err := client.Do(req)
	if err != nil {
		log.Println("Error making request")
		return "", err
	}
	defer resp.Body.Close()

	var translationResponse []TranslationResponse
	err = json.NewDecoder(resp.Body).Decode(&translationResponse)
	if err != nil {
		log.Println("Error decoding response")
		return "", err
	}

	return translationResponse[0].Translations[0].Text, nil
}

func translateOpenAI(text string, client *http.Client, apiKey string) (string, error) {
	endpoint := "https://api.openai.com/v1/chat/completions"

	headers := map[string]string{
		"Authorization": "Bearer " + apiKey,
		"Content-type":  "application/json",
	}

	body, _ := json.Marshal(map[string]interface{}{
		"model":       "gpt-3.5-turbo-16k-0613",
		"messages": []map[string]string{
			{"role": "system", "content": "Translate this Japanese into closest English. Output Format: Text"},
			{"role": "user", "content": text},
		},
		"temperature": 0.5,
		"max_tokens":  300,
		"n":           1,
		"stop":        nil,
	})

	req, err := http.NewRequest("POST", endpoint, bytes.NewBuffer(body))
	if err != nil {
		log.Println("Error creating request")
		return "", err
	}

	for k, v := range headers {
		req.Header.Add(k, v)
	}

	resp, err := client.Do(req)
	if err != nil {
		log.Println("Error making request")
		return "", err
	}
	defer resp.Body.Close()

	respBody, _ := io.ReadAll(resp.Body)

	type ChatCompletionResponse struct {
		ID        string `json:"id"`
		Object    string `json:"object"`
		Created   int    `json:"created"`
		Model     string `json:"model"`
		Choices   []struct {
			Index         int `json:"index"`
			Message       struct {
				Role    string `json:"role"`
				Content string `json:"content"`
			} `json:"message"`
			FinishReason string `json:"finish_reason"`
		} `json:"choices"`
		Usage struct {
			PromptTokens    int `json:"prompt_tokens"`
			CompletionTokens int `json:"completion_tokens"`
			TotalTokens     int `json:"total_tokens"`
		} `json:"usage"`
	}

	var result ChatCompletionResponse
	err = json.Unmarshal(respBody, &result)
	if err != nil {
		log.Println("Error decoding response")
		return "", err
	}
	translatedText := result.Choices[0].Message.Content

	return translatedText, nil
}

func translateDeepl(text string, client *http.Client, apiKey string) (string, error) {
	endpoint := "https://api-free.deepl.com/v2/translate"

	headers := map[string]string{
		"Authorization": "DeepL-Auth-Key " + apiKey,
		"Content-Type":  "application/x-www-form-urlencoded",
	}

	data := url.Values{}
	data.Set("text", text)
	data.Set("target_lang", "EN") // 目的言語を英語に設定
	data.Set("source_lang", "JA") // 元の言語を日本語に設定

	req, err := http.NewRequest("POST", endpoint, strings.NewReader(data.Encode()))
	if err != nil {
		log.Println("Error creating request")
		return "", err
	}

	for k, v := range headers {
		req.Header.Add(k, v)
	}

	resp, err := client.Do(req)
	if err != nil {
		log.Println("Error making request")
		return "", err
	}
	defer resp.Body.Close()

	respBody, _ := io.ReadAll(resp.Body)

	type DeepLResponse struct {
		Translations []struct {
			DetectedSourceLanguage string `json:"detected_source_language"`
			Text                   string `json:"text"`
		} `json:"translations"`
	}

	var result DeepLResponse
	err = json.Unmarshal(respBody, &result)
	if err != nil {
		log.Println("Error decoding response")
		return "", err
	}
	translatedText := result.Translations[0].Text

	return translatedText, nil
}

func main() {
	client := &http.Client{}

	text, err := clipboard.ReadAll()
	if err != nil {
		log.Fatal("Error reading from clipboard:", err)
	}

	// Check if the clipboard content is empty or not valid UTF-8 text
	if strings.TrimSpace(text) == "" || !utf8.ValidString(text) {
		log.Println("Clipboard is empty or not valid text. Skipping translation.")
		return
	}

	cfg, err := ini.Load("config.ini")
	if err != nil {
		log.Fatal("Error loading config.ini file:", err)
	}

	apiChoice := cfg.Section("API").Key("choice").String()

	var translatedText string
	if apiChoice == "Azure" {
		apiKey := cfg.Section("Azure").Key("api_key").String()
		endpoint := cfg.Section("Azure").Key("endpoint").String()
		location := cfg.Section("Azure").Key("location").String()

		// Decrypt API key, endpoint, and location
		decryptedAPIKey, _ := base64.StdEncoding.DecodeString(apiKey)
		decryptedEndpoint, _ := base64.StdEncoding.DecodeString(endpoint)
		decryptedLocation, _ := base64.StdEncoding.DecodeString(location)

		translatedText, err = translateAzure(text, client, string(decryptedAPIKey), string(decryptedEndpoint), string(decryptedLocation))
	} else if apiChoice == "OpenAI" {
		apiKey := cfg.Section("OpenAI").Key("api_key").String()
		decryptedAPIKey, _ := base64.StdEncoding.DecodeString(apiKey)
		translatedText, err = translateOpenAI(text, client, string(decryptedAPIKey))

	} else if apiChoice == "DeepL" {
		apiKey := cfg.Section("DeepL").Key("api_key").String()
		decryptedAPIKey, _ := base64.StdEncoding.DecodeString(apiKey)
		translatedText, err = translateDeepl(text, client, string(decryptedAPIKey))

	} else {
		log.Fatal("Invalid API choice:", apiChoice)
	}

	if err != nil {
		log.Fatal("Error translating text:", err)
	}

	err = clipboard.WriteAll(translatedText)
	if err != nil {
		log.Fatal("Error writing to clipboard:", err)
	}
}