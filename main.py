from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import os
from selenium.webdriver.common.keys import Keys

# Function to search the product name given by the user on Amazon
def for_amazon(product):
    print(product)
    print ("Checking Amazon")
    driver.get('https://www.amazon.ca/')
    amazon_searchBar = driver.find_element_by_xpath("//*[@id=\"twotabsearchtextbox\"]")
    amazon_searchBar.send_keys(product)
    amazon_searchBar.send_keys(Keys.RETURN)


def for_ebay(product):
    print ("Checking Ebay")
    driver.get('https://www.ebay.ca/')
    ebay_searchBar = driver.find_element_by_xpath("//*[@id=\"gh-ac\"]")
    ebay_searchBar.send_keys(product)
    ebay_searchBar.send_keys(Keys.RETURN)
    print(product)



def for_apple(product):
    print(product)
    print("Checking Apple")
    driver.get('https://www.apple.com/ca/')
    driver.find_element_by_xpath("//*[@id=\"ac-gn-link-search\"]").click()
    apple_searchBar = driver.find_element_by_xpath("//*[@id=\"ac-gn-searchform-input\"]")
    apple_searchBar.send_keys(product)
    apple_searchBar.send_keys(Keys.RETURN)
    driver.find_element_by_xpath("//*[@id=\"exploreCurated\"]/div[1]/div[2]/ul/li[2]/a").click()



def for_microsoft(product):
    print(product)
    print("Checking Microsoft")
    driver.get('https://www.microsoft.com/en-ca')
    driver.find_element_by_xpath("//*[@id=\"search\"]").click()
    microsoft_searchBar = driver.find_element_by_xpath("//*[@id=\"cli_shellHeaderSearchInput\"]")
    microsoft_searchBar.send_keys(product)
    microsoft_searchBar.send_keys(Keys.RETURN)




def for_kijiji(product):
    print(product)
    print("Checking Kijij")
    driver.get('https://www.kijiji.ca/')
    kijiji_searchBar = driver.find_element_by_xpath("//*[@id=\"SearchKeyword\"]")
    kijiji_searchBar.send_keys(product)
    kijiji_searchBar.send_keys(Keys.RETURN)




driver = webdriver.Chrome('./chromedriver.exe')
product = raw_input("Please enter a product you wish to search for: ")

test = 1
if test == 1:
    for_amazon(product)
    time.sleep(2)
    for_ebay(product)
    time.sleep(2)
    for_apple(product)
    time.sleep(2)
    for_microsoft(product)
    time.sleep(2)
    for_kijiji(product)
if test == 2:
    
    for_microsoft(product)
    for_kijiji(product)



#driver.get('https://www.ebay.ca/')
#driver.get('https://www.apple.com/ca/')
#driver.get('https://www.microsoft.com/en-ca?SilentAuth=1')
#driver.get('https://www.kijiji.ca/')
