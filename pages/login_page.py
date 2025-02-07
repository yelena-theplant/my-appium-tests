from appium.webdriver.common.mobileby import MobileBy
from appium import webdriver
from time import sleep

from appium.webdriver.common.appiumby import AppiumBy

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.get_verfication_code import get_verification_code

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def onboarding(self):
        el1 = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.ID, "jp.co.mcdonalds.android.uat:id/btn_get_started"))
        )
        el1.click()
        # el1 = driver.find_element(by=AppiumBy.ID, value="jp.co.mcdonalds.android.uat:id/btn_get_started")
        # el1.click()
        el1.click()
        el1.click()
        el1.click()

    def enter_username(self, username):
        # username_field = self.driver.find_element(MobileBy.ID, "com.example.myapp:id/username")
        # username_field.send_keys(username)
        # 点击登录按钮
        el2 = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.ID, "jp.co.mcdonalds.android.uat:id/reLoginButton"))
        )
        # el2 = driver.find_element(by=AppiumBy.ID, value="jp.co.mcdonalds.android.uat:id/reLoginButton")
        el2.click()

        sleep(3)

        # 输入邮箱
        # 显示等待
        el3 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"Enter email\")"))
        )
        # el3 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"Enter email\")")
        el3.send_keys(username)



    def enter_password(self, password):
        # password_field = self.driver.find_element(MobileBy.ID, "com.example.myapp:id/password")
        # password_field.send_keys(password)
        # 输入密码
        el4 = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                                       value="new UiSelector().text(\"Enter password\")")
        el4.send_keys(password)

    def click_login_button(self):
        # login_button = self.driver.find_element(MobileBy.ID, "com.example.myapp:id/login_button")
        # login_button.click()

        # 点击登录
        el5 = self.driver.find_element(by=AppiumBy.ID, value="jp.co.mcdonalds.android.uat:id/reLoginButton")
        el5.click()

        sleep(10)
   #
   #      # 获取验证码
   #      verification_code = get_verification_code()
   #      print(verification_code)
   #      sleep(2)
   #      # 输入验证码
   #
   #      el6 = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
   #                                     value="new UiSelector().text(\"6 digits number\")")
   #      el6.send_keys(verification_code)
   #
   #      # 提交验证码
   #      el7 = self.driver.find_element(by=AppiumBy.ID, value="jp.co.mcdonalds.android.uat:id/auth")
   #      el7.click()
   #
   #      sleep(6)
   #      # Home页面开屏动画,点击关闭
   #      el9 = self.driver.find_element(by=AppiumBy.ID, value="jp.co.mcdonalds.android.uat:id/closeButton")
   #      el9.click()
   #  #
   #