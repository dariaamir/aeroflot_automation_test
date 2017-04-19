from selenium import webdriver

class StartPage(object):
    #selectors
    destination_to = 'cityWidgetInput'
    #methods
    page_address = 'https://www.aeroflot.ru/'

    def __init__(self, driver):
        self.driver = driver