import time
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pandas as pd   

data=[]
# with Chrome(executable_path="/Users/pratham/Documents/data/chromedriver") as driver:
# with Chrome(ChromeDriverManager().install()) as driver:
driver = Chrome(ChromeDriverManager().install())
wait = WebDriverWait(driver,15)
driver.get("https://www.youtube.com/watch?v=kuhhT_cBtFU&t=2s")
for item in range(200): 
        wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body"))).send_keys(Keys.END)
        time.sleep(15)
for comment in wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#content-text"))):
        data.append(comment.text)
    
df = pd.DataFrame(data, columns=['comment'])
df.head()