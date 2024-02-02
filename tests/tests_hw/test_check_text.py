from pages.demoqa import DemoQa
from pages.elements import Elements
import time


def test_check_footer_text(browser):
    demo_qa_page = DemoQa(browser)
    demo_qa_page.visit()
    assert demo_qa_page.txt_footer.get_text() == '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.'


def test_check_please_text(browser):
    demo_qa_page = DemoQa(browser)
    el_page = Elements(browser)
    demo_qa_page.visit()
    demo_qa_page.btn_elements.click()
    assert el_page.text_please.get_text() == 'Please select an item from left to start practice.'


def test_page_elements(browser):
    el_page = Elements(browser)
    el_page.visit()

    assert el_page.text_elements.get_text() == 'Elements'

    assert el_page.icon.exist()

    assert el_page.btn_sidebar_first.exist()

    assert el_page.btn_sidebar_first_textbox.exist()



