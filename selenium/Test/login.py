from selenium import webdriver
import time
import unittest
class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("C:\\Users\\user\\PycharmProjects\\test\\browsers\\chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_test(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        self.driver.find_element_by_id("btnLogin").click()
        self.driver.find_element_by_id("welcome").click()
        self.driver.find_element_by_link_text("Logout").click()
        time.sleep(10)

    @classmethod
    def tearDown(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Complete")

