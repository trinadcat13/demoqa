import time
import pytest
from pages.large_modal import LargeModal
from pages.small_modal import SmallModal


@pytest.mark.parametrize('pages', [SmallModal, LargeModal])
def test_check_modal(browser, pages):
    page = pages(browser)
    page.visit()
    assert page.open_modal.exist()
    page.open_modal.click()
    time.sleep(2)
    assert page.modal_window.exist()
    assert page.close_modal.exist()
    page.close_modal.click()
    time.sleep(2)
    assert not page.modal_window.exist()





