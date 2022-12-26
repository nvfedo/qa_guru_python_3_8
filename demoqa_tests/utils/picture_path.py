from selene.support.shared import browser
import os


def download_files(value):
    browser.element('#uploadPicture').send_keys(os.path.abspath(value))
