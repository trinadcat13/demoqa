import time
import pytest
from pages.demoqa import DemoQa
from pages.accordian import Accordian
from pages.alerts import Alerts
from pages.browser_tab import BrowserTab


def test_seo(browser):
    demo = DemoQa(browser)

    demo.visit()
    assert browser.title == 'DEMOQA'


@pytest.mark.parametrize('button', [Accordian, Alerts, DemoQa, BrowserTab])
def test_check_title_all_page(browser, pages):
    page = pages(browser)
    page.visit()
    time.sleep(2)
    assert page.get_title() == 'DEMOQA'

