"""
====================================================================

   Copyright (c) 2017 Mobile Media Solutions, Inc.
      ALL RIGHTS RESERVED.

   C O N F I D E N T I A L    I N F O R M A T I O N

      This file contains confidential, proprietary and unpublished
      source code solely owned by Mobile Media Solutions, Inc.

   Runs Nest's unittests.

   To run a single test case:
       python -m unittest run_nest_tests.NestTest.test_007_header_thermostat

   Jack Eisenbach 09-06-2017

====================================================================
"""

import os
import sys
import unittest
import locators

from main_page import Main_Page


class NestTest(unittest.TestCase):
    
    def __init__(self, *args, **kwargs):
        super(NestTest, self).__init__(*args, **kwargs)
    
    def setUp(self):
        print "\n=============================== TEST START ====================================="
        self.mp = Main_Page()

    def tearDown(self):
        print "================================ TEST END ======================================"
        self.mp.quit()


    #@unittest.skip("Skipping test_001")
    def test_001_login_email_not_found(self):
        self.mp.signin('elmerfudd@gmail.com', 'Passme123!')
        msg = self.mp.get_text(self.mp.sign_in_error)
        print msg
        self.assertEqual(msg, locators.sign_in_error_msg)
    
    #@unittest.skip("Skipping test_002")
    def test_002_login_email_incorrect_format(self):
        self.mp.signin('elmerfudd', 'Passme123!')
        msg = self.mp.get_text(self.mp.sign_in_bad_email)
        print msg
        self.assertEqual(msg, locators.sign_in_bad_email_msg)
    
    @unittest.skip("Skipping test_003")
    def test_003_login_create_account(self):
        self.mp.signup('jackeisenbach@gmail.com', 'Passme123!')
        msg = self.mp.get_text(self.mp.sign_in_tos)
        print msg
        self.assertEqual(msg, locators.sign_in_tos_msg)
    
    #@unittest.skip("Skipping test_004")
    def test_004_login_recreate_existing_account(self):
        self.mp.signup('jackeisenbach@gmail.com', 'Passme123!')
        msg = self.mp.get_text(self.mp.sign_up_existing)
        print msg
        self.assertEqual(msg, locators.sign_up_existing_msg)

    #@unittest.skip("Skipping test_005")
    def test_005_login_wrong_password(self):
        self.mp.signin('jackeisenbach@gmail.com', 'Passme124!')
        msg = self.mp.get_text(self.mp.sign_in_error)
        print msg
        self.assertEqual(msg, locators.sign_in_error_msg)

    @unittest.skip("Skipping test_006")
    def test_006_login_forgot_password(self):
        self.mp.signin('jackeisenbach@gmail.com', 'Passme124!')
        msg = self.mp.get_text(self.mp.sign_in_error)
        print msg
        self.assertEqual(msg, locators.sign_in_error_msg)

    #@unittest.skip("Skipping test_007")
    def test_007_header_thermostat(self):
        self.mp.open_thermostat()
        msg = self.mp.get_text(self.mp.thermostat_css)
        print msg
        self.assertEqual(msg, locators.thermostat_msg)

    #@unittest.skip("Skipping test_008")
    def test_008_header_cameras(self):
        self.mp.open_cameras()
        msg = self.mp.get_text(self.mp.cameras_css)
        print msg
        self.assertEqual(msg, locators.cameras_msg)

    #@unittest.skip("Skipping test_009")
    def test_009_header_doorbell(self):
        self.mp.open_doorbell()
        msg = self.mp.get_text(self.mp.doorbell_css)
        print msg
        self.assertEqual(msg, locators.doorbell_msg)

    #@unittest.skip("Skipping test_010")
    def test_010_header_alarm_system(self):
        self.mp.open_alarm_system()
        msg = self.mp.get_text(self.mp.alarm_system_css)
        print msg
        self.assertEqual(msg, locators.alarm_system_msg)

    #@unittest.skip("Skipping test_011")
    def test_011_header_smoke_co(self):
        self.mp.open_smoke_co()
        msg = self.mp.get_text(self.mp.smoke_co_css)
        print msg
        self.assertEqual(msg, locators.smoke_co_msg)

    #@unittest.skip("Skipping test_012")
    def test_012_header_works_with(self):
        self.mp.open_works_with()
        msg = self.mp.get_text(self.mp.works_with_css)
        print msg
        self.assertEqual(msg, locators.works_with_msg)

    #@unittest.skip("Skipping test_013")
    def test_013_header_support(self):
        self.mp.open_support()
        msg = self.mp.get_text(self.mp.support_css)
        print msg
        self.assertEqual(msg, locators.support_msg)

    @unittest.skip("Skipping test_014")
    def test_014_header_shopping_cart(self):
        self.mp.open_shopping_cart()
        msg = self.mp.get_text(self.mp.shopping_cart_css)
        print msg
        self.assertEqual(msg, locators.shopping_cart_msg)

    #@unittest.skip("Skipping test_015")
    def test_015_header_check_logo_presence(self):
        self.assertEqual(True, self.mp.check_logo_present())



def test_run_login_tests():
    suite = unittest.TestLoader().loadTestsFromTestCase(NestTest)
    test_result = unittest.TextTestRunner(verbosity = 2).run(suite)
    exit(0)

if __name__=='__main__':
    test_run_login_tests()

