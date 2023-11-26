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
                      choices=['主程序', '更新API设置程序'],
                      ),
    ]

    while True:
        answers = inquirer.prompt(questions)

        if answers['script'] == '主程序':
            run_script('text_to_speech.py')
        elif answers['script'] == '更新API设置程序':
            run_script('update_config.py')

        if not inquirer.prompt([inquirer.Confirm('continue', message="是否再次选择需要运行的程序?", default=True)])['continue']:
            break

if __name__ == "__main__":
    main()
