from selenium.webdriver.common.by import By


class MainPageLocators:
    QUESTION_LOCATOR = By.XPATH, './/*[@id="accordion__heading-{}"]'
    LAST_QUESTION_SCROLL = By.XPATH, './/*[@id="accordion__heading-7"]'
    ANSWER_LOCATOR = By.XPATH, './/*[@id="accordion__panel-{}"]'
    COOKIE_BUTTON = By.XPATH, './/*[contains(@class, "App_CookieButton") and contains(text(), "да все привыкли")]'
    BUTTON_ORDER_HEADER = By.XPATH, ('.//div[contains(@class, "Header_Nav")]/button[contains(@class, "Button_Button") '
                                     'and contains(text(), "Заказать")]')
    BUTTON_ORDER_ON_PAGE = By.XPATH, ('.//div[contains(@class, "Home_FinishButton")]/button[contains(@class, '
                                      '"Button_Button") and contains(text(), "Заказать")]')
    TITLE_ON_MAIN_PAGE = By.XPATH, './/div[contains(@class, "Home_Header")]'
