from selenium import webdriver
import time

link = "http://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    robots_radio = browser.find_element_by_id("robotsRule")
    robots_checked = robots_radio.get_attribute("checked")
    print("robot radiobutton is: ", robots_checked)
    assert robots_checked == "true", "Robots radiobutton is not selected by default"
            
finally:
    time.sleep(10)
    browser.quit()
