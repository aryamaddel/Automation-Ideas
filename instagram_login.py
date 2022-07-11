from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def instagram_login(username, password):
    """
    This function logs into instagram using the username and password provided.
    """
    
    driver.get("https://www.instagram.com/accounts/login/")

    # Wait for the login page to load
    try:
        WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.NAME, "username")))  # username field is used because it is the first field in the login page
    except TimeoutException:
        print("Timed out waiting for page to load")
        driver.close()

    driver.find_element(by="name", value="username").send_keys(username)
    driver.find_element(by="name", value="password").send_keys(password)
    driver.find_element(by="xpath", value="//button[@type='submit']").click()



username = input("Enter your username: ")
password = input("Enter your password: ")
driver = webdriver.Chrome()
driver.maximize_window()
instagram_login(username, password) 

