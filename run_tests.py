#定义测试运行入口
import pytest

if __name__ == "__main__":
    pytest.main(["-v", "--html=reports/report.html"])