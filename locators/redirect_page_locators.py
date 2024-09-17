from selenium.webdriver.common.by import By


class RedirectPageLocators:
    LOGO_SCOOTER = By.XPATH, './/img[@alt = "Scooter"]'
    LOGO_YANDEX = By.XPATH, './/img[@alt = "Yandex"]'
    BUTTON_FIND = By.XPATH, './/button[text()="Найти"]'
