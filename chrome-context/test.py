from playwright.sync_api import sync_playwright
import os

def check_browser_version():
    with sync_playwright() as p:
        # 启动 Chromium 并获取版本
        browser = p.chromium.launch()
        version = browser.version
        print(f"Chromium 版本: {version}")
        browser.close()


check_browser_version()


from skyvern.constants import REPO_ROOT_DIR, SKYVERN_DIR

print(REPO_ROOT_DIR)
print(SKYVERN_DIR)


def run_browser_with_extension():
    with sync_playwright() as p:
        # 获取扩展的绝对路径
        extension_path = os.path.abspath("./extensions/yesCaptcha")
        
        # 启动带扩展的浏览器
        context = p.chromium.launch_persistent_context(
            user_data_dir="./user-data",  # 用户数据目录
            headless=False,  # 扩展需要无头模式关闭
            args=[
                f"--disable-extensions-except={extension_path}",
                f"--load-extension={extension_path}",
            ],
            ignore_default_args=["--enable-automation"],
        )
        
        # 创建新页面
        page = context.new_page()
        page.goto("https://www.google.com/recaptcha/api2/demo")
        
        # 等待用户操作
        page.pause()
        


        # 关闭浏览器
        # context.close()

run_browser_with_extension()