""" This module helps to scrape all the commets from a given YT video
This modules uses selenium webdriver to open up the url in a chrome browser
There are better ways of doing this i.e.e using YT API, but that would require the
YT API key which is specific to the 
"""

import time
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Format the output as per the requirements.
# import pandas as pd 

# TODO: Pause the video in the starting itself, so that it doesn't buffer.
# TODO: Open chrome in an incognito mode.
# TODO: Close the Chrome browser.

data=[]
YT_URL = "https://www.youtube.com/watch?v=kuhhT_cBtFU&t=2s"
# This code will check for the latest chrome driver, if it is already present in the cache
# No need to download, otherwise download the latest version.
driver = Chrome(ChromeDriverManager().install())
wait = WebDriverWait(driver,15)
# Open the YT video from which to gather the comments
driver.get(YT_URL)
for item in range(3): 
        # This will wait till the loading of commentsis finished
        wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body"))).send_keys(Keys.END)
        time.sleep(10)
for comment in wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#content-text"))):
        data.append(comment.text)
        print(comment.text)
        print("\n")

print(data)