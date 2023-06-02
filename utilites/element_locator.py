from selenium.webdriver.common.by import By


class EL_Locator:
    path = ".//testData/Clinton_Raj_Timesheet_Entry.xlsx"
    textBox_userName_ID = (By.ID, "txtUserName")
    textBox_password_ID = (By.ID, "txtPassword")
    login_btn_ID = (By.ID, "btnSubmit")
    i_frame_ID = ("MainContent_myframe")
    btnSave_andsubmit_btn_XPath = (By.XPATH, '//input[@class="form-control form-control-sm" and @id="btnSave"]')
    btnSave_XPath = (By.XPATH, '//input[@class="form-control form-control-sm" and @id="btnSave"]')
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

