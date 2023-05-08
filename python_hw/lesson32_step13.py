from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest


class TestAbs(unittest.TestCase):
    def test_registration1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        input1 = browser.find_element(By.XPATH,
                                      "//div[@class='first_block']/div[1]/input[@class='form-control first']")
        input1.send_keys("Mary")
        input2 = browser.find_element(By.XPATH,
                                      "//div[@class='first_block']/div[2]/input[@class='form-control second']")
        input2.send_keys("Popins")
        input3 = browser.find_element(By.XPATH,
                                      "//div[@class='first_block']/div[3]/input[@class='form-control third']")
        input3.send_keys("abc@abc.com")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text,
                         f"Should be '{welcome_text}'")

        time.sleep(5)
        browser.quit()

    def test_registration2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        input1 = browser.find_element(By.XPATH,
                                      "//div[@class='first_block']/div[1]/input[@class='form-control first']")
        input1.send_keys("Mary")
        input2 = browser.find_element(By.XPATH,
                                      "//div[@class='first_block']/div[2]/input[@class='form-control second']")
        input2.send_keys("Popins")
        input3 = browser.find_element(By.XPATH,
                                      "//div[@class='first_block']/div[3]/input[@class='form-control third']")
        input3.send_keys("abc@abc.com")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text,
                         f"Should be '{welcome_text}'")

        time.sleep(5)
        browser.quit()


if __name__ == "__main__":
    unittest.main()
