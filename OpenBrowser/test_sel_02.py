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
    time.sleep(5)
    driver.quit()