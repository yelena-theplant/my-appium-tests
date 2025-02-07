from appium import webdriver
from utils.config import Config

class DriverManager:
    @staticmethod
    def get_driver():
        desired_caps = {
            "platformName": Config.PLATFORM_NAME,
            "platformVersion": Config.PLATFORM_VERSION,
            "deviceName": Config.DEVICE_NAME,
            #"app": Config.APP_PATH,
            "automationName": Config.AUTOMATION_NAME,
            "appPackage": Config.APP_PACKAGE,
            "appActivity": Config.APP_ACTIVITY
        }
        driver = webdriver.Remote(Config.APPIUM_SERVER_URL, desired_caps)
        return driver