from selene.support.shared import browser


# def set_month(month):
#     browser.element('.react-datepicker__month-select').click()
#     option_select.select_by_text('.react-datepicker__month-select', month)
#
#
# def set_year(year):
#     browser.element('.react-datepicker__year-select').click()
#     option_select.select_by_text('.react-datepicker__year-select', year)
#
#
# def set_day(day):
#     browser.element(f'.react-datepicker__day--0{day}').click()

def set_birthday_date(month, year, day):
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element(f'[value="{month}"]').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element(f'[value="{year}"]').click()
    browser.element(f'.react-datepicker__day--0{day}').click()
