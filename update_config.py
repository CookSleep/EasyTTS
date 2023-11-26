import json

def update_config(api_key, api_base):
    # 检查并移除URL中的协议部分（如果存在）
    if api_base.startswith("http://"):
        api_base = api_base[7:]
    elif api_base.startswith("https://"):
        api_base = api_base[8:]

    with open("config.json", "w") as file:
        json.dump({"api_key": api_key, "api_base": api_base}, file, indent=4)
    print("配置已更新。")

api_key = input("请输入你的API-KEY: ")
api_base = input("请输入API-BASE (如 'example.com'): ")
update_config(api_key, api_base)
