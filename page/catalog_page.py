import time

from base.base_class import Base
from helpers.assertetion import AssertValidate
from helpers.locators import LocatorsCatalogPage, LocatorsFilterSections,LocatorsHeader


class ActionCatalog(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.expected_count = 0

    def navigate_to_section(self, locator):
        self.click_element(locator)

    def click_add_to_bug(self, item_name):
        element_locator = LocatorsCatalogPage.get_item_locator(item_name)
        self.click_element(element_locator)

    def click_to_filter_checkbox(self, checkbox_name):
        self.click_element(LocatorsFilterSections.manufactured_checkbox_item(checkbox_name))

    def click_to_apply_button(self):
        self.click_element(LocatorsFilterSections.APPLY_MANUFACTURED_FILTER_BUTTON)

    def show_all_manufactured(self):
        self.click_element(LocatorsFilterSections.SHOW_ALL_MANUFACTURER_BUTTON)

    def add_to_expected_count(self, count=1):
        self.expected_count += count


class MethodsCatalog(ActionCatalog):
    def add_to_bug_container_vacuum_by_samsung_filter(self, item_locator, checkbox_name):
        self.navigate_to_section(LocatorsCatalogPage.for_home_category["vacuum_section"])
        self.navigate_to_section(LocatorsCatalogPage.vacuum_subcategory["container_vacuum_section"])
        self.show_all_manufactured()
        self.click_to_filter_checkbox(checkbox_name)
        self.click_to_apply_button()
        self.scroll_page(0, 1400)
        self.click_add_to_bug(item_locator)
        print("Товар добавлен")
        self.add_to_expected_count()

        self.wait_count_cart(self.expected_count)
        print("Количество товаров в корзине увеличилось")




