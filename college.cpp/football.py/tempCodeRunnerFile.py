from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd
#extract data from data import into csv file
chrome_options = Options()
chrome_options.add_argument("--headless")
website='https://www.adamchoi.co.uk/overs/detailed'
path = 'C:/Users/sk545/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe'
service = Service(path)
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get("https://storage.googleapis.com/chrome-for-testing-public/126.0.6478.126/win64/chrome-win64.zip")
print(driver.title)
driver = webdriver.Chrome('C:/Users/sk545/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe')
driver.get(website)
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)
driver.quit()