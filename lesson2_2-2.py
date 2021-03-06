from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

link = "http://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("num1")
    x = x_element.text
    y_element = browser.find_element_by_id("num2")
    y = y_element.text
    SUM = str(int(x)+int(y))
    
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(SUM)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()
            
finally:
    time.sleep(5)
    browser.quit()
