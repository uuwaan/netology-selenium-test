import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

_AUTH_LOGIN = ""
_AUTH_PASSWORD = ""


class TestYaPassportAuth(unittest.TestCase):
    def setUp(self):
        drv_options = webdriver.ChromeOptions()
        drv_options.add_argument("--incognito")
        drv_options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=drv_options)

    def test_login_password_auth(self):
        self.driver.get("https://passport.yandex.ru/auth")
        self.assertIn("Авторизация", self.driver.title)
        elem = self.driver.find_element_by_css_selector(
            "input#passp-field-login"
        )
        elem.send_keys(_AUTH_LOGIN)
        elem.send_keys(Keys.RETURN)
        WebDriverWait(self.driver, 10).until(
            EC.url_to_be("https://passport.yandex.ru/auth/welcome")
        )
        elem = self.driver.find_element_by_css_selector(
            "input#passp-field-passwd"
        )
        elem.send_keys(_AUTH_PASSWORD)
        elem.send_keys(Keys.RETURN)
        WebDriverWait(self.driver, 10).until(
            EC.url_to_be("https://passport.yandex.ru/profile")
        )

    def test_auth_with_wrong_password(self):
        self.driver.get("https://passport.yandex.ru/auth")
        self.assertIn("Авторизация", self.driver.title)
        elem = self.driver.find_element_by_css_selector(
            "input#passp-field-login"
        )
        elem.send_keys(_AUTH_LOGIN)
        elem.send_keys(Keys.RETURN)
        WebDriverWait(self.driver, 10).until(
            EC.url_to_be("https://passport.yandex.ru/auth/welcome")
        )
        elem = self.driver.find_element_by_css_selector(
            "input#passp-field-passwd"
        )
        elem.send_keys(_AUTH_PASSWORD[::-1])
        elem.send_keys(Keys.RETURN)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "div.passp-form-field__error")
        ))

    def tearDown(self):
        self.driver.close()
