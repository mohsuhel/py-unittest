import unittest
import multiprocessing
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from flask import Flask

class TestWebsiteLoad(unittest.TestCase):
    def setUp(self):
        print("Setting up the test...")
        # Set up Chrome in headless mode
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=chrome_options)

    def test_website_load(self):
        print("Loading the website...")
        self.driver.get("http://127.0.0.1:3000/")

        try:
            print("Waiting for 'Hello, World!' text on the page...")
            WebDriverWait(self.driver, 10).until(
                EC.text_to_be_present_in_element((By.TAG_NAME, 'body'), 'Hello, World!')
            )
            print("'Hello, World!' found on the page!")
        except Exception as e:
            print(f"Failed to find 'Hello, World!' on the page: {e}")
            self.fail("Text 'Hello, World!' not found on the page")

    def tearDown(self):
        print("Tearing down the test...")
        self.driver.quit()

def run_flask_app():
    app = Flask(__name__)

    @app.route('/')
    def hello_world():
        return 'Hello, World!'

    app.run(host='127.0.0.1', port=3000)

if __name__ == "__main__":
    flask_process = multiprocessing.Process(target=run_flask_app)
    flask_process.start()

    unittest.main()

    flask_process.terminate()
    flask_process.join()
