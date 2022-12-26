from selene import have
from selene.support.shared import browser


def checkboxes_click(locator, *by_texts):
    for value in by_texts:
        locator.element_by(have.text(value)).click()
