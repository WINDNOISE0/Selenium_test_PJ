from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from config import PERSON_DATA, EMAIL, MOBILE_PHONE_NUMBER
from helpers.locators import LocatorsMainPage, LocatorsOrders


class AssertValidate(Base):
    def __init__(self, driver):
        super().__init__(driver)

    def user_name_validate(self, expected_user_name):
        current_user_name = self.get_viewed_element(LocatorsMainPage.USER_NAME)
        assert (
            current_user_name.text == expected_user_name
        ), f"Ожидалось имя пользователя: {expected_user_name}, но текущее: {current_user_name}"

    def item_validate_str(self, first_param, second_param):
        assert first_param == second_param, f'{first_param} !=  {second_param}'

    def checkbox_active_validate(self, element):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(element))
        assert element.is_selected(), f"Чекбокс не выбран"

    def contact_date_validate(self, order_header, person_date, email, phone):

        """Проверяем хэадер"""
        self.item_validate_str(order_header, LocatorsOrders.EXPECTED_ORDER_HEADER)
        print("хэадер +++")

        """Проверяем верно ли указано кнотактное лицо"""
        self.item_validate_str(person_date, PERSON_DATA)
        print("Контактное лицо корректное +++")

        """Проверяем верно ли указан email"""
        self.item_validate_str(email, EMAIL)
        print("email корректный +++")

        """Проверяем верно ли указан мобильный номер"""
        self.item_validate_str(phone, MOBILE_PHONE_NUMBER)
        print("номер телефона корректный +++")





