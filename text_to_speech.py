import http.client
import json
import inquirer
import os

# 从配置文件读取API-KEY和API-BASE
def load_config():
    if not os.path.exists("config.json"):
        return {"api_key": "", "api_base": ""}
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

    try:
        conn = http.client.HTTPSConnection(config["api_base"])
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

        conn.request("POST", "/v1/audio/speech", payload, headers)
        res = conn.getresponse()
        data = res.read()

        if res.status == 200:
            with open(file_path, "wb") as file:
                file.write(data)
            print(f"音频已保存在 '{file_path}'")
        else:
            print(f"请求失败，HTTP状态码: {res.status}")
            if res.status in [401, 403]:
                print("错误：无效的API-KEY。请检查您的API-KEY是否正确。")
            elif res.status == 404:
                print("错误：无效的API-BASE。请检查您的API-BASE是否正确。")

    except Exception as e:
        print(f"发生错误：{e}")
        print("请检查您的API-BASE格式是否正确。")

def main():
    text = input("请输入你要转换的文字 (最多 4096 字符，建议粘贴文字以避免可能存在的无法输入中文的问题): ")
    if len(text) > 4096:
        print("错误：文字长度超过 4096 字符限制。")
        return

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
