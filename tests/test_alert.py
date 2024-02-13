import time
from pages.alerts import Alerts


def test_alert(browser):
    page_alerts = Alerts(browser)
    page_alerts.visit()

    assert not page_alerts.alert()

    page_alerts.alertButton.click()
    time.sleep(2)
    assert page_alerts.alert()


def test_alert_text(browser):
    page_alerts = Alerts(browser)
    page_alerts.visit()

    page_alerts.alertButton.click()
    time.sleep(2)

    assert page_alerts.alert().text == 'You clicked a button'
    page_alerts.alert().accept()
    time.sleep(2)
    assert not page_alerts.alert()


def test_confirm(browser):
    page_alerts = Alerts(browser)
    page_alerts.visit()

    page_alerts.confirmButton.click()
    time.sleep(2)

    page_alerts.alert().dismiss()
    time.sleep(2)

    assert page_alerts.confirmResult.get_text() == 'You selected Cancel'


def test_promt(browser):
    page_alerts = Alerts(browser)
    page_alerts.visit()
    name = 'Name'
    page_alerts.promtButton.click()
    time.sleep(2)

    page_alerts.alert().send_keys(name)
    page_alerts.alert().accept()

    assert page_alerts.promtResult.get_text() == f'You entered {name}'

