from Framework.Py.Selenium.BasePage import BasePage
from Framework.Py.Selenium.TestExceptionHandler import driverhandler


class LoginPage(BasePage):
    def __init__(self, loc_file):
        self.locator_file = loc_file

    @driverhandler
    def Open_Web_Browser(self, browser, url):
        BasePage.__init__(self, browser, url, self.locator_file)

    @driverhandler
    def Go_to_Login_Page(self):
        self.navigate_to_url()

    @driverhandler
    def Login(self, username, password):
        self.get_element('Username').send_keys(username)
        self.get_element('Password').send_keys(password)
        self.click_element('Login Button')

    @driverhandler
    def get_user_label(self):
        return self.get_element('Username Label').text
