from pages.base_page import BasePage
from components.components import WebElement


class SmallModal(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/modal-dialogs'
        super().__init__(driver, self.base_url)

        self.close_modal = WebElement(driver, '#closeSmallModal')
        self.open_modal = WebElement(driver, '#showSmallModal')
        self.modal_window = WebElement(driver, 'body > div.fade.modal.show > div > div')



