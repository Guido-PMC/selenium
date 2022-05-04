from flask import Flask
from flask import request
from flask import jsonify
from flask import Response
import json
import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pickle
import os
import time
from selenium import webdriver
#sele = os.popen('bash -c /opt/bin/start-selenium-standalone.sh')
#output = sele.read()
#print(output)
app = Flask(__name__)
@app.route('/test', methods = ['GET','POST'])
def test():
    if request.method == 'POST':
        data = request.json # a multidict containing POST data
        print(data)
        data = {'name': 'Guido'}
        webdriver_path = os.environ['WEBDRIVER']
        argument_path = os.environ['ARGUMENT']
        argument2_path = os.environ['ARGUMENT2']
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-dev-shm-usage")
        #options.add_argument("--user-data-dir=/Users/guigonzalez/Library/Application Support/Google/Chrome/") #e.g. C:\Users\You\AppData\Local\Google\Chrome\User Data
        #options.add_argument(r'--profile-directory=Profile 8') #e.g. Profile 3
        #options.add_argument(argument_path)
        #options.add_argument(argument2_path)
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

        return jsonify(data)
if __name__ == '__main__':
   app.run(host= '0.0.0.0', port=5005)
