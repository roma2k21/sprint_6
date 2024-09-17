from selenium.webdriver.common.by import By
from helpers import InfoAboutPerson


class OrderPageLocators:
    TITLE = By.XPATH, './/div[contains(@class, "Order_Header") and contains(text(), "Для кого самокат")]'
    NAME = By.XPATH, './/input[@placeholder = "* Имя"]'
    SURNAME = By.XPATH, './/input[@placeholder = "* Фамилия"]'
    ADRESS = By.XPATH, './/input[@placeholder = "* Адрес: куда привезти заказ"]'
    METRO = By.XPATH, './/input[@placeholder = "* Станция метро"]'
    METRO_DROPDOWNLIST = By.XPATH, './/div[@class = "select-search__select"]'
    PHONE = By.XPATH, './/input[@placeholder = "* Телефон: на него позвонит курьер"]'
    NEXT_PAGE = By.XPATH, './/button[contains(@class, "Button_Middle")]'
    TITLE_LAST = By.XPATH, './/*[contains(@class, "Order_Header") and contains(text(), "Про аренду")]'
    DATA_RENT = By.XPATH, './/input[@placeholder = "* Когда привезти самокат"]'
    RANDOM_DAY = By.XPATH, './/div[@aria-label="Choose пятница, 20-е сентября 2024 г."]'
    TIME_RENT = By.XPATH, './/div[@class = "Dropdown-placeholder"]'
    RENT_PERIOD = By.XPATH, f'.//div[@class = "Dropdown-option"][{InfoAboutPerson.random_period}]'
    CHECKBOX_COLOUR = By.XPATH, f'//input[@id="{InfoAboutPerson.random_color}"]'
    COMMENTS_COURIER = By.XPATH, './/input[@placeholder = "Комментарий для курьера"]'
    ORDER_BUTTON = By.XPATH, './/*[contains(@class, "Button_Middle") and contains(text(), "Заказать")]'
    BUTTON_YES = By.XPATH, './/*[contains(@class, "Button_Middle") and contains(text(), "Да")]'
    CONF_ORDER = By.XPATH, './/div[text()="Заказ оформлен"]'
