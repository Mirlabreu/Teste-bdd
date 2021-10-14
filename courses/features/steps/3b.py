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


@given("a user accesses the enrollment courses page")
def given(context):
    context.driver = webdriver.Chrome(os.path.join(ROOT_DIR, 'utils', 'driver', 'chromedriver.exe'))
    context.driver.get("https://homologacao.leadfortaleza.com.br/ead/login")


@when("the user clicks Go to course")
def when(context):
    pass

# @and("the system displays the course name and course didactic contract")
# def and(context):
#     pass
#
# @and("the user accepts the didactic contract")
# def and(context):
#     pass

@then("the system redirects to the class page")
def then(context):
    pass