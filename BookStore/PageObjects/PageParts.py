from selenium.webdriver.common.by import By
from Utils.EdgeSupport import EdgeSupport


class Header(object):
    def __init__(self, driver):
        self.driver = driver
        # Locators
        self.sign_in_loc = (By.ID, 'Header_Menu_Field1')
        self.admin_lnk_loc = (By.ID, 'Header_Menu_Admin')
        # Elements
        self.sign_in_lnk = self.driver.find_element(*self.sign_in_loc)
        self.admin_lnk = self.driver.find_element(*self.admin_lnk_loc)

    def click_sign_in_link(self):
        EdgeSupport.click_element_by_id(self.driver, self.sign_in_loc[1])

    def click_admin_link(self):
        EdgeSupport.click_element_by_id(self.driver, self.admin_lnk_loc[1])
