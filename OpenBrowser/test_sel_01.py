import time

from selenium import webdriver


def test_sel_Program1():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com/")
    driver.maximize_window()
    print(driver.page_source)
    driver.refresh()
    driver.back()
    driver.forward()
    time.sleep(10)
    driver.close() #close only current tab
    driver.quit()  #close all the tabs and session id == null
    # print(driver.session_id)
    # print(driver.title)
    # assert driver.title == "Login - VWO"