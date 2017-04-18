import unittest
from pages.start_page import StartPage
from selenium import webdriver


class TestBuyTickets(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        page = StartPage(self.driver)
        self.driver.get(page.page_address)

    def test_01_select_destination_and_dates(self):
        #!!! empty field before entering new

        #enter destination
        page = StartPage(self.driver)
        page.destimation_to.click()

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
