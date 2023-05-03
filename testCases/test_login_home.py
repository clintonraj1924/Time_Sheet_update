import time
from pageObject.login_page_2 import Login_002_Test
from utilites.readProperteFile import Read_Congig


class Test_Login_Home:
    baseURL = Read_Congig.getApplicationURL()
    userName = Read_Congig.getUserName()
    password = Read_Congig.getPassword()

    def test_login_page(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        time.sleep(3)
        act_title = self.driver.title
        time.sleep(3)
        print(act_title)
        if act_title == "Login Area":
            assert True
        else:
            self.driver.save_screenshot(".\\screenShots\\" + "test_loginpage.png")
            self.driver.close()
            assert False

        # def test_login(self, userName, password):
        self.ls = Login_002_Test(self.driver)
        self.ls.test_login(self.userName, self.password)
        self.ls.test_mouse_hover_Timesheet_Entry()
        self.ls.test_main_page()
        self.ls.test_simple_alert()
        self.ls.test_tim_app_status()
        self.ls.test_excell_operation()
        # self.ls.clk_save_submit_btn()
        self.ls.copy_sheet_1to2()


