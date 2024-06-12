import pytest

from pageObjects.Credkart_Login_Page import Login_Class
from utilities.Logger import Logging_Class


class Test_Credkart_Login_Params:
    log = Logging_Class.log_generator()

    def test_credkart_Login_Param003(self, setup, getDataForLogin):
        self.log.info("Test Credkart Login Param is Started")
        self.log.info("Opening Browser")
        self.driver = setup
        self.lg = Login_Class(self.driver)
        self.log.info("Click Login Link")
        self.lg.Login_Link()
        self.log.info("Enter Email  " + getDataForLogin[0])
        self.lg.Enter_Email(getDataForLogin[0])
        self.log.info("Enter Password  " + getDataForLogin[1])
        self.lg.Enter_Password(getDataForLogin[1])
        self.log.info("Click Login Button")
        self.lg.Click_Login_Button()
        self.log.info("Verify Login Status by Title")

        # if getDataForLogin[2] == "Login_Pass" and self.lg.Verify_Login_Status() == "Pass":
        #     self.log.info("Taking screenshot")
        #     self.driver.save_screenshot(".\\Screenshots\\test_Credkart_Login_Param_Pass01.PNG")
        #     assert True
        #
        # elif ((getDataForLogin[2] == "Login_Pass" and self.lg.Verify_Login_Status() == "Fail")
        #       or (getDataForLogin[2] == "Login_Fail" and self.lg.Verify_Login_Status() == "Pass")):
        #     self.log.info("Taking Screenshot")
        #     self.driver.save_screenshot(".\\Screenshots\\test_Credkart_Login_Param_Fail01.PNG")
        #     assert False
        #
        # else:
        #     self.log.info("Taking Screenshot")
        #     self.driver.save_screenshot(".\\Screenshots\\test_Credkart_Login_Param_Fail02.PNG")
        #     assert True
        #
        # self.log.info("Test case Credkart Login execution Is completed")

        if getDataForLogin[2] == "Login_Pass" and self.lg.Verify_Login_Status() == "Pass":
            self.log.info("Taking screenshot_01_PP")
            self.driver.save_screenshot(".\\Screenshots\\test_Credkart_Login_Param_Pass_01_PP.PNG")
            assert True

        elif getDataForLogin[2] == "Login_Pass" and self.lg.Verify_Login_Status() == "Fail":
            self.log.info("Taking Screenshot_02_PF")
            self.driver.save_screenshot(".\\Screenshots\\test_Credkart_Login_Param_Fail_02_PF.PNG")
            assert False

        elif getDataForLogin[2] == "Login_Fail" and self.lg.Verify_Login_Status() == "Pass":
            self.log.info("Taking Screenshot_03_FP")
            self.driver.save_screenshot(".\\Screenshots\\test_Credkart_Login_Param_Fail_03_FP.PNG")
            assert False

        elif getDataForLogin[2] == "Login_Fail" and self.lg.Verify_Login_Status() == "Fail":
            self.log.info("Taking Screenshot_04_FF")
            self.driver.save_screenshot(".\\Screenshots\\test_Credkart_Login_Param_Fail_04_FF.PNG")
            assert True

        self.log.info("Test case Credkart Login Params execution Is completed")

# pytest -v -n=4 --html=HtmlReports/my_param.html --alluredir="AllureReports" -k test_credkart_Login_Param003