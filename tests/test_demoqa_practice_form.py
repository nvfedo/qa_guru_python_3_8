from demoqa_tests.model.pages import practice_form


def test_positive_fill_practice_form():
    practice_form.open_practice_form_page()

    # When
    practice_form.set_first_name('Nikita')
    practice_form.set_last_name('Fedotov')
    practice_form.set_email('fedotov_nikita_test@mail.ru')
    practice_form.set_current_address('Moscow')
    practice_form.set_phone_number('7963732987')

    practice_form.set_gender('Male')

    practice_form.set_birthday('4', '1997', '14')

    practice_form.set_subject('History')

    practice_form.set_hobby('Reading')

    practice_form.upload_file('resources/image_for_test.png')

    practice_form.set_state('Haryana')
    practice_form.set_city('Panipat')

    practice_form.submit_form()

    # Then
    practice_form.register_modal_window_validation(
        [
            ('Student Name', 'Nikita Fedotov'),
            ('Student Email', 'fedotov_nikita_test@mail.ru'),
            ('Gender', 'Male'),
            ('Mobile', '7963732987'),
            ('Date of Birth', '14 May,1997'),
            ('Subjects', 'History'),
            ('Hobbies', 'Reading'),
            ('Picture', 'image_for_test.png'),
            ('Address', 'Moscow'),
            ('State', 'Haryana Panipat'),
        ],
    )
