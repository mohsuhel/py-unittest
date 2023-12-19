import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestWebsiteLoad(unittest.TestCase):
    def setUp(self):
        print("Setting up the test...")
        self.driver = webdriver.Chrome()

    def test_website_load(self):
        print("Loading the website...")
        self.driver.get("https://atg.world/")

        try:
            print("Waiting for an element with ID 'your_element_id' to be present...")
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'landing-signin-btn'))
            )
            print("Website loaded successfully!")
        except Exception as e:
            print(f"Failed to load the website: {e}")
            self.fail("Website did not load successfully")

    def tearDown(self):
        print("Tearing down the test...")
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
