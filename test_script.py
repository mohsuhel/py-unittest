import logging
import requests
import unittest

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TestWebsiteLoader(unittest.TestCase):
    def test_load_atg_world_website(self):
        url = "https://atg.world"
        logger.info(f"Attempting to load the {url} website...")
        response = None
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()  # Raise an HTTPError for bad responses
            logger.info(f"Website {url} loaded successfully.")
        except requests.RequestException as e:
            logger.error(f"Failed to load the website: {e}")
        
        if response is None or not response.ok:
            logger.error(f"Website loading test failed. URL: {url}")
            self.fail(f"Website loading test failed. URL: {url}")

if __name__ == "__main__":
    unittest.main()
