from selenium.webdriver.common.by import By
from Utils.EdgeSupport import EdgeSupport


class BooksPage (object):
    def __init__(self, driver):
        self.driver = driver
        self.AddNew_txt_loc = (By.ID, 'Items_insert')
        self.AddNew_txt = driver.find_element(*self.AddNew_txt_loc)

    def click_on_add_new(self):
        EdgeSupport.click_element_by_id(self.driver, self.AddNew_txt_loc[1])