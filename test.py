import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
import time
import HtmlTestRunner


class GoogleTest(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.headless = False  
        service = Service(GeckoDriverManager().install())
        self.driver = webdriver.Firefox(service=service, options=options)

    def test_search(self):
        self.driver.get("https://www.google.com/?hl=es")

        self.assertIn("Google", self.driver.title)

        search_box = self.driver.find_element(By.NAME, "q")

        search_box.send_keys("Selenium WebDriver")
        search_box.submit()

        time.sleep(3)

        self.assertIn("selenium", self.driver.page_source.lower())

        self.driver.save_screenshot("google_search_result.png")

    def test_search_images(self):
        self.driver.get("https://www.google.com/?hl=es")


        images_tab = self.driver.find_element(By.LINK_TEXT, "Imágenes")
        images_tab.click()

        time.sleep(3)

        self.assertIn("imghp", self.driver.current_url)

        self.driver.save_screenshot("google_images_result.png")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(
            output="./report",
            report_name="GoogleTestReport",
            combine_reports=True
        ),
        verbosity=2
    )
