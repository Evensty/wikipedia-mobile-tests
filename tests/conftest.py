import allure
import allure_commons
import pytest
from _pytest.nodes import Item
from _pytest.runner import CallInfo
from selene.support.shared import browser
from selene import support
from appium import webdriver

import config
from wikipedia import utils


@pytest.fixture(scope='function', autouse=True)
def driver_management(request):
    browser.config.timeout = config.settings.timeout
    browser.config._wait_decorator = support._logging.wait_with(
        context=allure_commons._allure.StepContext
    )

    with allure.step('set up app session'):
        browser.config.driver = webdriver.Remote(
            config.settings.remote_url, options=config.settings.driver_options
        )

    yield

    if config.settings.run_on_browserstack and request.node.result_of_call.failed:
        '''
        request.node is an "item" because we use the default "function" scope
        '''
        utils.allure.attach.screenshot(name='Last screenshot')
        utils.allure.attach.screen_xml_dump()

    session_id = browser.driver.session_id

    allure.step('close app session')(browser.quit)()

    if config.settings.run_on_browserstack:
        utils.allure.attach.video_from_browserstack(session_id)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item: Item, call: CallInfo):  # noqa
    outcome = yield
    result_of_ = outcome.get_result()


    setattr(item, 'result_of_' + result_of_.when, result_of_)
