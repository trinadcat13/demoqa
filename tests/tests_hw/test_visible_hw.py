import time
from pages.elements import Elements
from pages.accordian import Accordian


def test_visible_accordian(browser):
    accordian = Accordian(browser)
    accordian.visit()
    assert accordian.section1_p.visible()
    accordian.section1.click()
    time.sleep(2)
    assert not accordian.section1_p.visible()


def test_visible_accordion_default(browser):
    accordian = Accordian(browser)
    accordian.visit()
    assert not accordian.section2_p_1.visible()
    assert not accordian.section2_p_2.visible()
    assert not accordian.section3_p.visible()

