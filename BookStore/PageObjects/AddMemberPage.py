from selenium.webdriver.common.by import By
from Utils.EdgeSupport import EdgeSupport


class AddMemberPage (object):
    def __init__(self, driver):
        self.driver = driver

        # Locators
        self.AddLogin_txt_loc = (By.ID, 'Members_member_login')
        self.AddPassword_txt_loc = (By.ID, 'Members_member_password')
        self.AddLevel_txt_loc = (By.ID, 'Members_member_level')
        self.AddFirstName_txt_loc = (By.ID, 'Members_name')
        self.AddLastName_txt_loc = (By.ID, 'Members_last_name')
        self.AddEmail_txt_loc = (By.ID, 'Members_email')
        self.Insert_btn_loc = (By.ID, 'Members_insert')

        # Elements
        self.AddLogin_txt = driver.find_element(*self.AddLogin_txt_loc)
        self.AddPassword_txt = driver.find_element(*self.AddPassword_txt_loc)
        self.AddLevel_txt = driver.find_element(*self.AddLevel_txt_loc)
        # self.select = Select(self.AddLevel_txt)
        self.AddFirstName_txt = driver.find_element(*self.AddFirstName_txt_loc)
        self.AddLastName_txt = driver.find_element(*self.AddLastName_txt_loc)
        self.AddEmail_txt = driver.find_element(*self.AddEmail_txt_loc)
        self.Insert_btn = driver.find_element(*self.Insert_btn_loc)

    def insert_member(self, login, password, level, fname, lname, email):
        self.AddLogin_txt.send_keys(login)
        self.AddPassword_txt.send_keys(password)
        self.AddLevel_txt.send_keys(level)
        self.AddFirstName_txt.send_keys(fname)
        self.AddLastName_txt.send_keys(lname)
        self.AddEmail_txt.send_keys(email)

    def click_on_insert_btn(self):
        EdgeSupport.click_element_by_id(self.driver, self.Insert_btn[1])