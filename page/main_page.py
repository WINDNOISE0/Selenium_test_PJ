from base.base_class import Base
from config import USER_NAME, BASE_URL
from helpers.assertetion import AssertValidate
from helpers.locators import LocatorsMainPage, LocatorsHeader


class ActionsMainPage(Base):

    def click_sign_in_button(self):
        self.click_element(LocatorsMainPage.SING_IN_BUTTON)

    def login_input(self, login):
        self.input_text(LocatorsMainPage.LOGIN_INPUT, login)

    def password_input(self, password):
        self.input_text(LocatorsMainPage.PASSWORD_INPUT, password)

    def click_authorize_button(self):
        self.click_element(LocatorsMainPage.AUTHORIZE_BUTTON)

    def click_profile_button(self):
        self.click_element(LocatorsMainPage.USER_PREVIEW_BUTTON)

    def go_to_for_home_section(self):
        self.click_element(LocatorsMainPage.FOR_HOME_SECTION)


class MethodsMainPage(ActionsMainPage):
    def sign_in(self, login, password):
        self.open_url(BASE_URL)
        self.click_sign_in_button()
        self.login_input(login)
        self.password_input(password)
        self.delete_cookies()
        self.click_authorize_button()
        self.click_profile_button()

        validator = AssertValidate(self.driver)
        validator.user_name_validate(USER_NAME)
