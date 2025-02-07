import pytest
from utils.driver_manager import DriverManager
from pages.login_page import LoginPage
from appium.webdriver.common.appiumby import AppiumBy

@pytest.fixture(scope="function")
def driver():
    driver = DriverManager.get_driver()
    yield driver
    driver.quit()

def test_login_success(driver):
    login_page = LoginPage(driver)
    login_page.onboarding()
    login_page.enter_username("yelena+uat3@theplant.jp")
    login_page.enter_password("Yqq123321")
    login_page.click_login_button()
    assert driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                                       value="new UiSelector().text(\"6 digits number\")").is_displayed()