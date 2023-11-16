# EasyTTS

## 简介
EasyTTS 是一个便捷的工具，旨在方便地使用第三方API服务chatanywhere（前往 https://github.com/chatanywhere/GPT_API_free 以了解更多）来调用OpenAI的文本转语音（TTS）功能。该项目的代码几乎完全由GPT-4编写，我仅提供需求和建议。EasyTTS 允许用户输入文本，并选择不同的模型、音色、格式来生成音频文件。
请注意，本项目与chatanywhere无直接关联，仅为方便调用其API而创建。如果您没有chatanywhere的API-KEY，请前往 [chatanywhere的项目](https://github.com/chatanywhere/GPT_API_free) 选择“支持付费Key”来购买！
目前本工具只支持调用chatanywhere的API，后续可能会提供对更多API的支持！

## 快速开始
在开始使用前，请确保您的计算机上已安装Python。如果您尚未安装Python，可以前往 https://www.python.org/downloads 进行下载安装。

### 安装步骤
1. 克隆或下载（点击界面上绿色的Code按钮→点击Download ZIP）此项目到您的本地计算机，使用前请解压。
2. 双击运行 `第一次启动请点我！.bat` 文件，以安装所需的Python库（例如 `inquirer`）。
3. 双击运行 `日常启动.bat`，并在启动器菜单中选择“更新 API Key 程序”以输入您的API密钥。

### 使用方法
1. 双击运行 `日常启动.bat` 文件。
2. 在启动器菜单中，选择“主程序”以启动文本转语音程序。
3. 按照屏幕上的提示输入文本、选择音频质量、声音选项和音频格式。
4. 输入一个文件名（无需扩展名），程序将生成相应的音频文件在本项目同一目录下的名为“文件”的文件夹中。

### 注意事项
- 确保您的API密钥是正确无误且可用的，如果在运行主程序获取音频文件时请求未成功，请联系chatanywhere获取支持。

## 音色
想了解各个音色，请访问 [Text to speech - OpenAl API](https://platform.openai.com/docs/guides/text-to-speech) 。注意，同一音色在不同语言下可能有所差异，请以实际效果为准。您也可以在各大视频网站上寻找有关ChatGPT语音对话功能的视频，OpenAI的ChatGPT APP内的语音对话功能使用的就是OpenAI TTS。

## 贡献
欢迎对项目进行贡献！如果您有任何建议或想要添加新功能，请随时创建一个Issue或Pull Request。
