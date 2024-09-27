import pytest
import time
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

@pytest.mark.negative
def test_vwo_wait():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://app.vwo.com/")
    username = driver.find_element(By.CSS_SELECTOR, "[id = 'login-username'] ")
    username.send_keys("admin@gmail.com")
    password = driver.find_element(By.CSS_SELECTOR, "[name = 'password'] ")
    password.send_keys("admin")
    submit_button = driver.find_element(By.ID, "js-login-btn")
    submit_button.click()
    WebDriverWait(driver=driver, timeout=5).until(EC.visibility_of_element_located((By.ID, "js-notification-box-msg")))
    error_msg_box = driver.find_element(By.ID, "js-notification-box-msg")
    print(error_msg_box.text)
    # assert error_msg_box.text == "Your email, password, IP address or location did not match"
    driver.quit()
