# nest_demo  
Demo Python unittest framework running Selenium Webdriver using a Page Object Model design pattern.  
This demo was run using Python 2.7.13 (64-bit) and the Firefox Browser 57.0.1 (64-bit). The computer is  
a Windows 10. Tests were run on the site: https://nest.com The selenium module was installed using "pip install selenium". The included geckodriver.exe (64-bit) works with the Firefox version listed above.  
  
The Nest.com sections tested were for various signin and signup scenarious and also the header links were verified.  
  
Here's what the output should look like once everything is setup and running properly:  
  
c:\workspace\nest>python run_nest_tests.py  
test_001_login_email_not_found (main.NestTest) ...  
=============================== TEST START =====================================  
signin ...  
Incorrect email address or password. Please try again.  
================================ TEST END ======================================  
ok  
test_002_login_email_incorrect_format (main.NestTest) ...  
=============================== TEST START =====================================  
signin ...  
Your Nest Account name needs to be a working email address.  
================================ TEST END ======================================  
ok  
test_003_login_create_account (main.NestTest) ... skipped 'Skipping test_003'  
test_004_login_recreate_existing_account (main.NestTest) ...  
=============================== TEST START =====================================  
signup ...  
This Nest Account already exists.  
================================ TEST END ======================================  
ok  
test_005_login_wrong_password (main.NestTest) ...  
=============================== TEST START =====================================  
signin ...  
Incorrect email address or password. Please try again.  
================================ TEST END ======================================  
ok  
test_006_login_forgot_password (main.NestTest) ... skipped 'Skipping test_006'  
test_007_header_thermostat (main.NestTest) ...  
=============================== TEST START =====================================  
A Nest Thermostat for every home.  
================================ TEST END ======================================  
ok  
test_008_header_cameras (main.NestTest) ...  
=============================== TEST START =====================================  
Meet the Nest Cam family.  
================================ TEST END ======================================  
ok  
test_009_header_smoke_co (main.NestTest) ...  
=============================== TEST START =====================================  
Nest Protect  
================================ TEST END ======================================  
ok  
test_010_header_works_with (main.NestTest) ...  
=============================== TEST START =====================================  
Works with Nest  
================================ TEST END ======================================  
ok  
test_011_header_support (main.NestTest) ...  
=============================== TEST START =====================================  
Nest Support  
================================ TEST END ======================================  
ok  
test_012_header_shopping_cart (main.NestTest) ...  
=============================== TEST START =====================================  
Your cart  
================================ TEST END ======================================  
ok  
test_013_header_check_logo_presence (main.NestTest) ...  
=============================== TEST START =====================================  
================================ TEST END ======================================  
ok  
  
Ran 13 tests in 179.997s  
  
OK (skipped=2)  
  
c:\workspace\nest>  
  
All the locators can be found in the locators.py file. If the nest.com site changes, then  
by modifying only the locators.py file, the tests should run OK.  
Jack Eisenbach  
760-270-6937  
  
