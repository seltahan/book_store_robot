import os
from time import sleep
from selenium import webdriver


class DriverFactory(object):
    @staticmethod
    def get_driver(browser):
        exec_path = os.path.join(os.path.dirname(__file__), "..", "..", "Tools", "Drivers")
        print 'Starting {} browser session.'.format(browser)

        if browser == 'Chrome':
            driver = webdriver.Chrome(executable_path=exec_path + "/chromedriver.exe")
        elif browser == 'IE':
            driver = webdriver.Ie(executable_path=exec_path + "/IEDriverServer.exe")
        elif browser == 'Edge':
            driver = webdriver.Edge(executable_path=exec_path + "/MicrosoftWebDriver.exe")
        else:
            raise Exception('Incorrect browser type supplied to driver factory')

        sleep(5)
        driver.implicitly_wait(30)
        driver.maximize_window()
        return driver
