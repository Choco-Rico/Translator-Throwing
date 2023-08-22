This application is designed to quickly input unspellable English words or sentences into a form. DeepL was developed because it was tedious to translate and paste every time.


## Requirements
* AzureTranslatorAPI or OpenAIAPI
  
## Install
* Install the latest version of .exe from the releases.
* There may be errors from Windows or the browser when installing. Please ignore them and proceed as usual, as there should be no problem.
* After installation is complete, the GUI for registering the API key should launch. If it does not, you can set it up by launching setting.exe.
* The hotkey application is added to the startup folder so it does not need to be run manually each time the PC starts up.

## Usage
  #### Setting
  * You can use AzureTranslatorAPI or OpenAIAPI.  
  * Open `setting.exe`, you can save the setting.
  * The API is encrypted and stored in a config.ini.
  * If you use AzureTranslatorAPI, you also need to input the endpoint and location. You can obtain them from the page where the API key is visible.
  #### Translate
  * If you Select the text you want to translate and press the hotkey twice (default is Alt+C), The text will be replaced with the translated text in a few seconds.
  * Because of the API specification, basically, it only supports complete Japanese. Please translate in the correct format to obtain accurate   translation results. Please refer to the following **examples**.
<details>
<summary>examples</summary>

りんご → Apple  
あっぷる → Apple  
*あっぽーぺん → Appopen  
アッポーペン → Apple Pen  

*みかん → Mikan  
*おれんじ → orenji  
オレンジ → Orange  

*ぱいなっぽーぺん → Painappopen  
パイナッポーペン → Pineapple Pen  

*きゃっと → Kyatto  
キャット → Cat  
ねこ → Cat  
猫 → Cat  
🙀 → screaming cat face  

*さいころじかる → Sai Koro Jikaru  
サイコロジカル → Psychological  
心理的 → Psychological  

隣の客はよく柿食う客だ → The customer next to me is a customer who often eats persimmons.
</details>

## Caution
* There may be differences in translation results and time between the two API keys. Please use the one that suits you best.
* There is a usage fee for the API. Please refer to the API website for pricing.
* **There is a risk of receiving high bills if your API key is leaked. Please manage usage restrictions and other settings on each API's website.**
  
# 以下日本語版(DeepLで翻訳)

このアプリはスペルのわからない英単語あるいは英文を素早くフォームに入力するためのものです。DeepLでいちいち翻訳して貼り付けての作業がおっくうになり開発しました。

 
## 必要条件
* AzureTranslatorAPI または OpenAIAPI
  
## インストール
* リリースから最新版の .exe をインストールしてください。
* インストール時にWindowsやブラウザからエラーが出ることがありますが、問題ありませんので無視して通常通り進めてください。
* インストールが完了するとAPIキーを登録するGUIが立ち上がるはずです。もし立ち上がらない場合はsetting.exeを起動すれば設定できます。
* ホットキーアプリケーションがスタートップフォルダに追加されるためPC起動の度に手動で実行する必要はありません。

## 使用方法
  #### 設定
  * AzureTranslatorAPI または OpenAIAPI を使用します。 
  * setting.exe`を開くと、設定を保存できます。
  * APIkeyは暗号化されてconfig.iniに保存されます。
  * AzureTranslatorAPI を使う場合は、エンドポイントと場所も入力する必要があります。これらは API キーが表示されているページから取得できます。
  #### 翻訳
  * 翻訳したいテキストを選択し、ホットキーを2回押すと(デフォルトは Alt+C)、数秒で翻訳されたテキストに置き換わります。
  * APIの仕様上、基本的に完全な日本語にしか対応していません。正確な翻訳結果を得るためには、正しい形式で翻訳してください。以下の**例**をご参照ください。
<details>
<summary>例</summary>

りんご → Apple  
あっぷる → Apple  
*あっぽーぺん → Appopen  
アッポーペン → Apple Pen  

*みかん → Mikan  
*おれんじ → orenji  
オレンジ → Orange  

*ぱいなっぽーぺん → Painappopen  
パイナッポーペン → Pineapple Pen  

*きゃっと → Kyatto  
キャット → Cat  
ねこ → Cat  
猫 → Cat  
🙀 → screaming cat face  

*さいころじかる → Sai Koro Jikaru  
サイコロジカル → Psychological  
心理的 → Psychological  

隣の客はよく柿食う客だ → The customer next to me is a customer who often eats persimmons.
</details>

## 注意
* 二つのAPIキーで翻訳結果や時間に差が出る場合があります。自分に合った方を使ってください。
* APIは有料です。価格についてはAPIのウェブサイトをご参照ください。
* APIキーが流出した場合、高額な請求を受ける恐れがあります。利用制限等の設定は各APIのサイトで管理してください。
