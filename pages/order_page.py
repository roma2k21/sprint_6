import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):
    def choice_button_order(self, button):
        if button == 'header_button':
            self.click_element_with_wait(MainPageLocators.BUTTON_ORDER_HEADER)
        else:
            self.scroll_to_element(MainPageLocators.BUTTON_ORDER_ON_PAGE)
            self.click_element_with_wait(MainPageLocators.BUTTON_ORDER_ON_PAGE)

    @allure.step("Ждем когда появится заголовок страницы")
    def wait_see_title(self):
        self.find_element_with_wait(OrderPageLocators.TITLE).is_enabled()

    @allure.step("Вводим имя")
    def input_name(self, name):
        self.add_text_to_element(OrderPageLocators.NAME, name)

    @allure.step("Вводим фамилию")
    def input_surname(self, surname):
        self.add_text_to_element(OrderPageLocators.SURNAME, surname)

    @allure.step("Вводим адрес")
    def input_adress(self, adress):
        self.add_text_to_element(OrderPageLocators.ADRESS, adress)

    @allure.step("Выбираем станцию метро")
    def choise_metro_station(self):
        self.click_element_with_wait(OrderPageLocators.METRO)
        self.click_element_with_wait(OrderPageLocators.METRO_DROPDOWNLIST)

    @allure.step("Вводим телефон")
    def input_phone_number(self, phone):
        self.add_text_to_element(OrderPageLocators.PHONE, phone)

    @allure.step("Переход на следующую страницу заказа")
    def next_page_order(self):
        self.click_element_with_wait(OrderPageLocators.NEXT_PAGE)

    @allure.step("Ждем когда появится заголовок страницы")
    def wait_see_title_about_rent(self):
        self.find_element_with_wait(OrderPageLocators.TITLE_LAST).is_enabled()

    @allure.step("Выбираем дату")
    def data_order(self):
        self.click_element_with_wait(OrderPageLocators.DATA_RENT)
        self.click_element_with_wait(OrderPageLocators.RANDOM_DAY)

    @allure.step("Выбираем срок аренды")
    def long_order(self):
        self.click_element_with_wait(OrderPageLocators.TIME_RENT)
        self.click_element_with_wait(OrderPageLocators.RENT_PERIOD)

    @allure.step("Выбираем цвет самоката")
    def color_scooter(self):
        self.click_element_with_wait(OrderPageLocators.CHECKBOX_COLOUR)

    @allure.step("Комментарий для курьера")
    def comments_for_courier(self):
        self.add_text_to_element(OrderPageLocators.COMMENTS_COURIER, '1234567890')

    @allure.step("Нажимаем заказать")
    def click_order_button(self):
        self.click_element_with_wait(OrderPageLocators.ORDER_BUTTON)

    @allure.step("Нажимаем Да")
    def yes_button(self):
        self.click_element_with_wait(OrderPageLocators.BUTTON_YES)

