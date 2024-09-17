import time

import pytest
from conftest import driver
from pages.redirect_page import RedirectPage


class TestRedirect:
    def test_redirect_to_main_page(self, driver):
        redirect_page = RedirectPage(driver)
        assert 'Самокат' in redirect_page.redirect_to_main_page()

    def test_redirect_to_dzen_page(self, driver):
        redirect_page = RedirectPage(driver)
        redirect_page.redirect_to_yandex_page()
        handles = driver.window_handles
        driver.switch_to.window(handles[1])
        assert 'Найти' in redirect_page.find_button_on_dzen_page()
