import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://automationplayground.com/crm/login.html")
driver.implicitly_wait(10)
#Login
inputEmail = driver.find_element(By.XPATH,"//*[@id='email-id']").send_keys('segun@gamil.com')
inputPassword = driver.find_element(By.XPATH,"//*[@id='password']").send_keys('segun123')
rememberme = driver.find_element(By.XPATH,"//*[@id='remember']").click()
siginButton = driver.find_element(By.XPATH,"/html/body/section/div/div/div/div/form/button").click()

#Add New Customer
addCustomer = driver.find_element(By.XPATH,"//*[@id='new-customer']").click()
customeremail = driver.find_element(By.XPATH,"//*[@id='EmailAddress']").send_keys('segun123@gmail.com')
customerFname = driver.find_element(By.XPATH,"//*[@id='FirstName']").send_keys('Segun')
customerLname = driver.find_element(By.XPATH,"//*[@id='LastName']").send_keys('Ayanloye')
customerCity = driver.find_element(By.XPATH,"//*[@id='City']").send_keys('Lagos')
customerState = driver.find_element(By.XPATH,"//*[@id='StateOrRegion']").click()
selectState = driver.find_element(By.XPATH,"/html/body/section/div/div/div/div/form/div[5]/select/option[4]").click()
customerGender = driver.find_element(By.XPATH,"//*[@id='loginform']/div/div/div/div/form/div[6]/input[1]").click()
promotionList =driver.find_element(By.XPATH,"//*[@id='loginform']/div/div/div/div/form/div[7]/input").click()
submitForm = driver.find_element(By.XPATH,"//*[@id='loginform']/div/div/div/div/form/button").click()

#Signout
signoutButton = driver.find_element(By.XPATH,"/html/body/nav/ul/li/a").click()
