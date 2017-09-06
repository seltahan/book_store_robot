from selenium.webdriver.common.by import By
from Utils.EdgeSupport import EdgeSupport


class AddBookPage(object):

    def __init__(self, driver):
        self.driver = driver

        # Locators
        self.Title_txt_loc = (By.ID, 'Book_name')
        self.Author_txt_loc = (By.ID, 'Book_author')
        self.Category_txt_loc = (By.ID, 'Book_category_id')
        self.Price_txt_loc = (By.ID, 'Book_price')
        self.Add_btn_loc = (By.ID, 'Book_insert')

        # Elements
        self.Title_txt = driver.find_element(*self.Title_txt_loc)
        self.Author_txt = driver.find_element(*self.Author_txt_loc)
        self.Category_txt = driver.find_element(*self.Category_txt_loc)
        self.Price_txt = driver.find_element(*self.Price_txt_loc)
        self.Add_btn = driver.find_element(*self.Add_btn_loc)

    def add_book(self, title, author, category, price):
        self.Title_txt.send_keys(title)
        self.Author_txt.send_keys(author)
        self.Category_txt.send_keys(category)
        self.Price_txt.send_keys(price)

    def click_on_add_btn(self):
        EdgeSupport.click_element_by_id(self.driver, self.Add_btn[1])