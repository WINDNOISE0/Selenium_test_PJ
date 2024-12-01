class LocatorsMainPage:
    SING_IN_BUTTON = "//a[@id='loginBtn']"
    LOGIN_INPUT = "//input[@id='loginInput']"
    PASSWORD_INPUT = "//input[@id='passwordInput']"
    REMEMBER_ME_CHECKBOX = "//input[@id='USER_REMEMBER_frm']"
    AUTHORIZE_BUTTON = "//button[contains(text(),'Авторизоваться')]"

    USER_PREVIEW_BUTTON = "//a[@id='userPreviewBtn']"
    USER_NAME = "//*[@id='userPreviewDropdown']/div[1]/div[2]"

    FOR_HOME_SECTION = "//a[contains(text(),'Для дома')]"


class LocatorsSubcategories:
    SAMSUNG_CHECKBOX_ITEM = "//body/div[@class='container']/div[@class='content']/aside[@class='aside aside_filter']/div[@class='filter']/form[@class='js-FilterForm']/div[@class='filter__block']/div[10]/label[1]/span[1]"
    APPLY_MANUFACTURER_FILTER_BUTTON = "//body/div[@class='container']/div[@class='content']/aside[@class='aside aside_filter']/div[@class='filter']/form[@class='js-FilterForm']/div[@class='filter__block']/div[10]/label[1]/span[1]"
    RESULT_ITEM = "//div[@class='catalog-list']"


class LocatorsFilterSections:
    SORT_DROPDOWN = "//button[@class='catalog-sort__btn']"
    AMOUNT_DESK_SORT_BUTTON = "//div[1]//div[2]//div[1]//div[1]//a[3]"
    MIN_AMOUNT_FILTER_INPUT = (
        "//aside[@class='aside aside_filter']//input[@name='price_min']"
    )
    MAX_AMOUNT_FILTER_INPUT = (
        "//aside[@class='aside aside_filter']//input[@name='price_max']"
    )
    APPLY_MANUFACTURED_FILTER_BUTTON = "//aside[@class='aside aside_filter']//form[@class='js-FilterForm']//button[@type='submit'][contains(text(),'Применить')]"
    APPLY_AMOUNT_FILTER_BUTTON = "//aside[@class='aside aside_filter']//form[@class='js-FilterRangePriceForm']//button[@type='submit'][contains(text(),'Применить')]"
    SHOW_ALL_MANUFACTURER_BUTTON = "//aside[@class='aside aside_filter']//a[@class='filter__more filter__more_checkboxes'][contains(text(),'Показать все')]"

    @staticmethod
    def manufactured_checkbox_item(checkbox_name):
        checkbox_item = f"(//div[@class='filter' and .//div[@class='filter__title' and contains(text(), 'Производитель')]]//a[contains(., '{checkbox_name}')]/preceding-sibling::span[contains(@class, 'checkbox__box')])[2]"
        return checkbox_item


class LocatorsCatalogPage:
    for_home_category = {
        "vacuum_section": "//div[@class='catalog-sections']//div[2]//div[1]//div[1]//div[2]//div[5]//a[1]",
    }

    vacuum_subcategory = {
        "container_vacuum_section": "//h2[@class='catalog-sections__title']//a[contains(text(),'Пылесосы с контейнером')]"
    }

    @staticmethod
    def get_item_locator(item_name):
        item_locator = f"//div[@class='catalog-list__row' and .//b[contains(normalize-space(), '{item_name}')]]//button[contains(normalize-space(), 'Купить в 1 клик')]"
        return item_locator


class LocatorsHeader:
    BUG_COUNT = "//span[@id='js-basket-line']"


class LocatorsOrders:
    EXPECTED_ORDER_HEADER = "Оформление заказа"

    PERSON_DATA_INPUT = "//input[@id='input-15']"
    EMAIL_INPUT = "//input[@id='input-16']"
    MOBILE_PHONE_INPUT = "/html/body/div[5]/div/main/form/div/div[2]/div/div[4]/div/input"
    CONTINUE_BUTTON = "//button[contains(text(), 'Продолжить')]"

    CONTACT_PERSON_FOR_CHECK = "(//div[@class='profiles-form__input']//b)[1]"
    EMAIL_FOR_CHECK = "(//div[@class='profiles-form__input']//b)[2]"
    MOBILE_PHONE_FOR_CHECK = "(//div[@class='profiles-form__input']//b)[3]"

    ORDER_PLACEMENT_HEADER = "//header[@class='page-header']//h1"
    SECOND_DATA_DELIVERY_CHECKBOX = "/html/body/div[5]/div/main/form/div[2]/div[2]/div/div[1]/div/div[2]/label[2]/span[1]"

    CAPTCHA = "//img[@style='margin-top: 10px;']"
    CAPTCHA_INPUT_CODE = "//input[@id='captcha_word']"
    AGREE_CHECKBOX = "//label[@for='offertaInput']"

    ERROR_WITH_MISSING_CAPTCHA = "//div[@class='error']"

    EXPECTED_ERROR_TEXT = "Заполните корректно слово с картинки"
