import time
from pages.demoqa import DemoQa
from pages.elements import Elements


def test_go_to_page_elements(browser):
    demo_qa_page = DemoQa(browser)
    el_page = Elements(browser)

    demo_qa_page.visit()
    time.sleep(2)
    assert demo_qa_page.equal_url()
    time.sleep(2)
    demo_qa_page.btn_elements.click()
    time.sleep(2)
    assert el_page.equal_url()
