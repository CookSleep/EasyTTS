import http.client
import json
import inquirer
import os

# 从配置文件读取API密钥
def load_config():
    if not os.path.exists("config.json"):
        return {"api_key": ""}
    with open("config.json", "r") as file:
        return json.load(file)

config = load_config()

def tts_request(text, model, voice, filename, format):
    # 确保“文件”文件夹存在
    output_dir = os.path.join(os.getcwd(), "文件")
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 文件保存路径
    file_path = os.path.join(output_dir, f"{filename}.{format}")

    conn = http.client.HTTPSConnection("api.chatanywhere.com.cn")
    payload = json.dumps({
        "model": model,
        "input": text,
        "voice": voice,
        "format": format
    })
    headers = {
        'Authorization': f'Bearer {config["api_key"]}',
        'Content-Type': 'application/json'
    }

    conn.request("POST", "/audio/speech", payload, headers)
    res = conn.getresponse()
    data = res.read()

    if res.status == 200:
        with open(file_path, "wb") as file:
            file.write(data)
        print(f"音频已保存在 '{file_path}'")
    else:
        print("请求未成功，未能保存音频")

def main():
    text = input("请输入你要转换的文字: ")

    questions = [
        inquirer.List('model',
                      message="请选择音频质量",
                      choices=['tts-1', 'tts-1-hd'],
                      ),
        inquirer.List('voice',
                      message="请选择声音选项",
                      choices=['alloy', 'echo', 'fable', 'onyx', 'nova', 'shimmer'],
                      ),
        inquirer.List('format',
                      message="请选择音频格式",
                      choices=['mp3', 'opus', 'aac', 'flac'],
                      ),
    ]

    answers = inquirer.prompt(questions)
    model = answers['model']
    voice = answers['voice']
    format = answers['format']

    filename = input("请输入你想保存的文件名（不要包括扩展名）: ")

    tts_request(text, model, voice, filename, format)

if __name__ == "__main__":
    main()
