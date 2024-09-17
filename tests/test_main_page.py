import pytest
from conftest import driver
from pages.main_page import MainPage
from data import AnswersText


class TestMainPage:

    @pytest.mark.parametrize(
        'num, result',
        [
            (0, AnswersText.ANSWERSTEXT_PRICE),
            (1, AnswersText.ANSWERSTEXT_ONE_SCOOTER),
            (2, AnswersText.ANSWERSTEXT_ORDER),
            (3, AnswersText.ANSWERSTEXT_TOMOROW),
            (4, AnswersText.ANSWERSTEXT_CALL),
            (5, AnswersText.ANSWERSTEXT_FULL_CHARG),
            (6, AnswersText.ANSWERSTEXT_NALOG),
            (7, AnswersText.ANSWERSTEXT_ALL_REGION)
        ]
    )
    def test_question_and_answers(self, driver, num, result):
        main_page = MainPage(driver)
        main_page.scroll_to_last_question()
        main_page.click_on_cookie_button()
        assert main_page.get_answer_text(num) == result
