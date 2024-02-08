from pages.base_page import BasePage
from components.components import WebElement


class Elements(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/elements'
        super().__init__(driver, self.base_url)

        self.text_please = WebElement(driver, '#app > div > div > div.row > div.col-12.mt-4.col-md-6')
        self.text_elements = WebElement(driver, 'div.playgound-header > div')
        self.icon = WebElement(driver, 'header > a > img')
        self.btn_sidebar_first = WebElement(driver, '#app > div > div > div.row > div:nth-child(1) > div > div > div:nth-child(1) > span > div')
        self.btn_sidebar_first_textbox = WebElement(driver, '#item-0')
        self.btn_sidebar_first_checkbox = WebElement(driver, '#item-1')
        self.btns_first_menu = WebElement(driver, 'div:nth-child(1) > div > ul > li')

