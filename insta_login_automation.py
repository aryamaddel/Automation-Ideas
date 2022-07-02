import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.instagram.com/")
time.sleep(0.175)
enter_usr_name_bar = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
# put username
enter_usr_name_bar.send_keys('<user_name>')
enter_usr_pwd_bar = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
# put password
enter_usr_pwd_bar.send_keys('<password>')
login_button = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]')
login_button.click()
# close tab
driver.quit()
