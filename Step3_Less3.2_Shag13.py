from selenium import webdriver
import time
import unittest

link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"

try:
    class TestRegForms(unittest.TestCase):
        def test_test1(self):
            browser = webdriver.Chrome()
            browser.get(link1)
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

            self.assertEqual("Congratulations! You have successfully registered!",welcome_text)

        def test_test2(self):
            browser = webdriver.Chrome()
            browser.get(link2)

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

            self.assertEqual("Congratulations! You have successfully registered!",welcome_text)
finally:
            if __name__ == "__main__":
                unittest.main()
