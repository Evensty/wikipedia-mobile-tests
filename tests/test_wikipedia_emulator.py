import allure
from allure import step
from allure_commons.types import Severity

from appium.webdriver.common.appiumby import AppiumBy
from selene import have
from selene.support.conditions import be
from selene.support.shared import browser

from wikipedia.model import app

@allure.title('Search title')
@allure.tag('mobile')
@allure.label('owner', 'Maxim Veselov')
@allure.severity(Severity.CRITICAL)
@allure.feature('Search')
@allure.story('Wikipedia')
def test_search_title():
    with step('skip start screen'):
        app.given_opened()

    with step('Input search text'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).send_keys("python")
    with step('Check search results'):
        browser.all((AppiumBy.CLASS_NAME, "android.widget.TextView")).should(have.size_greater_than(0))
    browser.all((AppiumBy.CLASS_NAME, 'android.widget.TextView'))[4].click()

    browser.element((AppiumBy.ACCESSIBILITY_ID, "Save")).click()
    browser.element((AppiumBy.ACCESSIBILITY_ID, 'Navigate up')).click()
    browser.element((AppiumBy.ACCESSIBILITY_ID, 'Navigate up')).click()
    browser.element((AppiumBy.XPATH, '//android.widget.FrameLayout[@content-desc="Saved"]/'
                                 'android.widget.FrameLayout/android.widget.ImageView')).click()
    browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/item_title_container')).click()
    browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/buttonView')).click()
    browser.element((AppiumBy.ACCESSIBILITY_ID, 'Image: Python (programming language)')).should(be.existing)
