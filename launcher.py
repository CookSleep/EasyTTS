import inquirer
import subprocess
import os

def run_script(script_name):
    # 在当前工作目录下运行脚本
    script_path = os.path.join(os.getcwd(), script_name)
    subprocess.run(['python', script_path])

def main():
    questions = [
        inquirer.List('script',
                      message="请选择要运行的程序",
                      choices=['主程序', '更新 API Key 程序'],
                      ),
    ]

    answers = inquirer.prompt(questions)

    if answers['script'] == '主程序':
        run_script('text_to_speech.py')
    elif answers['script'] == '更新 API Key 程序':
        run_script('update_config.py')

if __name__ == "__main__":
    main()
