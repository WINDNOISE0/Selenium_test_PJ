import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import TIMEOUT
from helpers.locators import LocatorsHeader


class Base:
    def __init__(self, driver):
        self.driver = driver

    def open_url(self, page):
        self.driver.get(page)
        self.driver.maximize_window()

    def click_element(self, locator, timeout=TIMEOUT):
        WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable((By.XPATH, locator))
        ).click()

    def delete_cookies(self):
        self.driver.delete_all_cookies()

    def input_text(self, locator, text, timeout=TIMEOUT):
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable((By.XPATH, locator))
        )
        element.clear()
        element.send_keys(text)

    def get_viewed_element(self, locator, timeout=TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((By.XPATH, locator))
        )

    def scroll_page(self, x, y):
        self.driver.execute_script(f"window.scrollTo({x}, {y});")

    def current_link(self):
        return self.driver.current_url

    def wait_count_cart(self, count, timeout=TIMEOUT):
        count_cart = WebDriverWait(self.driver, timeout).until(
            lambda driver: driver.find_element(By.XPATH, LocatorsHeader.BUG_COUNT).text
            == str(count)
        )
        return count_cart
