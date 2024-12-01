import time

from base.base_class import Base
from config import PERSON_DATA, EMAIL, MOBILE_PHONE_NUMBER
from helpers.assertetion import AssertValidate
from helpers.locators import LocatorsOrders


class ActionOrderPage(Base):

    def input_personal_data(self):
        self.input_text(LocatorsOrders.PERSON_DATA_INPUT, PERSON_DATA)

    def input_email(self):
        self.input_text(LocatorsOrders.EMAIL_INPUT, EMAIL)

    def input_mobile_phone(self):
        element = self.get_viewed_element(LocatorsOrders.MOBILE_PHONE_INPUT)
        self.driver.execute_script("arguments[0].value = arguments[1];", element, MOBILE_PHONE_NUMBER)

    def click_continue(self):
        self.click_element(LocatorsOrders.CONTINUE_BUTTON)

    def select_second_data_delivery(self):
        self.click_element(LocatorsOrders.SECOND_DATA_DELIVERY_CHECKBOX)

    def click_agree_persona_date_checkbox(self):
        self.click_element(LocatorsOrders.AGREE_CHECKBOX)

    def get_order_header(self):
        order_header = self.get_viewed_element(LocatorsOrders.ORDER_PLACEMENT_HEADER)
        return order_header.text

    def get_contact_information(self):
        contact = self.get_viewed_element(LocatorsOrders.CONTACT_PERSON_FOR_CHECK)
        return contact.text

    def get_email_information(self):
        email = self.get_viewed_element(LocatorsOrders.EMAIL_FOR_CHECK)
        return email.text

    def get_mobile_phone_information(self):
        mobile_phone = self.get_viewed_element(LocatorsOrders.MOBILE_PHONE_FOR_CHECK)
        return mobile_phone.text

    def get_error_text(self):
        error_text = self.get_viewed_element(LocatorsOrders.ERROR_WITH_MISSING_CAPTCHA).text
        return error_text


class MethodOrderPage(ActionOrderPage):
    def create_order(self):
        self.input_personal_data()
        self.input_email()

        self.input_mobile_phone()
        self.click_continue()

        validate = AssertValidate(self.driver)

        actual_order_header = self.get_order_header()
        actual_contact = self.get_contact_information()
        actual_email = self.get_email_information()
        actual_mobile_phone = self.get_mobile_phone_information()

        validate.contact_date_validate(actual_order_header, actual_contact, actual_email, actual_mobile_phone)

        self.scroll_page(0, 400)
        self.select_second_data_delivery()
        time.sleep(1)
        self.click_agree_persona_date_checkbox()
        time.sleep(1)
        self.click_continue()

        actual_error_text = self.get_error_text()
        validate.item_validate_str(actual_error_text, LocatorsOrders.EXPECTED_ERROR_TEXT)
        print("Тест добавления товара без ввода капчи успешно пройден")

