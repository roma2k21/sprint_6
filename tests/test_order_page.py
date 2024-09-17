import pytest
from conftest import driver
from pages.order_page import OrderPage
from pages.main_page import MainPage
from helpers import InfoAboutPerson
from locators.order_page_locators import OrderPageLocators


class TestMainPage:

    @pytest.mark.parametrize(
        'button',
        [
            'header_button',
            'page_button'
        ]
    )
    def test_create_order(self, driver, button):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.click_on_cookie_button()
        order_page.choice_button_order(button)
        order_page.wait_see_title()
        order_page.input_name(InfoAboutPerson.first_name)
        order_page.input_surname(InfoAboutPerson.last_name)
        order_page.input_adress(InfoAboutPerson.adress)
        order_page.choise_metro_station()
        order_page.input_phone_number(InfoAboutPerson.random_phone_number)
        order_page.next_page_order()
        order_page.wait_see_title_about_rent()
        order_page.data_order()
        order_page.long_order()
        order_page.color_scooter()
        order_page.comments_for_courier()
        order_page.click_order_button()
        order_page.yes_button()
        assert 'Заказ оформлен' in order_page.get_text_from_element(OrderPageLocators.CONF_ORDER)
