import unittest
from pages.start_page import StartPage
from selenium import webdriver
import json


class TestBuyTickets(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        with open('../config/test_data.json') as config_json:
            self.config = json.load(config_json)

    def test_01_select_destination_and_dates(self):
        #!!! empty field before entering new

        #enter destination
        page = StartPage(self.driver)
        self.driver.get(page.page_address)
        self.driver.implicitly_wait(30)
        page_address_field = self.driver.find_element_by_class_name(page.destination_to)
        page_address_field.clear()
        page_address_field.send_keys(self.config['StartPage']['flight_from'])

        #enter passagers
        #enter dates
        #confirm
        #click
        #check that flight details page opened


        self.assertEqual(True, False)

    def test_02_select_flight(self):
        #find flight
        # confirm
        # check that flight details page opened

        self.assertEqual(True, False)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
