from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver=webdriver.Chrome(r"/home/vidya-murali/Desktop/Vidya/python_projects/selenium_projects/chromedriver")
driver.get("https://www.facebook.com/")
action=ActionChains(driver)
email=input("Enter Your Email:")
password=input("Enter Your password:")

email_element=driver.find_element_by_id("email")
password_element=driver.find_element_by_id("pass")

email_element.send_keys(email)
password_element.send_keys(password)
login_button=driver.find_element_by_name("login")

action.click(on_element=login_button)
action.perform()
print("performed")
# driver.close()
