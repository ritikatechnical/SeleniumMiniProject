import time
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType


# Selenium 4

@pytest.mark.positive
@allure.title("URL changing after clicking on make appointment button ")
@allure.description("TC#1 - Simple Login check on CURA katalong Website.")
def test_mini_katalon():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://katalon-demo-cura.herokuapp.com/")

    # make_appointment_btn = driver.find_element(By.LINK_TEXT, "Make Appointment")
    make_appointment_btn = driver.find_element(By.XPATH, value="//a[@id='btn-make-appointment']")
    make_appointment_btn.click()
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"
    print(driver.current_url)
    time.sleep(2)
    username = driver.find_element('xpath', "//input[@id='txt-username']")
    username.send_keys("John Doe")
    password = driver.find_element(By.ID, "txt-password")
    password.send_keys("ThisIsNotAPassword")
    submit_btn = driver.find_element(By.ID, "btn-login")
    submit_btn.click()
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/#appointment"
    time.sleep(2)
    driver.quit()
