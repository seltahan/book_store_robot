from Framework.Py.Selenium.BasePage import BasePage
from Framework.Py.Selenium.TestExceptionHandler import driverhandler


class ChangeMemAuthorityPage(BasePage):
    def __init__(self, loc_file):
        self.locator_file = loc_file

    @driverhandler
    def Open_Web_Browser(self, browser, url):
        BasePage.__init__(self, browser, url, self.locator_file)

    @driverhandler
    def Go_to_Admin_Page(self):
        self.navigate_to_url()

    @driverhandler
    def Login(self, username, password):
        self.get_element('Username').send_keys(username)
        self.get_element('Password').send_keys(password)
        self.click_element('Login Button')

    @driverhandler
    def get_user_label(self):
        return self.get_element('AdminMenu label').text

    @driverhandler
    def Go_to_Home_Page(self):
        self.navigate_to_url()

    @driverhandler
    def Click_on_memebers_link(self):
        self.click_element('MembersLink')

    @driverhandler
    def Click_on_insert_member_link(self):
        self.click_element('InsertMember')

    @driverhandler
    def Addlogin(self, login):
        self.get_element('LoginName').send_keys(login)

    @driverhandler
    def Addpassword(self, password):
        self.get_element('Pwd').send_keys(password)

    @driverhandler
    def Addlevel(self, level):
        self.get_element('Level').send_keys(level)

    @driverhandler
    def Addfname(self, fname):
        self.get_element('Fname').send_keys(fname)

    @driverhandler
    def Addlname(self, lname):
        self.get_element('Lname').send_keys(lname)

    @driverhandler
    def Addemail(self, email):
        self.get_element('Email').send_keys(email)

    @driverhandler
    def Click_on_insert_button(self):
        self.click_element('Insert Button')

    @driverhandler
    def Click_on_member_info (self):
        self.click_element('NewMember')

    @driverhandler
    def Click_on_login_name(self):
        self.click_element('RecordMember')

    @driverhandler
    def Addpassword(self):
        self.click_element('Pwd')

    @driverhandler
    def Addlevel(self):
        self.click_element('MembersLink')

    @driverhandler
    def Click_on_update_button (self):
        self.click_element('MembersLink')

