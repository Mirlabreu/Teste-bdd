import time
from _ast import Assert

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


@given("a user accesses the login page (2a)")
def given(context):
    context.driver = webdriver.Chrome(os.path.join(ROOT_DIR, 'utils', 'driver', 'chromedriver.exe'))
    context.driver.get("https://homologacao.leadfortaleza.com.br/ead/login")
    context.driver.maximize_window()

@when("the user clicks I need help")
def when(context):
    button_help = context.driver.find_element_by_xpath("/html/body/app-root/app-login/html/body/form/div[6]/a[2]")
    button_help.click()




@then("the system redirects to the home page of the platform https://leadfortaleza.com.br/portal")
def then(context):

    WebDriverWait(context.driver, 10).until(EC.url_to_be('https://leadfortaleza.com.br/portal'))
    context.driver.quit()



