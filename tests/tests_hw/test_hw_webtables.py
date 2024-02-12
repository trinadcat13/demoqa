import time
from pages.tables import Tables


def test_first(browser):
    page_tables = Tables(browser)

    page_tables.visit()
    #a
    assert page_tables.add_btn.exist()
    #b
    page_tables.add_btn.click_force()
    time.sleep(2)
    assert page_tables.modal.exist()
    #c
    page_tables.submit.click()
    time.sleep(2)
    assert page_tables.modal.exist()
    #d
    firstname = 'Firstname'
    lastname = 'Lastname'
    mail = 'name@example.com'
    age = '22'
    salary = '9999'
    department = 'Department'
    page_tables.m_firstname.send_keys(firstname)
    page_tables.m_lastname.send_keys(lastname)
    page_tables.m_mail.send_keys(mail)
    page_tables.m_age.send_keys(age)
    page_tables.m_salary.send_keys(salary)
    page_tables.m_department.send_keys(department)
    time.sleep(2)
    page_tables.submit.click()
    time.sleep(2)
    #i
    assert not page_tables.modal.exist()
    #ii
    assert page_tables.firstname.get_text() == firstname
    assert page_tables.lastname.get_text() == lastname
    assert page_tables.age.get_text() == age
    assert page_tables.mail.get_text() == mail
    assert page_tables.salary.get_text() == salary
    assert page_tables.department.get_text() == department
    #e
    page_tables.edit.click()
    time.sleep(2)
    assert page_tables.modal.exist()
    #ei
    assert page_tables.m_firstname.get_dom_attribute('value') == firstname
    assert page_tables.m_lastname.get_dom_attribute('value') == lastname
    assert page_tables.m_mail.get_dom_attribute('value') == mail
    assert page_tables.m_age.get_dom_attribute('value') == age
    assert page_tables.m_salary.get_dom_attribute('value') == salary
    assert page_tables.m_department.get_dom_attribute('value') == department
    #f
    page_tables.m_firstname.send_keys(lastname)
    time.sleep(2)
    page_tables.submit.click()
    time.sleep(2)
    assert page_tables.firstname.get_text() == firstname + lastname
    #g
    page_tables.delete.click()
    time.sleep(2)
    assert not page_tables.delete.exist()
