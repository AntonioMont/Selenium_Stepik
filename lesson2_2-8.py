from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:

    browser = webdriver.Chrome()
    browser.get(link)
    
    input1 = browser.find_element_by_name("firstname")
    input1.send_keys("AA")
    input1 = browser.find_element_by_name("lastname")
    input1.send_keys("DD")
    input1 = browser.find_element_by_name("email")
    input1.send_keys("DADA@gmail.com")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, "lesson2_2-8.txt")
    element = browser.find_element_by_id("file")
    element.send_keys(file_path)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    
            
finally:
    time.sleep(10)
    browser.quit()
