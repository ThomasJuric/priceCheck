from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import os

driver = webdriver.Chrome('./chromedriver.exe')
product = raw_input("Please enter a product you wish to search for: ")

print(product)



#driver.get('https://www.amazon.ca/')
#driver.get('https://www.ebay.ca/')
#driver.get('https://www.apple.com/ca/')
#driver.get('https://www.microsoft.com/en-ca?SilentAuth=1')
#driver.get('https://www.kijiji.ca/')
