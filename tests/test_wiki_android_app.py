import allure
from selene import have, be
from allure import step
from pages import main_page, onboarding_page


@allure.epic("Wiki app")
@allure.feature("Onboarding")
@allure.tag("Smoke")
@allure.tag("Mobile")
@allure.label("owner", "Gleb T")
class TestWikiAndroid:

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title("Проверка прохождения онбординга")
    def test_onboarding_passed(self):
        with step("Проверяем открыт ли экран приветствия"):
            onboarding_page.page_title.should(have.text("The Free Encyclopedia\n…in over 300 languages"))

        with step("Переходим на вторую страницу экрана приветствия"):
            onboarding_page.continue_button().click()
            onboarding_page.page_title.should(have.text("New ways to explore"))

        with step("Переходим на третью страницу экрана приветствия"):
            onboarding_page.continue_button().click()
            onboarding_page.page_title.should(have.text("Reading lists with sync"))

        with step("Переходим на четвертую страницу экрана приветствия"):
            onboarding_page.continue_button().click()
            onboarding_page.page_title.should(have.text("Data & Privacy"))

        with step("Закрываем экран приветствия"):
            onboarding_page.get_started_button().click()
            main_page.search_field.should(be.visible)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Проверка пропуска онбординга")
    def test_skip_onboarding(self):

        with step('Пропускаем онбординг'):
            onboarding_page.skip_button.click()

        with step("Проверяем стартовую страницу"):
            main_page.main_logo.should(be.visible)
            main_page.search_field.should(be.visible)

    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Проверка перехода по страницам онбординга")
    def test_navigating_through_onboarding_pages(self):

        with step("Проверяем открыт ли экран приветствия"):
            onboarding_page.page_title.should(have.text("The Free Encyclopedia\n…in over 300 languages"))

        with step("Переходим на вторую страницу экрана приветствия"):
            onboarding_page.continue_button().click()
            onboarding_page.page_title.should(have.text("New ways to explore"))

        with step("Переходим на последнюю страницу экрана приветствия"):
            onboarding_page.last_page_button().click()
            onboarding_page.page_title.should(have.text("Data & Privacy"))

        with step("Переходим на первую страницу экрана приветствия"):
            onboarding_page.first_page_button().click()
            onboarding_page.page_title.should(have.text("The Free Encyclopedia\n…in over 300 languages"))
            