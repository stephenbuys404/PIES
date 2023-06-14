#selenium
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

#https://www.google.com/chrome/thank-you.html?brand=CHBF&statcb=0&installdataindex=empty&defaultbrowser=0
#https://sites.google.com/chromium.org/driver/?pli=1

driver = webdriver.Chrome(r'C:\Users\username\Downloads\chromedriver_win32\chromedriver.exe')
driver.implicitly_wait(30)
driver.get('https://www.gmail.com')
print(driver.page_source)
id_box = driver.find_element(By.NAME, 'identifier')
id_box = driver.find_element(By.ID, 'identifierId')
id_box.send_keys('username')
input('Click Next To Continue.')
pass_box = driver.find_element(By.NAME, 'Passwd')
pass_box.send_keys('password')
#login_button = driver.find_element(By.NAME, 'LgbsSe')
#login_button.click()