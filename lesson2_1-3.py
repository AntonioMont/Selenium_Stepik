from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    
    x_element = browser.find_element_by_id("treasure")
    x = x_element.get_attribute("valuex")
    y = calc(x)

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

    robots_checkbox = browser.find_element_by_id("robotCheckbox")
    robots_checkbox.click()
     
    robots_radio = browser.find_element_by_id("robotsRule")
    robots_radio.click()

    button = browser.find_element_by_css_selector("button.btn")
    button.click()
            
finally:
    time.sleep(10)
    browser.quit()
