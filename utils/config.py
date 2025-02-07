#测试设备Android-Google pixel 6 pro

class Config:
    PLATFORM_NAME = "Android"# 测试的平台 (Android)
    PLATFORM_VERSION = "14"# Android 版本，确保和设备上的版本匹配
    DEVICE_NAME = "1A051FDEE009FW"# 从 'adb devices' 获取的设备ID  # "app": "/Users/yourname/Downloads/app-debug.apk",APK 文件的路径
    #APP_PATH = "/path/to/your/app.apk"
    AUTOMATION_NAME = "UiAutomator2"
    APP_PACKAGE = "jp.co.mcdonalds.android.uat"  # JMA-UAT-Android5.3.170(1055) 的包名
    APP_ACTIVITY = "mcdonalds.basic.McdonaldsJapanHomeActivity"  # 启动的 Activity
    APPIUM_SERVER_URL = "http://127.0.0.1:4723"


