import time
from pages.tables import Tables


def test_sort(browser):
    page_tables = Tables(browser)
    page_tables.visit()

    # firstname
    page_tables.firstname_column.click()
    time.sleep(2)
    assert page_tables.firstname_column.get_dom_attribute(
        'class') == 'rt-th rt-resizable-header -sort-asc -cursor-pointer'
    page_tables.firstname_column.click()
    time.sleep(2)
    assert page_tables.firstname_column.get_dom_attribute(
        'class') == 'rt-th rt-resizable-header -sort-desc -cursor-pointer'

    # lastname
    page_tables.lastname_column.click()
    time.sleep(2)
    assert page_tables.lastname_column.get_dom_attribute(
        'class') == 'rt-th rt-resizable-header -sort-asc -cursor-pointer'
    page_tables.lastname_column.click()
    time.sleep(2)
    assert page_tables.lastname_column.get_dom_attribute(
        'class') == 'rt-th rt-resizable-header -sort-desc -cursor-pointer'

    # age
    page_tables.age_column.click()
    time.sleep(2)
    assert page_tables.age_column.get_dom_attribute(
        'class') == 'rt-th rt-resizable-header -sort-asc -cursor-pointer'
    page_tables.age_column.click()
    time.sleep(2)
    assert page_tables.age_column.get_dom_attribute(
        'class') == 'rt-th rt-resizable-header -sort-desc -cursor-pointer'

    # email
    page_tables.mail_column.click()
    time.sleep(2)
    assert page_tables.mail_column.get_dom_attribute(
        'class') == 'rt-th rt-resizable-header -sort-asc -cursor-pointer'
    page_tables.mail_column.click()
    time.sleep(2)
    assert page_tables.mail_column.get_dom_attribute(
        'class') == 'rt-th rt-resizable-header -sort-desc -cursor-pointer'

    # salary
    page_tables.salary_column.click()
    time.sleep(2)
    assert page_tables.salary_column.get_dom_attribute(
        'class') == 'rt-th rt-resizable-header -sort-asc -cursor-pointer'
    page_tables.salary_column.click()
    time.sleep(2)
    assert page_tables.salary_column.get_dom_attribute(
        'class') == 'rt-th rt-resizable-header -sort-desc -cursor-pointer'

    # department
    page_tables.department_column.click()
    time.sleep(2)
    assert page_tables.department_column.get_dom_attribute(
        'class') == 'rt-th rt-resizable-header -sort-asc -cursor-pointer'
    page_tables.department_column.click()
    time.sleep(2)
    assert page_tables.department_column.get_dom_attribute(
        'class') == 'rt-th rt-resizable-header -sort-desc -cursor-pointer'
