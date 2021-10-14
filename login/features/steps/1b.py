from behave import *
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import os
import sys

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
path_dir = os.path.join(ROOT_DIR, "utils")
sys.path.append(path_dir)


@given("a user accesses the login page (1b)")
def given(context):
    context.driver = webdriver.Chrome(os.path.join(ROOT_DIR, 'utils', 'driver', 'chromedriver.exe'))
    context.driver.get("https://homologacao.leadfortaleza.com.br/ead/login")


@when("the user submits his signup without the user")
def when(context):
    username_field = context.driver.find_element_by_id("login")
    username_field.send_keys()

    password_field = context.driver.find_element_by_id("password")
    password_field.send_keys("abcd1234")

    login_button = context.driver.find_element_by_id("login-btn")
    login_button.click()


@then("the system displays Invalid user and/or password. Check the user and password and try again")
def then(context):
    WebDriverWait(context.driver, 30).until(expected_conditions.text_to_be_present_in_element(
        (By.XPATH, '/html/body/app-root/app-login/html/body/form/div[1]'),
        'Usuário e/ou senha inválidos. Verifique o usuário e senha e tente novamente.'))
    context.driver.quit()
