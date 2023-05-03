import time
from utilites.readProperteFile import Read_Congig
from pageObject.login_page import Test_Login


class Test_001_Login:

    # baseURL = "http://timesheet.inspirisys.com/"
    # userName = "101635"
    # password = "!QAZ2wsx"
    baseURL = Read_Congig.getApplicationURL()
    userName = Read_Congig.getUserName()
    password = Read_Congig.getPassword()

    def test_login_page(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        time.sleep(5)
        act_title = self.driver.title
        time.sleep(5)
        print(act_title)
        if act_title == "Login Area":
            assert True
        else:
            self.driver.save_screenshot(".\\screenShots\\" + "test_loginpage.png")
            self.driver.close()
            assert False
        self.lp = Test_Login(self.driver)
        time.sleep(5)
        self.lp.setUserName(self.userName)
        time.sleep(5)
        self.lp.setPassword(self.password)
        time.sleep(5)
        self.lp.click_login_btn()




