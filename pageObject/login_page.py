from selenium.webdriver.common.by import By
from utilites.base_class import Base_Class


class Tags:
    textBox_userName_ID = "txtUserName"
    textBox_password_ID = "txtPassword"
    login_btn_ID = "btnSubmit"


class Test_Login(Base_Class):

    def __init__(self, driver):

        self.driver = driver

    def setUserName(self, userName):
        self.driver.find_element(By.ID, Tags.textBox_userName_ID).clear()
        self.driver.find_element(By.ID, Tags.textBox_userName_ID).send_keys(userName)

    def setPassword(self, password):
        self.driver.find_element(By.ID, Tags.textBox_password_ID).send_keys(password)

    def click_login_btn(self):
        self.driver.find_element(By.ID, Tags.login_btn_ID).click()
