from pages.base_page import BasePage
from components.components import WebElement


class Elements(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/elements/'
        super().__init__(driver, self.base_url)
        self.txt_elements = WebElement(driver, '#app > div > div > div.row > div.col-12.mt-4.col-md-6')
