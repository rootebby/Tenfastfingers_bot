from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox(executable_path="C:\geckodriver.exe")
sleep(2)
browser.get("https://10fastfingers.com/typing-test/turkish")
allow = browser.find_element(By.CLASS_NAME,r'CybotCookiebotDialogBodyButton')
allow.click()
sleep(1)
word = browser.find_element(By.CLASS_NAME,r'highlight')
area = browser.find_element(By.ID,r'inputfield')
sleep(2)
try:
        
    while True:
        word = browser.find_element(By.CLASS_NAME,r'highlight')
        area.send_keys(str(word.text))
        area.send_keys(Keys.SPACE)
        sleep(0.03)
        
except:
    sleep(100)
    #browser.quit()