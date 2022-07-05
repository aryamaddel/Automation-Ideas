# The chromedriver which  is required to run the code is put in the Requirements folder
# Copy the chromediver to PATH variable on your computer


import webbrowser

from selenium import webdriver

Current_location = input("Enter your current location: ")
Address = input('Enter address: ')
driver = webdriver.Chrome()


def mapit(address):
    driver.get('https://www.google.com/maps/search/' + address)
    return driver.current_url


def get_directions(from_location, Address):
    url = 'https://www.google.com/maps/dir/' + from_location + '/' + Address
    return url


def open_map(url):
    webbrowser.open(url)


open_map(get_directions(Current_location, Address))
driver.close()
