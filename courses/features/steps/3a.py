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


@given("a user accesses the platform homepage")
def given(context):
    context.driver = webdriver.Chrome(os.path.join(ROOT_DIR, 'utils', 'driver', 'chromedriver.exe'))
    context.driver.get("https://homologacao.leadfortaleza.com.br/ead/login")


@when("the user clicks My Courses")
def when(context):
    pass

@then("the system displays the ongoing courses of Application Development Fundamentals with Visual C# and Entrepreneurship and Ethics")
def then(context):
    pass
