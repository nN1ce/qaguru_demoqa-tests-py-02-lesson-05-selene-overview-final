import os.path

from selene import have
from selene.support.shared import browser


def test_practice_form():
    browser.open('https://demoqa.com/automation-practice-form')
    browser.element('#firstName').type('Evgeniy')
    browser.element('#lastName').type('Lukyanov')
    browser.element('#userEmail').type('evgeniy@gmail.qa')
    browser.element('.custom-control-label').click()
    browser.element('#userNumber').type('9111223345')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').click().element('[value="1990"]').click()
    browser.element('.react-datepicker__month-select').click().element('[value="4"]').click()
    browser.element('[class="react-datepicker__day react-datepicker__day--004"]').click()
    browser.element('#subjectsInput').type('Ar').press_enter().type('Bi').press_enter().type('Comp').press_enter()
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('[for="hobbies-checkbox-2"]').click()
    browser.element('[for="hobbies-checkbox-3"]').click()
    # browser.element('[id="uploadPicture"]').send_keys(os.path.abspath('resources\photo.jpg'))
    browser.element('#uploadPicture').send_keys(r"D:\Python\Project\QA_Guru\qaguru_demoqa-tests-py-02-lesson-05-selene-overview-final\resources\photo.jpg")
    browser.element('#currentAddress').type('Russia\nSaint-P\nMoskovskaya\n20')
    browser.element('#react-select-3-input').type('NCR').press_enter()
    browser.element('#react-select-4-input').type('Delhi').press_enter()
    browser.element('#submit').press_enter()

    dialog_table = browser.element('.modal-content').element('.table')
    rows = dialog_table.all('tbody tr')
    rows.should(have.texts(
        'Evgeniy Lukyanov',
        'evgeniy@gmail.qa',
        'Male',
        '9111223345',
        '04 May,1990',
        'Arts, Biology, Computer Science',
        'Sports, Reading, Music',
        'photo.jpg',
        'Russia Saint-P Moskovskaya 20',
        'NCR Delhi'
    ))