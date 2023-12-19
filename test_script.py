import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

class TestWebsiteLoad(unittest.TestCase):
    def setUp(self):
        print("Setting up the test...")
        # Set up Chrome in headless mode
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=chrome_options)

    def test_website_load(self):
        print("Loading the website...")
        self.driver.get("https://atg.world/")

        try:
            print("Waiting for an element with class 'landing-signin-btn' to be present...")
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
