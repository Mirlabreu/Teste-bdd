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


@given("a user accesses the login page (1a)")
def given(context):
    context.driver = webdriver.Chrome(os.path.join(ROOT_DIR, 'utils', 'driver', 'chromedriver.exe'))
    context.driver.get("https://homologacao.leadfortaleza.com.br/ead/login")

@when("the user submits his signup with user and password")
def when(context):
    username_field = context.driver.find_element_by_id("login")
    username_field.send_keys("mirlaalunaaudment")

    password_field = context.driver.find_element_by_id("password")
    password_field.send_keys("abcd1234")

    login_button = context.driver.find_element_by_id("login-btn")
    login_button.click()

@then("the system redirects the user to the logged area")
def then(context):
    wait = WebDriverWait(context.driver, 30)
    element = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/app-sidebar-layout/app-header/header/app-accessibility-bar/nav/div/div/div/button/img')))
    context.driver.quit()

