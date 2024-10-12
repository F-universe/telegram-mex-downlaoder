Telegram Message Scraper
This project is a Python script that uses Selenium to automate the extraction of messages from Telegram Web and save them into a text file. The messages, along with their timestamps, are written to an output file after the user logs in manually through the Telegram Web interface.

Prerequisites
Before running the script, ensure you have the following installed:

Python 3.x - Download Python
Google Chrome - Download Chrome
ChromeDriver - Ensure the correct version of ChromeDriver is downloaded. The version should match your installed version of Google Chrome.
Download ChromeDriver
Selenium - Install the Selenium Python package using the command:
bash

pip install selenium
Setup
ChromeDriver Path
Update the chrome_driver_path variable in the script to match the location where ChromeDriver is installed on your machine:

python

chrome_driver_path = 'C:/path/to/your/chromedriver.exe'
Output File Path
The messages and timestamps will be saved to a text file. You can configure the output file path by updating the output_file_path variable:

python

output_file_path = 'C:/path/to/output/file.txt'
Script Description
The script opens the Telegram Web interface in a maximized Chrome browser window.
It waits for the user to log in manually.
After login, the script scrapes messages and timestamps from the chat and writes them to the specified output file.
After scraping, the browser window closes automatically.
Usage
Clone this repository or copy the script to your local machine.
Open a terminal and navigate to the folder containing the script.
Run the script using Python:
bash

python telegram_scraper.py
Once the browser opens, log into your Telegram Web account.
After logging in, return to the terminal and press "Enter" to start the scraping process.
The messages, along with timestamps, will be saved in the output file at the path specified.
Customization
You can modify the script to:

Scrape other types of elements (e.g., user names, media content).
Change the logic to scrape messages from specific chat groups or individual conversations.
Important Notes
This script relies on manual login to Telegram Web. Automation of the login process is not implemented for security reasons.
Make sure your Chrome version is compatible with the installed version of ChromeDriver.
Update paths for ChromeDriver and the output file according to your system.
