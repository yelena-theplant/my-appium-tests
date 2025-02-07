#配置 pytest 报告
import pytest
from utils.logger import setup_logger

@pytest.hookimpl(tryfirst=True)
def pytest_configure():
    setup_logger()

@pytest.hookimpl(tryfirst=True)
def pytest_html_report_title(report):
    report.title = "Appium Test Report"