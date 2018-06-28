'''
Common locator file for all locators
Locators are ordered alphabetically

Selectors we can use
ID
NAME
css selector
CLASS_NAME
LINK_TEXT
PARTIAL_LINK_TEXT
XPATH
'''

#Locators for Signin object(signin_object.py)
email_input = "css selector,.email-input > input:nth-child(1)"
password_input = "css selector,#pass"
password_verify_input = "css selector,#passVerify"
signin_link = "css selector,.account-menu-trigger"
signup_link = "css selector,.signup"
signin_from_signup = "css selector,.account-menu-trigger"
sign_in_submit = "css selector,#signin"
sign_in_error = "css selector,div.error-msg:nth-child(2)" 
sign_in_error_msg = "Incorrect email address or password. Please try again."
sign_in_bad_email = "css selector,div.error-msg:nth-child(1)"
sign_in_bad_email_msg = "Your Nest Account name needs to be a working email address."
sign_in_tos = "css selector,#tos > h1:nth-child(1)"
sign_in_tos_msg = "Terms of Service"
sign_up_existing = "css selector,div.error-msg:nth-child(1)"
sign_up_existing_msg = "This Nest Account already exists."
sign_up_submit = "css selector,#signup"
tos_agree_submit = "css selector,#agree"

my_nest_home = "css selector, a.nl-global-header-account-links:nth-child(1) > span:nth-child(2)"

#Locators for header object(header_object.py)

#thermostat_link = "css selector,li.nl-global-header-desktop:nth-child(1) > a:nth-child(1)"
#thermostat_css = "css selector,#hero > div:nth-child(1) > header:nth-child(1) > h1:nth-child(1)"
thermostat_link = "css selector,div.nav-inner > nav > ul > li:nth-child(1) > a"
thermostat_css = "css selector,#hero > div:nth-child(1) > header:nth-child(1) > h1:nth-child(1)"
#thermostat_msg = "A Nest Thermostat for every home."
thermostat_msg = "What makes a Nest thermostat a Nest thermostat?"

cameras_link = "css selector,li.nl-global-header-desktop:nth-child(2) > a:nth-child(1)"
cameras_css = "css selector,#hero > div:nth-child(1) > header:nth-child(1) > h1:nth-child(1)"
cameras_msg = "Meet the Nest Cam family."

doorbell_link = "css selector,li.nl-global-header-desktop:nth-child(3) > a:nth-child(1)"
doorbell_css = "css selector,.title-text"
doorbell_msg = "Nest Hello"

alarm_system_link = "css selector,li.nl-global-header-desktop:nth-child(4) > a:nth-child(1)"
alarm_system_css = "css selector,.title-text"
alarm_system_msg = "Nest Secure"

#smoke_co_link = "css selector,li.nl-global-header-desktop:nth-child(3) > a:nth-child(1)"
#smoke_co_css = "css selector,.title-text"
#smoke_co_link = "css selector,div.nav-inner > nav > ul > li:nth-child(5) > a"
smoke_co_link = "css selector,li.nav-links-list-item:nth-child(6) > a:nth-child(1)"
smoke_co_css = "css selector,.title-text"
smoke_co_msg = "Nest Protect"

#works_with_link = "css selector,li.nl-global-header-desktop:nth-child(4) > a:nth-child(1)"
#works_with_css = "css selector,.title-text"
works_with_link = "css selector,div.nav-inner > nav > ul > li:nth-child(7) > a"
works_with_css = "css selector,.title-text"
works_with_msg = "Works with Nest"

#support_link = "css selector,li.nl-global-header-desktop:nth-child(5) > a:nth-child(1)"
#support_css = "css selector,h1.small-heading"
#support_link = "css selector,div.control-panel > div.utility-links > li > a"
support_link = "css selector,li.nl-global-header-utility-navigation > a:nth-child(1)"
#support_css = "css selector,#main > div.content.wrapper.main-wrapper > section.support-hero > div > h1"
support_css = "css selector,.title-text"
support_msg = "Nest Support"

shopping_cart_link = "css selector,.cart-icon-svg > path:nth-child(2)"
shopping_cart_css = "css selector,_cart-title_b8atml"
shopping_cart_xpath = "xpath,/html/body/div[3]/div[3]/main/div[2]/div[2]/div/div[1]/h1"
shopping_cart_msg = "Your cart"

nest_logo = "css selector,.nest-icon"

#Locators for main object(main_page.py)
rows_xpath = "xpath,//table[@name='Example Table']//tbody/descendant::tr"
cols_xpath = "xpath,//table[@name='Example Table']//tbody/descendant::td"
cols_relative_xpath = "xpath,//table[@name='Example Table']//tbody/descendant::tr[%d]/descendant::td"
cols_header = "xpath,//table[@name='Example Table']//thead/descendant::th"

#Locators for the footer object(footer_object.py)
footer_menu = "xpath,//ul[contains(@class,'nav-justified')]/descendant::a[text()='%s']"
copyright_text = "xpath,//p[contains(@class,'nest_copyright')]"


