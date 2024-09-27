import time

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.mark.positive
@allure.title("Verify create appointment")
@allure.description("Verify that URL")
def test_mini_Project1():
    driver = webdriver.Edge()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    driver.maximize_window()
    make_appointment_element = driver.find_element(By.ID, "btn-make-appointment")
    make_appointment_element.click()
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"
    time.sleep(3)
    #<input type="text" class="form-control" id="txt-username" name="username" placeholder="Username" value="" autocomplete="off">

    web_username_element = driver.find_element(By.ID, value="txt-username")
    web_username_element.send_keys("John Doe")

    password = driver.find_element(By.ID, value="txt-password")
    password.send_keys("ThisIsNotAPassword")

    submit_button = driver.find_element(By.ID, value="btn-login")
    submit_button.click()

    time.sleep(5)

    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/#appointment"

    # visible_text = driver.find_element(By.TAG_NAME, value="h2")
    # print(visible_text)
    # assert visible_text.text == "Make Appointment"

    assert driver.find_element(By.TAG_NAME, "h2").text == "Make Appointment"
    allure.attach(driver.get_screenshot_as_png(), name='makeappointment_screenshot')
    time.sleep(1)
    driver.quit()
