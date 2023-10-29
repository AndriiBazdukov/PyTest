from selenium.webdriver import Chrome, Firefox


class DriverFactory:
    __FIREFOX = "Firefox"

    def __init__(self, browser_id: str):
        self.__browser_id = browser_id

    def get_driver(self):
        if self.__browser_id == self.__FIREFOX:
            driver = Firefox()
            return driver
        else:
            driver = Chrome()
            return driver
