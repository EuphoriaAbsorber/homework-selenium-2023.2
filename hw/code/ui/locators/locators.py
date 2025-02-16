from selenium.webdriver.common.by import By


class BasePageLocators:
    base = ()

class CartLocators:
    TAB_NAME = (By.XPATH, '/html/head/title')
    EMPTY_CART_MESSAGE = (By.ID, 'content-unAuth-page-redirect')
    EMPTY_CART_MESSAGE_LINK = (By.XPATH, '//div[@id="content-unAuth-page-redirect"]/a')
    BUTTON_CLEAR_CART = (By.ID, 'button-default_cart__delete')
    CHECKBOX_SELECT_ALL = (By.ID, 'item_cart__select-all')
    CHECKBOX_ITEM = (By.XPATH, '//input[@name="itemCart"]')
    ITEM_PRICE = (By.XPATH, '//span[starts-with(@id, "price/")]')
    ITEM_COUNT = (By.XPATH, '//span[starts-with(@id, "count-product/")]')
    TOTAL_PRICE = (By.ID, 'total-price')
    PRODUCT_NAME_LINK = (By.CLASS_NAME, 'cart-item__cart__id')
    PRODUCT_PHOTO_LINK = (By.CLASS_NAME, 'cart-item__cart__img')
    BUTTON_FAVORITE = (By.XPATH, '//input[starts-with(@id, "favourite-opt_cart/")]')
    POPUP_MESSAGE = (By.ID, 'header_error-message')
    MESSAGE_FOR_LOGIN = (By.XPATH, '//div[@id="header_error-message"]/span')
    BUTTON_DELETE_PRODUCT = (By.XPATH, '//span[starts-with(@id, "delete-cart-item/")]')
    BUTTON_MINUS_PRODUCT = (By.XPATH, '//button[starts-with(@id, "button-minus_cart/")]')
    BUTTON_PLUS_PRODUCT = (By.XPATH, '//button[starts-with(@id, "button-plus_cart/")]')
    BUTTON_EDIT_ADDRESS = (By.ID, 'edit-address')
    BUTTON_EDIT_CARD = (By.ID, 'edit-payment-card')
    DELIVERY_DATE = (By.ID, 'delivery-date-value/0')
    DELIVERY_DATE_1 = (By.ID, 'delivery-date-value/1')
    DELIVERY_DATE_TABINDEX = (By.ID, 'address_cart__date')
    DELIVERY_TIME = (By.ID, 'delivery-time-value/1')
    DELIVERY_TIME_2 = (By.ID, 'delivery-time-value/2')
    DELIVERY_TIME_TABINDEX = (By.XPATH, '//div[@tabindex="1"]')
    SELECT_ADDRESS = (By.XPATH, '//div[@id="address-cart"]/span[2]')
    SELECT_CARD = (By.ID, 'cardNumber')
    UNAUTH_PAYMENT_CARD_MESSAGE = (By.XPATH, '//div[@class="payment-method__cart"]/span')
    UNAUTH_PAYMENT_CARD_MESSAGE_LOGIN_BUTTON = (By.XPATH, '//div[@class="payment-method__cart"]/span/a[1]')
    UNAUTH_PAYMENT_CARD_MESSAGE_REGISTRATION_BUTTON = (By.XPATH, '//div[@class="payment-method__cart"]/span/a[2]')
    UNAUTH_USER_DATA_MESSAGE = (By.XPATH, '//div[@class="user-data-cart__bottom"]/span')
    UNAUTH_USER_DATA_MESSAGE_LOGIN_BUTTON = (By.XPATH, '//div[@class="user-data-cart__bottom"]/span/a[1]')
    UNAUTH_USER_DATA_MESSAGE_REGISTRATION_BUTTON = (By.XPATH, '//div[@class="user-data-cart__bottom"]/span/a[2]')
    BUTTON_EDIT_USER_DATA = (By.ID, 'button-default_cart__delete')
    DISCOUNT = (By.ID, 'discount')
    PRICE_WITHOUT_DISCOUNT =(By.ID, 'price-without-discount')
    TOTAL_COUNT_PRODUCT = (By.ID, 'products-number')
    TOTAL_DATE_DELIVERY = (By.ID, 'date-delivery')
    TOTAL_TIME_DELIVERY = (By.ID, 'time-delivery')
    TOTAL_DELIVERY_INFO = (By.XPATH, '//div[@class="summary-cart__delivery-info"]/a')
    TOTAL_CARD = (By.ID, 'final-paymentmethod')
    TOTAL_UNAUTH_MESSAGE = (By.XPATH, '//div[@class="summary-cart"]/div[5]')
    TOTAL_UNAUTH_MESSAGE_LOGIN_BUTTON = (By.XPATH, '//div[@class="summary-cart"]/div[5]/a')
    BUTTON_MAKE_ORDER = (By.ID, 'summary_cart__create-order-button')

class CategoryPhonesLocators:
    BUTTON_ADD_TO_CART = (By.XPATH, '//div[@id="catalog_block-button-add-to-cart"][1]/div')

class AuthorizeLocators:
    LOGIN_BUTTON_FORM = (By.ID, 'submit-result')
    INPUT_EMAIL = (By.ID, 'email')
    INPUT_PASSWORD = (By.ID, 'password')

class HeaderLocators:
    BUTTON_CART = (By.XPATH, '//div[@class="header__card"]/a')
    BUTTON_LOGIN = (By.XPATH, '//div[@class="header__profile"]/a')
    BUTTON_FAVORITE = (By.XPATH, '//div[@class="header__favourites"]/a')

class FavouritesLocators:
    PRODUCT_NAME_LINK = (By.ID, 'catalog_item-title')
    EMPTY_PAGE_MESSAGE = (By.ID, 'content-unAuth-page-redirect')

class HomeLocators:
    GET_CATEGORIES_CONTAINER = (By.ID, 'catalog')
    BUTTON_ADD_TO_CART = (By.CLASS_NAME, 'item-card__block__button-add-to-cart')

class PopupLocators:
    POPUP = (By.ID, 'popUp')
    POPUP_HEADER = (By.XPATH, '//div[@class="cart-popup-form__header"]/span')
    ADD_BUTTON_IN_POPUP = (By.ID, 'popup-item-create')
    BUTTON_CANCEL = (By.ID, 'cart-popup-form__cancel')
    BUTTON_APPLY = (By.ID, 'cart-popup-form__apply')

class AddressPopupLocators:
    ADDRESS = (By.ID, 'address/76')

class CardPopupLocators:
    CARD = (By.ID, 'paymentCard/cardNumber')

class PromocodeLocators:
    BUTTON_APPLY = (By.ID, 'cart-promocode-submit-button')
    MESSAGE = (By.ID, 'cart-promocode-status')
    INPUT = (By.ID, 'cart-promocode-field')
