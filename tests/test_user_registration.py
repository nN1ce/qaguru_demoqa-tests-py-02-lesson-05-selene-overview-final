import os.path
from demoqa_tests.model.pages import registration_form
from demoqa_tests.model.pages.registration_form import given_opened
from selene import have
from selene.support.shared import browser
# from tests import controls
from demoqa_tests import model


def test_to_submit_form():

    pass
    #todo_

def test_fail_to_submit_form():

    pass

    # todo_


def test_practice_form():

    registration_form.given_opened()

    # WHEN

    browser.element('#firstName').type('Evgeniy')
    browser.element('#lastName').type('Lukyanov')
    browser.element('#userEmail').type('evgeniy@gmail.qa')

    browser.element('.custom-control-label').click()

    browser.element('#userNumber').type('9111223345')

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').click().element(
        '[value="1990"]'
    ).click()
    browser.element('.react-datepicker__month-select').click().element(
        '[value="4"]'
    ).click()
    browser.element(
        '[class="react-datepicker__day react-datepicker__day--004"]'
    ).click()

    browser.element('#subjectsInput').type('Ar').press_enter().type(
        'Bi'
    ).press_enter().type('Comp').press_enter()

    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('[for="hobbies-checkbox-2"]').click()
    browser.element('[for="hobbies-checkbox-3"]').click()

    browser.element('#uploadPicture').send_keys(
        os.path.abspath(r'.\resources\photo.jpg')
    )

    browser.element('#currentAddress').type('Russia\nSaint-P\nMoskovskaya\n20')

    browser.element('#react-select-3-input').type('NCR').press_enter()
    browser.element('#react-select-4-input').type('Delhi').press_enter()

    browser.element('#submit').with_(click_by_js=True).click()

    # THEN

    dialog_table = browser.element('.modal-content').element('.table')
    rows = dialog_table.all('tbody tr')
    rows.should(
        have.texts(
            'Evgeniy Lukyanov',
            'evgeniy@gmail.qa',
            'Male',
            '9111223345',
            '04 May,1990',
            'Arts, Biology, Computer Science',
            'Sports, Reading, Music',
            'photo.jpg',
            'Russia Saint-P Moskovskaya 20',
            'NCR Delhi',
        )
    )
