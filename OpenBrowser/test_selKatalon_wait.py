import time

import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from allure_commons.types import AttachmentType


@pytest.mark.negative
@allure.title("Katalon able to login by valid username & password")
def test_katalon_Negative():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    allure.attach(driver.get_screenshot_as_png(), name="Step1", attachment_type=AttachmentType.PNG)
    WebDriverWait(driver=driver, timeout=2).until(
        ec.element_to_be_clickable((By.CSS_SELECTOR, "#btn-make-appointment")))

    make_appoinment = driver.find_element(By.CSS_SELECTOR, "#btn-make-appointment")
    make_appoinment.click()

    WebDriverWait(driver=driver, timeout=2).until(ec.url_contains("/profile.php#login"))
    allure.attach(driver.get_screenshot_as_png(), name="Step2", attachment_type=AttachmentType.PNG)

    username = driver.find_element(By.CSS_SELECTOR, "[name='username']")
    username.send_keys("admin@gmail.com")
    password = driver.find_element(By.CSS_SELECTOR, "#txt-password")
    password.send_keys("admin")
    button_click = driver.find_element(By.ID, "btn-login")
    button_click.click()
    allure.attach(driver.get_screenshot_as_png(), name="Step3", attachment_type=AttachmentType.PNG)
    WebDriverWait(driver=driver, timeout=20).until(
        ec.presence_of_element_located((By.CSS_SELECTOR, "[class='lead text-danger']")))
    allure.attach(driver.get_screenshot_as_png(), name="Step4", attachment_type=AttachmentType.PNG)

    driver.quit()

@pytest.mark.positive
def test_katalon_positive():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    allure.attach(driver.get_screenshot_as_png(), name="Step1", attachment_type=AttachmentType.PNG)
    WebDriverWait(driver=driver, timeout=5).until(ec.element_to_be_clickable((By.CSS_SELECTOR, "#btn-make-appointment")))
    make_appoinment = driver.find_element(By.CSS_SELECTOR, "#btn-make-appointment")
    make_appoinment.click()
    # assert driver.current_url == "/profile.php#login"
    WebDriverWait(driver=driver, timeout=5).until(ec.url_contains("/profile.php#login"))
    allure.attach(driver.get_screenshot_as_png(), name="Step1", attachment_type=AttachmentType.PNG)
    username = driver.find_element(By.CSS_SELECTOR, "#txt-username")
    password = driver.find_element(By.CSS_SELECTOR, "#txt-password")
    username.send_keys("John Doe")
    password.send_keys("ThisIsNotAPassword")

    WebDriverWait(driver=driver, timeout=3).until(
        ec.element_to_be_clickable(((By.CSS_SELECTOR, "#btn-login")))
    )

    btn_login = driver.find_element(By.CSS_SELECTOR, "#btn-login")
    btn_login.click()
    allure.attach(driver.get_screenshot_as_png(), name="Step3_Login_Click", attachment_type=AttachmentType.PNG)
    WebDriverWait(driver=driver, timeout=5).until(ec.url_contains("/#appointment"))
    make_appoinment_h2 = driver.find_element(By.XPATH, "//h2[text()='Make Appointment']")
    assert make_appoinment_h2.text == "Make Appointment"
    allure.attach(driver.get_screenshot_as_png(), name="Step3_Verify_h2_login", attachment_type=AttachmentType.PNG)

