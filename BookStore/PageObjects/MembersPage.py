from selenium.webdriver.common.by import By
from Utils.EdgeSupport import EdgeSupport


class MembersPage(object):
    def __init__(self, driver):
        self.driver = driver
        self.Insert_txt_loc = (By.ID, 'Members_insert')
        self.Insert_txt = driver.find_element(*self.Insert_txt_loc)

    def click_on_insert_link(self):
        EdgeSupport.click_element_by_id(self.driver, self.Insert_txt_loc[1])
