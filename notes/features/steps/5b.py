import time
from behave import *
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import os
import sys

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
path_dir = os.path.join(ROOT_DIR, "utils")
sys.path.append(path_dir)



@given("a user accesses My Notes (5b)")
def given(context):
    context.driver = webdriver.Chrome(os.path.join(ROOT_DIR, 'utils', 'driver', 'chromedriver.exe'))
    context.driver.get("https://homologacao.leadfortaleza.com.br/ead/login")
    context.driver.maximize_window()

@when("the user clicks on the desired lesson")
def when(context):
    username_field = context.driver.find_element_by_id("login")
    username_field.send_keys("mirlaalunaaudment")

    password_field = context.driver.find_element_by_id("password")
    password_field.send_keys("abcd1234")

    login_button = context.driver.find_element_by_id("login-btn")
    login_button.click()

    wait = WebDriverWait(context.driver, 30)
    notes_menu = wait.until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/app-sidebar-layout/nav/ul/div/li[5]/a[1]/span')))
    notes_menu.click()

    while True:
        if not context.driver.find_element_by_xpath(
                '/html/body/app-root/app-sidebar-layout/div/div/ngx-spinner').is_displayed():
            break

    context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    element = context.driver.find_element_by_xpath('/html/body/app-root/app-sidebar-layout/div/div/app-results/div/app-small-header/div[4]/div[3]/div[5]/div[1]/button')
    context.driver.execute_script("arguments[0].click();", element)


@then("the system displays Evaluation and Workshop")
def then(context):

    wait = WebDriverWait(context.driver, 30)
    wait.until(EC.presence_of_element_located((By.XPATH,
                                                    '/html/body/app-root/app-sidebar-layout/div/div/app-results/div/app-small-header/div[4]/div[3]/div[4]/div[1]/button/span')))
    wait.until(EC.presence_of_element_located((By.XPATH,
                                               '/html/body/app-root/app-sidebar-layout/div/div/app-results/div/app-small-header/div[4]/div[3]/div[2]/div[2]/div/div[2]/div/span')))
    time.sleep(15)
    context.driver.quit()