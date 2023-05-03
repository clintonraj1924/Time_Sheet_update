import time

import openpyxl
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from utilites import xl_utils
from utilites.base_class import Base_Class
from utilites.custom_logger import LogGen


class Login_002_Test(Base_Class):
    logger = LogGen.loggen()
    path = ".//testData/Clinton_Raj_Timesheet_Entry.xlsx"
    textBox_userName_ID = (By.ID, "txtUserName")
    textBox_password_ID = (By.ID, "txtPassword")
    login_btn_ID = (By.ID, "btnSubmit")
    i_frame_ID = ("MainContent_myframe")
    btnSave_andsubmit_btn_XPath = (By.XPATH, '//input[@class="form-control form-control-sm" and @id="btnSave"]')
    timeSheetApprovelStatus_ID = (By.ID, "app_SP000170_header_lnkAccordion_SP000170")
    i_frame_ID_2 = ("frm_SP000156")
    Project_name_ID = (By.ID, "ddlSP000156_AddProject1")
    Milestone_ID = (By.ID, "ddlSP000156_AddMilestone1")
    Task_group_ID = (By.ID, "ddlSP000156_AddTaskGroup1")
    Task_Name_ID = (By.ID, "ddlSP000156_AddTaskName1")
    Hours_ID = (By.ID, "ddlSP000156_AddHour11")
    Minits_ID = (By.ID, "ddlSP000156_AddMinute11")
    Task_Description_ID = (By.ID, "txtSP000156_AddBriefRemarks1")
    save_btn = (By.XPATH, '//input[@id="btnSave" and @class="button"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    def test_login(self, userName, password):
        self.logger.info("************************ Login_002_Test **************************************")
        self.logger.info("************************ login_test **************************************")

        self.send_keys(self.textBox_userName_ID, userName)
        self.send_keys(self.textBox_password_ID, password)
        self.click(self.login_btn_ID)

    def test_mouse_hover_Timesheet_Entry(self):
        self.mouse_hover()

    def test_main_page(self):
        self.i_frame(self.i_frame_ID)
        self.click(self.btnSave_andsubmit_btn_XPath)

    def test_simple_alert(self):
        self.alert()

    def test_tim_app_status(self):
        # Timesheet Approval Status
        tim_app_status = Base_Class.isClickable(self, self.timeSheetApprovelStatus_ID)
        if tim_app_status.is_displayed():
            # identify element
            self.I = self.driver.find_element(By.ID, "btnReset")
            # action object creation to scroll
            self.a = ActionChains(self.driver)
            self.a.move_to_element(self.I).perform()
        else:
            print("Time sheet approval status is not visible")
            self.logger.error("******** Time sheet approval status is not visible *******")
            Base_Class.screenShort(self, "Time sheet approval status.png")

    def test_excell_operation(self):
        self.i_frame(self.i_frame_ID_2)
        self.rows = xl_utils.get_row_count(self.path, 'Sheet1')

        # 1st row is a headder part so using 2 and it will not take a last row so using +1
        for r in range(2, self.rows + 1):
            time.sleep(3)
            project = xl_utils.read_data(self.path, "Sheet1", r, 4)
            milestone = xl_utils.read_data(self.path, "Sheet1", r, 6)
            task_group = xl_utils.read_data(self.path, "Sheet1", r, 7)
            task_name = xl_utils.read_data(self.path, "Sheet1", r, 8)
            task_description = xl_utils.read_data(self.path, "Sheet1", r, 9)
            hours = xl_utils.read_data(self.path, "Sheet1", r, 12)

            time.sleep(2)
            Base_Class.insert_drop_down(self, self.Project_name_ID, project)
            time.sleep(2)
            Base_Class.insert_drop_down(self, self.Milestone_ID, milestone)
            time.sleep(2)
            Base_Class.insert_drop_down(self, self.Task_group_ID, task_group)
            time.sleep(2)
            Base_Class.insert_drop_down(self, self.Task_Name_ID, task_name)
            time.sleep(2)
            Base_Class.insert_drop_down(self, self.Hours_ID, str(hours))
            time.sleep(2)
            Base_Class.send_keys_xl_related(self, self.Task_Description_ID, task_description)
            time.sleep(2)

    def clk_save_submit_btn(self):
        Base_Class.click(self, self.save_btn)
        time.sleep(2)
        Base_Class.click(self, self.btnSave_andsubmit_btn_XPath)
        Base_Class.alert(self)


def copy_sheet_1to2(self):  # project, milestone, task_group, task_name, task_description, hours
    # Load the workbook
    workbook = openpyxl.load_workbook(self.path)

    # Access a Timesheet
    worksheet = workbook['Sheet1']
    logs_sheet = workbook['Sheet1']
    for row in list(worksheet.iter_rows())[1:]:
        project = xl_utils.read_data(self.path, "Sheet1", row, 4)
        milestone = xl_utils.read_data(self.path, "Sheet1", row, 6)
        task_group = xl_utils.read_data(self.path, "Sheet1", row, 7)
        task_name = xl_utils.read_data(self.path, "Sheet1", row, 8)
        task_description = xl_utils.read_data(self.path, "Sheet1", row, 9)
        hours = xl_utils.read_data(self.path, "Sheet1", row, 12)

        # Append row to Sheet2 starting from the second row
        logs_sheet.append([project, milestone, task_group, task_name, task_description, hours])

        try:
            # Delete row from Sheet1
            worksheet.delete_rows(row[0].row)
        except Exception as e:
            print("Failed to delete row from Sheet1: ", str(e))
    # Save the workbook
    workbook.save(self.path)
