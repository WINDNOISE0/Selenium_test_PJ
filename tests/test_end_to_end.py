import pytest

from config import LOGIN, PASSWORD
from page.catalog_page import MethodsCatalog
from page.main_page import MethodsMainPage
from page.order_page import MethodOrderPage


@pytest.mark.add
def test_create_order_without_captcha(driver_init):
    main_page = MethodsMainPage(driver_init)
    main_page.sign_in(LOGIN, PASSWORD)
    main_page.go_to_for_home_section()

    item_locator = "Samsung VC15K4130HB/EV"

    catalog_page = MethodsCatalog(driver_init)
    catalog_page.add_to_bug_container_vacuum_by_samsung_filter(item_locator, "Samsung")

    order_page = MethodOrderPage(driver_init)
    order_page.create_order()


