from base_page import Base_Page
import locators


class Header_Object():
    "Page Object for the header class"

    #locators
    thermostat_link = locators.thermostat_link
    cameras_link = locators.cameras_link
    doorbell_link = locators.doorbell_link
    alarm_system_link = locators.alarm_system_link
    smoke_co_link = locators.smoke_co_link
    works_with_link = locators.works_with_link
    support_link = locators.support_link
    shopping_cart_link = locators.shopping_cart_link
    nest_logo = locators.nest_logo

    #my_nest_home = locators.my_nest_home

    thermostat_css = locators.thermostat_css
    cameras_css = locators.cameras_css
    doorbell_css = locators.doorbell_css
    alarm_system_css = locators.alarm_system_css
    smoke_co_css = locators.smoke_co_css
    works_with_css = locators.works_with_css
    support_css = locators.support_css
    shopping_cart_css = locators.shopping_cart_css


    def check_logo_present(self):
        "Check if a logo is present"
        return self.check_element_present(self.nest_logo)

    def open_thermostat(self):
        self.click_element(self.thermostat_link)

    def open_cameras(self):
        self.click_element(self.cameras_link)

    def open_doorbell(self):
        self.click_element(self.doorbell_link)

    def open_alarm_system(self):
        self.click_element(self.alarm_system_link)

    def open_smoke_co(self):
        self.click_element(self.smoke_co_link)

    def open_works_with(self):
        self.click_element(self.works_with_link)

    def open_support(self):
        self.click_element(self.support_link)

    def open_shopping_cart(self):
        self.click_element(self.shopping_cart_link)


