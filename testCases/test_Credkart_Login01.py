from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from pageObjects.Credkart_Login_Page import Login_Class
from utilities.Logger import Logging_Class
from utilities.readConfigFile import ReadConfigClass


class TestClass01:
    log = Logging_Class.log_generator()
    Email = ReadConfigClass.getEmail()
    Password = ReadConfigClass.getPassword()

    def test_credkart_url(self, setup):
        # user defined logs
        self.log.debug("This is debug")
        self.log.info("This is info")
        self.log.warning("THis is warning")
        self.log.error("This is error")
        self.log.critical("This is critical")

        self.log.info(" Test case credkart_url is started")
        self.log.info("Opening Browser")
        driver = setup
        self.log.info("Check Page Title")
        if driver.title == "CredKart":
            self.log.info("Test Credkart URL test case is Pass")
            print("Test Credkart URL is Pass")
            self.log.info("Taking Pass sceenshot")
            driver.save_screenshot(".\\Screenshots\\test_credkart_url_Pass.PNG")
            assert True
        else:
            self.log.info("Test credkart URL Test case is Fail")
            print("Test Credkart URL is Fail")
            self.log.info("Taking Fail Screenshot")
            driver.save_screenshot(".\\Screenshots\\test_credkart_url_Fail.PNG")
            assert False
        self.log.info("Test case Credkart URL is completed")
        driver.quit()

    def test_credkart_login(self, setup):
        self.log.info("Test Credkart Login is Started")
        self.log.info("Opening Browser")
        driver = setup
        self.lg = Login_Class(driver)
        self.log.info("Click Login Link")
        self.lg.Login_Link()
        self.log.info("Enter Email" + self.Email)
        self.lg.Enter_Email(self.Email)
        self.log.info("Enter Password" + self.Password)
        self.lg.Enter_Password(self.Password)
        self.log.info("Click Login Button")
        self.lg.Click_Login_Button()
        self.log.info("Verify Login Status by Title")
        if self.lg.Verify_Login_Status() == "Pass":
            self.log.info("Test_Credkart_Login is Pass")
            print("Test Credkart Login is Pass")
            self.log.info("Taking Pass screenshot")
            driver.save_screenshot(".\\Screenshots\\test_credkart_login_Pass.PNG")
            assert True

        else:
            self.log.info("Test Credkart Login is Fail")
            print("Test Credkart Login is Fail")
            self.log.info("Taking Fail screenshot")
            driver.save_screenshot(".\\Screenshots\\test_credkart_login_Fail.PNG")
            assert False
        self.log.info("Test case Credkart Login execution Is completed")
        driver.quit()
