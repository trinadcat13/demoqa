from pages.base_page import BasePage
from components.components import WebElement


class Tables(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/webtables/'
        super().__init__(driver, self.base_url)

        self.btn_delete_row = WebElement(driver, '#delete-record-1')
        self.no_data = WebElement(driver, 'div.rt-noData')
        self.add_btn = WebElement(driver, '#addNewRecordButton')
        self.modal = WebElement(driver, 'div.modal-content')
        self.submit = WebElement(driver, '#submit')

        self.m_firstname = WebElement(driver, '#firstName')
        self.m_lastname = WebElement(driver, '#lastName')
        self.m_mail = WebElement(driver, '#userEmail')
        self.m_age = WebElement(driver, '#age')
        self.m_salary = WebElement(driver, '#salary')
        self.m_department = WebElement(driver, '#department')

        self.firstname = WebElement(driver, 'div:nth-child(4) > div > div:nth-child(1)')
        self.lastname = WebElement(driver, 'div:nth-child(4) > div > div:nth-child(2)')
        self.age = WebElement(driver, 'div:nth-child(4) > div > div:nth-child(3)')
        self.mail = WebElement(driver, 'div:nth-child(4) > div > div:nth-child(4)')
        self.salary = WebElement(driver, 'div:nth-child(4) > div > div:nth-child(5)')
        self.department = WebElement(driver, 'div:nth-child(4) > div > div:nth-child(6)')

        self.edit = WebElement(driver, '#edit-record-4')
        self.delete = WebElement(driver, '#delete-record-4')

        self.test_row = WebElement(driver, '#edit-record-4')

