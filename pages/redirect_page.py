import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.redirect_page_locators import RedirectPageLocators


class RedirectPage(BasePage):
    @allure.step("Переход на главную страницу самокатов")
    def redirect_to_main_page(self):
        self.click_element_with_wait(MainPageLocators.BUTTON_ORDER_HEADER)
        self.click_element_with_wait(RedirectPageLocators.LOGO_SCOOTER)
        return self.get_text_from_element(MainPageLocators.TITLE_ON_MAIN_PAGE)

    def redirect_to_yandex_page(self):
        self.click_element_with_wait(RedirectPageLocators.LOGO_YANDEX)

    def find_button_on_dzen_page(self):
        return self.get_text_from_element(RedirectPageLocators.BUTTON_FIND)