from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time

class Base_Page(unittest.TestCase):
    '''Base_Page class that all page models can inherit from'''
 
    def __init__(self, base_url='https://nest.com/'):
        '''Constructor'''
        # Add a / at the end of the URL if needed
        if base_url[-1] != '/': 
            base_url += '/' 
        self.base_url = base_url
        self.driver = webdriver.Firefox()
        #Initialize the logger object
        #self.log_obj = Base_Logging(level=logging.DEBUG)
        self.open("")
  
    def quit(self):
        self.driver.quit()

    def back(self):
        self.driver.back()

    def open(self, url):
        '''Visit the page base_url + url'''
        url = self.base_url + url
        self.driver.get(url)
 
    def get_xpath(self, xpath):
        '''Return the DOM element of the xpath OR the 'None' 
        object if the element is not found'''
        pass
 
    def get_title(self, title):
        '''Check the page title'''
        pass

    def get_element(self, locator, verbose_flag=True):
        "Return the DOM element of the path or 'None' if the element is not found "
        dom_element = None
        try:
            locator = self.split_locator(locator)
#            print "locator:", locator
            dom_element = self.driver.find_element(*locator)
        except Exception, e:
            if verbose_flag is True:
                self.write(str(e),'debug')
                self.write("Check your locator-'%s,%s' in the locators.py file"%(locator[0],locator[1]))

        return dom_element

    def split_locator(self, locator):
        "Split the locator type and locator"
        result = ()
        try:
            result = tuple(locator.split(',',1))
        except Exception, e:
            self.write("Error while parsing locator")
  
        return result

    def click_element(self, locator, wait_time=3):
        "Click the button supplied"
        link = self.get_element(locator)
        if link is not None:
            try:
                link.click()
                self.wait(wait_time)
            except Exception,e:
                self.write('Exception when clicking link with path: %s'%locator)
                self.write(e)
            else:
                return True

        return False
    
    def check_element_present(self, locator):
        "This method checks if the web element is present in page or not and returns True or False accordingly"
        result_flag = False
        if self.get_element(locator, verbose_flag=False) is not None:
            result_flag = True

        return result_flag

    def set_text(self, locator, value, clear_flag=True):
        "Set the value of the text field"
        text_field = self.get_element(locator)
        try:
            if clear_flag is True:
                text_field.clear()
        except Exception, e:
            self.write('ERROR: Could not clear the text field: %s'%locator,'debug')

        result_flag = False
        try:
            text_field.send_keys(value)
            result_flag = True
        except Exception,e:
            self.write('Unable to write to text field: %s'%locator,'debug')
            self.write(str(e),'debug')

        return result_flag
          
    def get_text(self, locator):
        "Return the text for a given path or the 'None' object if the element is not found"
        text = ''
        try:
            text = self.get_element(locator).text
        except Exception,e:
            self.write(e)
            return None
        else:
            return text.encode('utf-8')
        
    def write(self, msg, level='info'):
        print(msg, level)
        #self.log_obj.write(msg, level)
  
    def wait(self, wait_seconds=5):
        '''Performs wait for time provided'''
        time.sleep(wait_seconds)
