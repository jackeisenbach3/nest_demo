from base_page import Base_Page
import locators


class Signin_Object():
    '''Page object for the Signin/Signup pages'''
 
    #locators
    signin_link = locators.signin_link
    signup_link = locators.signup_link
    signin_from_signup = locators.signin_from_signup
    my_nest_home = locators.my_nest_home
    email_input = locators.email_input
    password_input = locators.password_input
    password_verify_input = locators.password_verify_input
    sign_in_submit = locators.sign_in_submit
    sign_up_submit = locators.sign_up_submit
    sign_in_error = locators.sign_in_error
    sign_in_bad_email = locators.sign_in_bad_email
    sign_in_tos = locators.sign_in_tos
    sign_up_existing = locators.sign_up_existing
    
    
    def signin(self, email, password):
        print "signin ..."
        self.click_element(self.signin_link)
        self.click_element(self.my_nest_home)
        self.set_text(self.email_input, email)
        self.set_text(self.password_input, password)
        self.click_element(self.sign_in_submit)

    def signup(self, email, password):
        print "signup ..."
        self.click_element(self.signin_link)
        self.click_element(self.my_nest_home)
        self.click_element(self.signup_link)
        self.set_text(self.email_input, email)
        self.set_text(self.password_input, password)
        self.set_text(self.password_verify_input, password)
        self.wait(1)
        self.click_element(self.sign_up_submit)

    def signin_from_signup(self):
        self.click_element(self.signin_from_signup)
#        self.back()

