import allure
from allure import step
from allure_commons.types import Severity

from appium.webdriver.common.appiumby import AppiumBy
from selene import have
from selene.support.shared import browser

from wikipedia.model import app

@allure.title('add language')
@allure.tag('mobile')
@allure.label('owner', 'Maxim Veselov')
@allure.severity(Severity.CRITICAL)
@allure.feature('Language')
@allure.story('Wikipedia')
def test_add_new_language():
    with step('skip start screen'):
        app.given_opened()
    with step('add a language'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/menu_icon')).click()
        browser.all((AppiumBy.CLASS_NAME, 'android.widget.TextView'))[1].click()
        browser.all((AppiumBy.CLASS_NAME, 'android.widget.TextView'))[0].click()
        browser.all((AppiumBy.CLASS_NAME, 'android.widget.LinearLayout'))[1].click()
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/section_header_text')).should(have.text('Your languages'))
        browser.all((AppiumBy.CLASS_NAME, 'android.widget.LinearLayout'))[3].click()
        browser.all((AppiumBy.CLASS_NAME, 'android.widget.LinearLayout'))[3].click()
        browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/wiki_language_title')).should(have.size_greater_than(1))
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Navigate up')).click()
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Navigate up')).click()

