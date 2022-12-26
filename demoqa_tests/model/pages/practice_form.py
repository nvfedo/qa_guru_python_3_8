from selene import have, be
from selene.support.shared import browser
import demoqa_tests.utils.picture_path
from demoqa_tests.model.controls import checkboxes
from demoqa_tests.model.controls import datepicker, radiobutton, dropdown


def open_practice_form_page():
    browser.open('/automation-practice-form')


def set_first_name(first_name):
    browser.element('#firstName').should(be.blank).type(first_name)


def set_last_name(last_name):
    browser.element('#lastName').should(be.blank).type(last_name)


def set_email(email):
    browser.element('#userEmail').should(be.blank).type(email)


def set_gender(gender):
    radiobutton.select_by_value(browser.all('[name=gender]'), gender)


def set_phone_number(phone_number):
    browser.element('#userNumber').should(be.blank).type(phone_number)


def set_birthday(month, year, day):
    datepicker.set_birthday_date(month, year, day)


def set_subject(subject):
    browser.element('#subjectsInput').type(subject).press_enter()


def set_hobby(hobby):
    checkboxes.checkboxes_click(browser.all('[for^=hobbies-checkbox]'), hobby)


def upload_file(value):
    demoqa_tests.utils.picture_path.download_files(value)


def set_current_address(address):
    browser.element('#currentAddress').type(address)


def set_state(state):
    dropdown.dropdown_set_value('#state', '[id^=react-select][id*=option]', state)


def set_city(city):
    dropdown.dropdown_set_value('#city', '[id^=react-select][id*=option]', city)


def submit_form():
    browser.element('#submit').press_enter()


def register_modal_window_validation(data):
    dialog = browser.element('.modal-content')
    rows = dialog.all('tbody tr')
    for row, values in data:
        rows.element_by(have.text(row)).all('td')[1].should(have.exact_text(values))