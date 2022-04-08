from selenium import webdriver
import time

link = "http://suninjuly.github.io/registration1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_xpath('//div/label[text()="First name*"]/following-sibling::*[1]')
    input1.send_keys("A")
    input2 = browser.find_element_by_xpath('//div/label[text()="Last name*"]/following-sibling::*[1]')
    input2.send_keys("D")
    input3 = browser.find_element_by_xpath('//div/label[text()="Email*"]/following-sibling::*[1]')
    input3.send_keys("ddada@gmail.com")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)
    
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(20)
    browser.quit()
