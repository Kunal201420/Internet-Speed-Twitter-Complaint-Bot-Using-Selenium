from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

PROMISED_DOWN = 40
PROMISED_UP = 40
TWITTER_USERNAME = os.getenv('TWITTER_USERNAME')
TWITTER_PASSWORD = os.getenv('TWITTER_PASSWORD')


class InternetSpeedTwitterBot:
    def __init__(self, driver_path=None):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('detach', True)
        options.add_argument("--start-maximized")
        if driver_path:
            self.driver = webdriver.Chrome(executable_path=driver_path, options=options)
        else:
            self.driver = webdriver.Chrome(options=options)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        wait = WebDriverWait(self.driver, 20)

        sleep(3)
        accept_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#onetrust-accept-btn-handler')))
        accept_button.click()


        # Wait for and click the "Go" button to start the test
        go_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".start-button a")))
        go_button.click()

        # Wait for the download speed to be displayed
        sleep(50)
        download_speed = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "span.download-speed"))
        )

        # Wait for the upload speed to be displayed
        upload_speed = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "span.upload-speed"))
        )

        # Extract the speeds as floats
        self.down = float(download_speed.text)
        self.up = float(upload_speed.text)
        print(f"Download speed: {self.down} Mbps, Upload speed: {self.up} Mbps")

    def tweet_at_provider(self):
        self.driver.get("https://x.com/")
        wait = WebDriverWait(self.driver, 20)
        sleep(20)
        login_btn = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Sign in')))
        login_btn.click()

        sleep(30)
        # Enter email/username
        email_input = wait.until(EC.presence_of_element_located(
            (By.NAME, "text")
        ))
        email_input.send_keys(TWITTER_USERNAME)
        email_input.send_keys(Keys.ENTER)

        # Wait for password input
        password_input = wait.until(EC.presence_of_element_located(
            (By.NAME, "password")
        ))
        time.sleep(1)  # Small delay to ensure password input is ready
        password_input.send_keys(TWITTER_PASSWORD)
        password_input.send_keys(Keys.ENTER)

        # Wait until the tweet compose area loads
        tweet_box = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "div[aria-label='Tweet text']")
        ))

        tweet = (f"Hey Internet Provider, why is my internet speed "
                 f"{self.down}down/{self.up}up when I pay for "
                 f"{PROMISED_DOWN}down/{PROMISED_UP}up?")
        tweet_box.send_keys(tweet)

        # Locate and click the Tweet button
        tweet_button = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//div[@data-testid='tweetButtonInline']")
        ))
        tweet_button.click()

        print("Tweet posted successfully!")

        # Close the browser
        self.driver.quit()


if __name__ == "__main__":
    bot = InternetSpeedTwitterBot()
    bot.get_internet_speed()
    # Tweet only if speeds are below promised values
    if bot.down < PROMISED_DOWN or bot.up < PROMISED_UP:
        bot.tweet_at_provider()
    else:
        print("Internet speed is satisfactory. No tweet sent.")
        bot.driver.quit()
