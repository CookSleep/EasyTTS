# EasyTTS

## 简介
EasyTTS是一个便捷的工具，旨在方便地使用第三方API服务来调用OpenAI的文本转语音（TTS）功能。EasyTTS允许用户输入文本，并选择不同的模型、音色、格式来生成音频文件。该项目的代码几乎完全由GPT-4编写，我仅提供需求和建议。
您在使用这个工具前应当获取一个可调用OpenAI TTS的API-KEY。

## 已知的支持调用OpenAI TTS的API服务商（欢迎补充）
1.[ChatAnywhere](https://github.com/chatanywhere/GPT_API_free) （仅付费Key支持调用OpenAI TTS，请选择“支持付费Key”以获取API-KEY）
2.[Bltcy](https://one-api.bltcy.top/)

## 快速开始
在开始使用前，请确保您的计算机上已安装Python。如果您尚未安装Python，可以前往 [Python官网](https://www.python.org/downloads) 进行下载安装。

### 安装步骤
1. 克隆或下载此项目到您的本地计算机。如果您是通过GitHub访问，可以点击界面上绿色的“Code”按钮，然后点击“Download ZIP”，下载完成后解压。
2. 双击运行 `安装所需的Python库.bat` 文件，以安装所需的Python库（例如 `inquirer`）。
3. 双击运行 `日常启动.bat`，并在启动器菜单中选择“更新API设置程序”以输入您的API密钥和API基地址。

### 使用方法
1. 双击运行 `日常启动.bat` 文件。
2. 在启动器菜单中，选择“主程序”以启动文本转语音程序。
3. 按照屏幕上的提示输入文本、选择音频质量、声音选项和音频格式。
4. 输入一个文件名（无需扩展名），程序将生成相应的音频文件并保存在本项目同一目录下的名为“文件”的文件夹中。

### 注意事项
- 确保您的API密钥和API基地址是正确无误且可用的，如果在运行主程序获取音频文件时请求未成功，请联系您选择的API服务商获取支持。

## 音色
想了解各个音色，请访问 [Text to Speech - OpenAI API](https://platform.openai.com/docs/guides/text-to-speech)。注意，同一音色在不同语言下可能有所差异，请以实际效果为准。您也可以在各大视频网站上寻找有关ChatGPT语音对话功能的视频，OpenAI的ChatGPT APP内的语音对话功能使用的就是OpenAI TTS。

## 正在尝试添加的功能
WebUI
音色展示（双语）
API消费、余额查询

## 贡献
欢迎对项目进行贡献！如果您有任何建议或想要添加新功能，请随时创建一个Issue或Pull Request。
