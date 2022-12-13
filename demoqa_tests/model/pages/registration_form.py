from selene import have, command
from selene.support.shared import browser


def given_opened():
    browser.open('/automation-practice-form')
    ads = browser.all('[id^=google_ads][id$=container__]')
    ads.with_(timeout=10).should(have.size_greater_than_or_equal(3)).perform(
        command.js.remove
    )

    if ads.with_(timeout=2).wait_until(have.size_greater_than_or_equal(2)):
        ads.perform(command.js.remove)
