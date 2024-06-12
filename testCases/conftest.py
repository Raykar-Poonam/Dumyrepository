import pytest
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")


def pytest_addoption(parser):  # customize command line by adding "--browser" command
    parser.addoption("--browser")


@pytest.fixture
def setup(request):
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        print("Test Run -  Browser Chrome")
        driver = webdriver.Chrome()
    elif browser == "firefox":
        print("Test Run - Browser Firefox")
        driver = webdriver.Firefox()
    elif browser == "edge":
        print("Test Run - Browser Edge")
        driver = webdriver.Edge()
    else:
        print("Test Run - Browser Headless")
        driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.get("https://automation.credence.in/shop")
    driver.implicitly_wait(3)
    yield driver
    driver.quit()


## for chrome webbrowser
# @pytest.fixture()
# def setup():                                                    # it's a function since it's not under a class
#
#     driver = webdriver.Chrome()
#     driver.get("https://automation.credence.in")
#     driver.maximize_window()
#     return driver
#     # yield
#     # driver.quit()


# login Testcase with Parameters

@pytest.fixture(params=[("2may2024@gmail.com", "Test@123", "Login_Pass"),
                            ("2may20245@gmail.com", "Test@123", "Login_Fail"),
                            ("2may2024@gmail.com", "Test@1234", "Login_Fail"),
                            ("2may20245@gmail.com", "Test@1234", "Login_Fail")])
def getDataForLogin(request):                                                           # it's a function, we apply fixtures to function  # Poonam Confirm please
    return request.param
