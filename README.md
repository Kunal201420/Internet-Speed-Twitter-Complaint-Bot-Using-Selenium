# InternetSpeedTwitterBot

A Python bot that uses Selenium to check your internet speed on [speedtest.net](https://www.speedtest.net/) and tweets a complaint automatically if the speed is below your promised internet plan.

---

## Features

- Automates the process of running an internet speed test.
- Extracts download and upload speeds from speedtest.net.
- Logs in to Twitter (now X.com) using your credentials securely loaded from environment variables.
- Tweets a complaint message mentioning your internet provider if speeds are below specified thresholds.
- Uses Selenium WebDriver for browser automation with Chrome.

---

## Prerequisites

- Python 3.7 or higher
- Google Chrome browser installed
- ChromeDriver matching your Chrome version ([Download here](https://sites.google.com/chromium.org/driver/))
- A Twitter account for posting tweets

---

## Setup

1. Clone the repository or copy the `InternetSpeedTwitterBot` script.

2. Install required Python packages.

3. Create a `.env` file in the project directory with your Twitter login credentials.

4. (Optional) Download ChromeDriver and provide its path when initializing the bot (if not on system PATH).




The bot will:

1. Open Chrome and navigate to speedtest.net.
2. Run a speed test and retrieve the download and upload speeds.
3. Compare the speeds with the promised speeds (default 40 Mbps down and up).
4. If speeds are below promised, it will log in to Twitter and tweet a complaint.
5. Otherwise, it will print that the internet speed is satisfactory and close the browser.

---

## Configuration

In the script, you can modify:

- `PROMISED_DOWN`: Your promised download speed (default 40 Mbps).
- `PROMISED_UP`: Your promised upload speed (default 40 Mbps).
- `TWITTER_USERNAME` and `TWITTER_PASSWORD`: Loaded from `.env`.

---

## Notes

- The bot uses Selenium Chrome WebDriver with options to keep the browser open during the test.
- It includes waits and delays to handle dynamic page loading.
- Make sure to keep your `.env` file private and not commit it to version control.

---

## Disclaimer

Use responsibly and consider Twitter's automation policies. This bot is intended for personal use to monitor and report internet speeds.

---

## License

This project is licensed under the MIT License.





