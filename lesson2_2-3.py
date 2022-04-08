from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

link = "http://suninjuly.github.io/selects2.html"

try:

    browser = webdriver.Chrome()
    browser.execute_script("alert('Robots at work');")
            
finally:
    time.sleep(5)
    browser.quit()
