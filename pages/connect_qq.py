from telnetlib import EC

from appium import webdriver
from time import sleep

from appium.webdriver.common.appiumby import AppiumBy

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

desired_caps = {
    "platformName": "Android",  # 测试的平台 (Android)
    "platformVersion": "14",  # Android 版本，确保和设备上的版本匹配
    "deviceName": "1A051FDEE009FW",  # 从 'adb devices' 获取的设备ID  # "app": "/Users/yourname/Downloads/app-debug.apk",APK 文件的路径
    "automationName": "UiAutomator2",  # 使用的自动化引擎
    "appPackage": "com.tencent.mobileqq",  # QQ 的包名
    "appActivity": "com.tencent.mobileqq.activity.SplashActivity",  # 启动的 Activity
}

# 连接到 Appium 服务器（确保 Appium 在该地址下运行）
driver = webdriver.Remote("http://127.0.0.1:4723", desired_caps)

# 可选：等待几秒钟，让应用加载完成（根据需要调整时间）
sleep(3)

# 点击同意
el1 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="同意")
el1.click()

# 等待登录按钮出现点击登录按钮
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "com.tencent.mobileqq:id/btn_login"))
)
el2 = driver.find_element(by=AppiumBy.ID, value="com.tencent.mobileqq:id/btn_login")
el2.click()

# 等待10秒
sleep(10)

# 退出会话（关闭应用）
driver.quit()