import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    @allure.step("Прокрутить страницу до последнего вопроса")
    def scroll_to_last_question(self):
        self.scroll_to_element(MainPageLocators.LAST_QUESTION_SCROLL)

    @allure.step("Нажать на кнопку согласиться на куки")
    def click_on_cookie_button(self):
        self.click_element_with_wait(MainPageLocators.COOKIE_BUTTON)

    @allure.step("Клик на вопрос")
    def click_on_question(self, num):
        locator_q_formatted = self.format_locator(MainPageLocators.QUESTION_LOCATOR, num)
        self.click_element_with_wait(locator_q_formatted)

    @allure.step("Получение текста ответа")
    def get_text_answer(self, num):
        locator_a_formatted = self.format_locator(MainPageLocators.ANSWER_LOCATOR, num)
        return self.get_text_from_element(locator_a_formatted)

    @allure.step("Проверка результата")
    def get_answer_text(self, num):
        self.click_on_question(num)
        return self.get_text_answer(num)
