from pageObjects.Credkart_Login_Page import Login_Class
from utilities import XL_Utilities
from utilities.Logger import Logging_Class


class Test_Credkart_Login_DDT:

    log = Logging_Class.log_generator()
    path = ".\\TestData\\Credkart_login_data_DDT.xlsx"

    def test_Credkart_Login_DDT_001(self,setup):
        self.log.info("test_Credkart_Login_DDT_001 started")
        self.log.info("Opening Browser")
        self.driver = setup
        self.lg = Login_Class(self.driver)
        self.log.info("CLick Login Link")
        self.lg.Login_Link()
        row = XL_Utilities.row_count(self.path,'Sheet1')
        print("Nuber of rows in Login Data Excel -->" + str(row))
        Result_List = []

        for r in range(2,row+1):
            print("Loop Number --->" + str(r-1))            # Poonam Recheck
            Email = XL_Utilities.read_data(self.path,"Sheet1",r,1)
            Password = XL_Utilities.read_data(self.path,"Sheet1",r,2)
            Exp_result = XL_Utilities.read_data(self.path,"Sheet1",r,3)
            self.log.info("Enter Email")
            self.lg.Enter_Email(Email)
            self.log.info("Enter Password")
            self.lg.Enter_Password(Password)
            self.log.info("Click Login Button")
            self.lg.Click_Login_Button()

            if Exp_result == "Login_Pass" and self.lg.Verify_Login_Status() == "Pass":
                XL_Utilities.write_data(self.path,"Sheet1",r,4,"Login_Pass")
                Result_List.append("Pass")
                self.log.info("Taking screenshot")
                self.driver.save_screenshot(".\\Screenshots\\test_Credkart_Login_DDT_Pass.PNG")
                self.lg.Click_Menu_Button()
                self.lg.Click_Logout_Button()
                self.lg.Login_Link()

            elif Exp_result == "Login_Pass" and self.lg.Verify_Login_Status() == "Fail":
                XL_Utilities.write_data(self.path,"Sheet1",r,4,"Login_Fail")
                self.log.info("Taking Screenshot")
                self.driver.save_screenshot(".\\Screenshots\\test_Credkart_Login_DDT_Fail.PNG")
                Result_List.append("Fail")
                self.lg.Login_Link()

            elif Exp_result == "Login_Fail" and self.lg.Verify_Login_Status() == "Pass":
                XL_Utilities.write_data(self.path,"Sheet1",r,4,"Login_Fail")
                Result_List.append("Fail")
                self.log.info("Taking Screenshot")
                self.driver.save_screenshot(".\\Screenshots\\test_Credkart_Login_DDT_Fail.PNG")
                self.lg.Click_Menu_Button()
                self.lg.Click_Logout_Button()
                self.lg.Login_Link()
            elif Exp_result == "Login_Fail" and self.lg.Verify_Login_Status() == "Fail":
                XL_Utilities.write_data(self.path,"Sheet1",r,4,"Login_Fail")
                Result_List.append("Pass")
                self.log.info("Taking Screenshot")
                self.driver.save_screenshot(".\\Screenshots\\test_Credkart_Login_DDT_Fail.PNG")
                self.lg.Login_Link()
        print(Result_List)
        if "Fail" in Result_List:
            self.log.info("test Case_Credkart_Login_DDT_001_Fail")
            assert False

        else:
            assert True
            self.log.info("test Case_Credkart_Login_DDT_001_Pass")
        self.log.info("test_Credkart_Login_DDT_001 is Completed\n")





















