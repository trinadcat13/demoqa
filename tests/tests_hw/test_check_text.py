from pages.demoqa import DemoQa
from pages.elements import Elements
import time

def test_check_text(browser):
    demo_qa_page = DemoQa(browser)
    el_page = Elements(browser)
    demo_qa_page.visit()
    assert demo_qa_page.txt_footer.get_text() == '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.'
    demo_qa_page.btn_elements.click()
    time.sleep(5)
    assert el_page.txt_elements.get_text() == 'Please select an item from left to start practice.'

