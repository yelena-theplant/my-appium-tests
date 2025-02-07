from datetime import time
from appium import webdriver

caps = {}
caps['platformName'] = 'Android'
caps['appium:app'] = 'storage:filename=app (6).apk' # The filename of the mobile app
caps['appium:deviceName'] = 'Android GoogleAPI Emulator'
caps['appium:platformVersion'] = '12.0'
caps['appium:automationName'] = 'UiAutomator2'
caps['sauce:options'] = {}
caps['sauce:options']['username'] = 'oauth-yelena-c14ed'
caps['sauce:options']['accessKey'] = '77e7db58-7141-41d2-b0a4-ab8832558991'
caps['sauce:options']['build'] = 'appium-build-L56PO'
caps['sauce:options']['name'] = '<your test name>'
caps['sauce:options']['deviceOrientation'] = 'PORTRAIT'

# start the session
url = 'https://ondemand.us-west-1.saucelabs.com:443/wd/hub'
driver = webdriver.Remote(url, caps)

# replace with commands and assertions
time.sleep(5)
jobStatus = 'passed' # or 'failed'

# end the session
driver.execute_script('sauce:job-result=' + jobStatus)
driver.quit()