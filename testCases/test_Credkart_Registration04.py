import pytest
from pageObjects.Credkart_Registration_Page import Registration_Class
from pageObjects.Credkart_Login_Page import Login_Class
from Faker import Faker
from utilities.Logger import Logging_Class

class Test_Registration():
    log = Logging_Class.log_generator()
    def test_credkart_registration04(self,setup):
        self.driver = setup
        self.reg = Registration_Class(self.driver)
        self.reg.Click_Registration_Link()
        self.log.info("Username" + (Faker().user_name()) )
        self.reg.Enter_Name(Faker().user_name())
        self.log.info("Email" + (Faker().user_name() + "@" + Faker().domain_name()))
        self.reg.Enter_Email(Faker().user_name() + "@" + Faker().domain_name())
        self.reg.Enter_Password("123456")
        self.reg.Enter_ConfirmPassword("123456")
        self.reg.Click_Registration_Button()
        self.driver.implicitly_wait(5)

        self.lg = Login_Class(self.driver)
        if self.lg.Verify_Login_Status() == "Pass":
            self.driver.save_screenshot(".\\Screenshots\\test_credkart_registration04_Pass.PNG")
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\test_credkart_registration04_Fail.PNG")
            assert False





