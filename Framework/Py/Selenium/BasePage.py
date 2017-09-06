import os
from DriverFactory import DriverFactory
from LocatorParser import LocatorParser
from WebElementWait import WebElementWait


class BasePage(object):

    def __init__(self, browser, url, locator_file):
        locator_file_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'Resources', 'Locators', locator_file)
        self.driver = DriverFactory.get_driver(browser)
        self.driver.get(url)
        self.page_locators = LocatorParser.get_locators(locator_file_path)

    # Navigate to the specified URLs
    def navigate_to_url(self):
        url_locator = self.page_locators['URL']
        self.driver.get(self.driver.current_url + url_locator[1])

    def get_cuurent_url(self):
        return self.driver.current_url

    # Get element by element name
    def get_element(self, elem_name, wait=True):
        elem_locator = self.page_locators[elem_name]
        if wait:
            WebElementWait.wait_for_element(self.driver, (elem_locator[0], elem_locator[1]))
        element = self.driver.find_element(elem_locator[0], elem_locator[1])
        return element

    # Get Element with Xpath and return Element
    def get_xpath_element(self, elem_name, xpath_locator, wait=True):
        elem_locator = self.page_locators[elem_name]
        if wait:
            WebElementWait.wait_for_element(self.driver, (elem_locator[0], elem_locator[1]))
        xpath_element = self.driver.find_element_by_xpath(".//*[@id='" + elem_locator[1] + "']" + xpath_locator)
        return xpath_element

    # Get Elements with Xpath and return Elements
    def get_xpath_elements(self, elem_name, xpath_locator):
        elem_locator = self.page_locators[elem_name]
        WebElementWait.wait_for_element(self.driver, (elem_locator[0], elem_locator[1]))
        xpath_elements = self.driver.find_elements_by_xpath(".//*[@id='" + elem_locator[1] + "']" + xpath_locator)
        return xpath_elements

    # click on elements
    def click_element(self, elem_name, wait=True):
        if self.driver.name == "MicrosoftEdge":
            loc = self.get_element(elem_name)
            self.driver.execute_script("arguments[0].click()", loc)
        else:
            self.get_element(elem_name, wait).click()

    # Close Web Browsers after tests
    def close_web_browser(self):
        self.driver.close()
