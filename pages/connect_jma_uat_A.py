#线性脚本
from telnetlib import EC

from appium import webdriver
from time import sleep

from appium.webdriver.common.appiumby import AppiumBy

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.get_verfication_code import get_verification_code


desired_caps = {
    "platformName": "Android",  # 测试的平台 (Android)
    "platformVersion": "14",  # Android 版本，确保和设备上的版本匹配
    "deviceName": "1A051FDEE009FW",  # 从 'adb devices' 获取的设备ID  # "app": "/Users/yourname/Downloads/app-debug.apk",APK 文件的路径
    "automationName": "UiAutomator2",  # 使用的自动化引擎
    "appPackage": "jp.co.mcdonalds.android.uat",  # JMA-UAT-Android5.3.170(1055) 的包名
    "appActivity": "mcdonalds.basic.McdonaldsJapanHomeActivity",  # 启动的 Activity
}

# 连接到 Appium 服务器（确保 Appium 在该地址下运行）
driver = webdriver.Remote("http://127.0.0.1:4723", desired_caps)

# 可选：等待几秒钟，让应用加载完成（根据需要调整时间）
#sleep(15)

#onboarding页面点击下一页
#使用显式等待（WebDriverWait），直到元素可用为止，而不是固定的 sleep
el1 = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.ID, "jp.co.mcdonalds.android.uat:id/btn_get_started"))
)
el1.click()
# el1 = driver.find_element(by=AppiumBy.ID, value="jp.co.mcdonalds.android.uat:id/btn_get_started")
# el1.click()
el1.click()
el1.click()
el1.click()

#sleep(3)

#点击登录按钮
el2 = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.ID, "jp.co.mcdonalds.android.uat:id/reLoginButton"))
)
#el2 = driver.find_element(by=AppiumBy.ID, value="jp.co.mcdonalds.android.uat:id/reLoginButton")
el2.click()

sleep(3)

#输入邮箱
#显示等待
el3 = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"Enter email\")"))
)
#el3 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"Enter email\")")
el3.send_keys("yelena+uat3@theplant.jp")

#输入密码
el4 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"Enter password\")")
el4.send_keys("Yqq123321")

#点击登录
el5 = driver.find_element(by=AppiumBy.ID, value="jp.co.mcdonalds.android.uat:id/reLoginButton")
el5.click()

sleep(5)


# 获取验证码
verification_code = get_verification_code()
print(verification_code)
sleep(2)
#输入验证码

el6 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"6 digits number\")")
el6.send_keys(verification_code)

#提交验证码
el7 = driver.find_element(by=AppiumBy.ID, value="jp.co.mcdonalds.android.uat:id/auth")
el7.click()

sleep(6)
#Home页面开屏动画,点击关闭
el9 = driver.find_element(by=AppiumBy.ID, value="jp.co.mcdonalds.android.uat:id/closeButton")
el9.click()

#点击Home页面的MOP点单banner
el10 = driver.find_element(by=AppiumBy.ID, value="jp.co.mcdonalds.android.uat:id/homeTopStoreLayout")
el10.click()

sleep(2)

#点击暂时不打开定位
el11 = driver.find_element(by=AppiumBy.ID, value="jp.co.mcdonalds.android.uat:id/btCancel")
el11.click()
#点击我喜欢的店铺
el12 = driver.find_element(by=AppiumBy.ID, value="jp.co.mcdonalds.android.uat:id/tvFavoriteTab")
el12.click()
#12603下面的还没调试好
el13 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"MOP Lab (12603) \")")
el13.click()
el14 = driver.find_element(by=AppiumBy.ID, value="jp.co.mcdonalds.android.uat:id/btConfirm")
el14.click()
el15 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().resourceId(\"jp.co.mcdonalds.android.uat:id/product_item_relative_layout\").instance(2)")
el15.click()
el16 = driver.find_element(by=AppiumBy.ID, value="jp.co.mcdonalds.android.uat:id/btGoToCartScreen")
el16.click()

# 等待10秒
sleep(10)

# 退出会话（关闭应用）
#driver.quit()