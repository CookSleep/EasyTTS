import subprocess
import sys

def install_package(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def main():
    try:
        import inquirer
        print("所有必需的库已正确安装。")
    except ImportError:
        print("正在安装必要的Python库 'inquirer'...")
        try:
            install_package("inquirer")
            print("库安装成功。")
        except Exception as e:
            print(f"安装过程中出现错误: {e}")
            print("尝试更换源重新安装...")
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install", "-i", "https://pypi.tuna.tsinghua.edu.cn/simple", "inquirer"])
                print("库安装成功。")
            except Exception as ex:
                print(f"更换源安装失败: {ex}")
                print("请检查您的Python环境和网络设置。")

if __name__ == "__main__":
    main()
