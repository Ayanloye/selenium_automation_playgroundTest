import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://automationplayground.com/crm/login.html")
driver.implicitly_wait(10)
#Login
driver.find_element(By.XPATH,"//*[@id='email-id']").send_keys('segun@gamil.com')
driver.find_element(By.XPATH,"//*[@id='password']").send_keys('segun123')
driver.find_element(By.XPATH,"//*[@id='remember']").click()
driver.find_element(By.XPATH,"/html/body/section/div/div/div/div/form/button").click()

#Add New Customer
driver.find_element(By.XPATH,"//*[@id='new-customer']").click()
driver.find_element(By.XPATH,"//*[@id='EmailAddress']").send_keys('segun123@gmail.com')
driver.find_element(By.XPATH,"//*[@id='FirstName']").send_keys('Segun')
driver.find_element(By.XPATH,"//*[@id='LastName']").send_keys('Ayanloye')
driver.find_element(By.XPATH,"//*[@id='City']").send_keys('Lagos')
driver.find_element(By.XPATH,"//*[@id='StateOrRegion']").click()
driver.find_element(By.XPATH,"/html/body/section/div/div/div/div/form/div[5]/select/option[4]").click()
driver.find_element(By.XPATH,"//*[@id='loginform']/div/div/div/div/form/div[6]/input[1]").click()
driver.find_element(By.XPATH,"//*[@id='loginform']/div/div/div/div/form/div[7]/input").click()
driver.find_element(By.XPATH,"//*[@id='loginform']/div/div/div/div/form/button").click()

#Signout
driver.find_element(By.XPATH,"/html/body/nav/ul/li/a").click()
time.sleep(3)
