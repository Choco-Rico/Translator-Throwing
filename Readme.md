このアプリはスペルのわからない英単語あるいは英文を素早くフォームに入力するためのものです。DeepLでいちいち翻訳して貼り付けての作業がおっくうになり開発しました。

 
## 必要条件
* AzureTranslatorAPI または OpenAIAPI
  
## インストール
* リリースから最新版のソースコードをインストールしてください。
* インストール時にOSやブラウザからエラーが出ることがありますが、問題ありませんので無視して進めてください。
* インストールが完了したらAPIキーを登録するために``setting.exe``を起動して設定します。
* ``translator-throwing``のショートカットを作成しスタートアップフォルダに追加して実行します。

## 使用方法
  #### 設定
  * ``setting.exe``を開くと、設定を保存できます。
  * APIkeyは暗号化されて``config.ini``に保存されます。
  * AzureTranslatorAPI を使う場合は、エンドポイントとlocationも入力する必要があります。これらは API キーが表示されているページから取得できます。
  #### 翻訳
  * 翻訳したいテキストを選択し、ホットキーを2回押すと(デフォルトは ``Alt+C``)、数秒で翻訳されたテキストに置き換わります。


## 注意
* APIは使用料がかかります。価格についてはAPIのウェブサイトをご参照ください。
* APIキーが流出した場合、高額な請求を受ける恐れがあります。利用制限等の設定は各APIのサイトで管理してください。


## English

This app is designed to help you quickly enter unspelled English words or sentences into a form. DeepL was developed because it was tedious to translate and paste every time.

 
## Requirements
* AzureTranslatorAPI or OpenAIAPI
  
## Installation
* Install the latest source code from the release.
* You may get an error from your OS or browser during installation, but this is not a problem, so please ignore it and proceed.
* After installation is complete, run ``setting.exe`` to register the API key.
* Create a shortcut for ``translator-throwing``, add it to your startup folder and run it.

## How to use
  #### Setting
  * Open ``setting.exe`` to save your settings.
  * The API key is encrypted and stored in ``config.ini``.
  * If you are using AzureTranslatorAPI, you must also enter the endpoint and location. These can be obtained from the page where the API key is displayed.
  #### Translation
  * Select the text you want to translate, press the hotkey twice (default is ``Alt+C``), and it will be replaced by the translated text in a few seconds.


## Attention.
* The API requires a usage fee. Please refer to the API website for pricing.
* If your API key is leaked, you may be charged a hefty fee. Please manage usage restrictions and other settings at each API's website.

Translated with www.DeepL.com/Translator (free version)