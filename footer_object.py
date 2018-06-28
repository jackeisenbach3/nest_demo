"""
This class models the footer object
We model it as two parts:
1. The menu
2. The copyright
"""

from datetime import datetime
from base_page import Base_Page
import locators


class Footer_Object:
    "Page object for the footer class"

    #locators
    footer_menu = locators.footer_menu
    copyright_text = locators.copyright_text
    copyright_start_year = "2017"
    

#    @Wrapit._exceptionHandler
    def goto_footer_link(self, link_name, expected_url_string=None):
        "Go to the link in the footer"
        #Format for a link: string separated by a '>'
        #E.g.: 'About > Our name'
        result_flag = True
        split_link = link_name.split('>')
        for link in split_link:
            result_flag &= self.click_element(self.footer_menu%link.strip())

        #Additional check to see if we went to the right page
        if expected_url_string is not None:
            result_flag &= True if expected_url_string in self.get_current_url() else False

        return result_flag


    def get_copyright(self):
        "Get the current copyright"
        copyright = str(self.get_text(self.copyright_text))
        copyright = copyright.strip()
        #NOTE: We strip out the special '&copy;'
        copyright = '' + copyright.split('')[-1] 
    
        return copyright


    def get_current_year(self):
        "Return the current year in YYYY format"
        now = datetime.now()
        current_year = now.strftime('%Y')

        return current_year


    def check_copyright(self):
        "Check if the copyright is correct"
        result_flag = False
        actual_copyright = self.get_copyright()
        self.write('Copyright text: %s'%actual_copyright, 'debug')
        #Note: We need to maintain this at 2015 because we promised to not change this page 
        expected_copyright = "2017 " + self.copyright_start_year  
    
        if actual_copyright == expected_copyright:
            result_flag = True

        return result_flag


    
