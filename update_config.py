import json

def update_config(api_key):
    with open("config.json", "w") as file:
        json.dump({"api_key": api_key}, file, indent=4)
    print("配置已更新。")

api_key = input("请输入你的API密钥: ")
update_config(api_key)
