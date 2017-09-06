from selenium.webdriver.common.by import By
from Utils.EdgeSupport import EdgeSupport
from Page import Page


class HomePage(Page):
    def __init__(self, driver):
        Page.__init__(self, driver)

    @staticmethod
    def get_home_url():
        return 'http://10.1.23.10/bookstore'
