import time
from pages.text_box import TextBox


def test_two_elements(browser):
    text_box = TextBox(browser)
    text = 'SampleText'
    text_box.visit()
    text_box.name.send_keys(text)
    time.sleep(2)
    text_box.address.send_keys(text)
    text_box.submit.click_force()
    time.sleep(2)
    assert text_box.name_output.get_text() == 'Name:' + text
    assert text_box.address_output.get_text() == 'Current Address :' + text

