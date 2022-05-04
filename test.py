"""from selenium import webdriver
import time
driver = webdriver.Safari()
driver.get("https://web.whatsapp.com/send?phone=5491121708911")
time.sleep(2)

# Replace the below string with your own message
string = "Message sent using Python!!!"

inp_xpath = '//div[@class="_13NKt copyable-text selectable-text"][@data-tab="9"]'
input_box = wait.until(EC.presence_of_element_located((
    By.XPATH, inp_xpath)))
for i in range(100):
    input_box.send_keys(string + Keys.ENTER)
    time.sleep(1)
driver.quit()
"""

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pickle
import os
import time
from selenium import webdriver



webdriver_path = os.environ['WEBDRIVER']
argument_path = os.environ['ARGUMENT']
argument2_path = os.environ['ARGUMENT2']
options = webdriver.ChromeOptions()
#options.add_argument("--user-data-dir=/Users/guigonzalez/Library/Application Support/Google/Chrome/") #e.g. C:\Users\You\AppData\Local\Google\Chrome\User Data
#options.add_argument(r'--profile-directory=Profile 8') #e.g. Profile 3
options.add_argument(argument_path)
options.add_argument(argument2_path)


driver = webdriver.Chrome(webdriver_path, chrome_options=options)

driver.get("https://web.whatsapp.com/send?phone=5491121708911")

wait = WebDriverWait(driver, 600)

# Replace 'Friend's Name' with the name of your friend
# or the name of a group
target = '"Guido"'

# Replace the below string with your own message
string = "Message sent using Python!!!"

time.sleep(20)
print("Pruebo introducir texto")
print(driver.get_cookies())

inp_xpath = '//div[@class="_13NKt copyable-text selectable-text"][@data-tab="10"]'
input_box = wait.until(EC.presence_of_element_located((
    By.XPATH, inp_xpath)))
input_box.send_keys(string + Keys.ENTER)
time.sleep(1)








"""

import os
from selenium import webdriver

dir_path = os.getcwd()
profile = os.path.join(dir_path, "profile", "wpp")
options = webdriver.ChromeOptions()
options.add_argument(
    r"user-data-dir={}".format(profile))

browser = webdriver.Chrome("./chromedriver.exe", chrome_options=options)

browser.get("https://web.whatsapp.com")
"""
