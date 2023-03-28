from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys


chrome_drive_path = "C:/Users/User/Desktop/Python-course/chromedriver_win32.exe"
ser = Service(chrome_drive_path)

driver = webdriver.Chrome(service=ser)

# driver.get("https://en.wikipedia.org/wiki/Main_Page")

# article_num = driver.find_element(by="css selector", value="#articlecount a")
# print(article_num.text)

# # #################clicking on the element #################################
# article_num.click()

# content_portals = driver.find_element(by="link text", value="Content portals")
# content_portals.click()


# # #################typing on the search bar #################################
# search = driver.find_element(by="name", value="search")
# search.send_keys("Python")
# search.send_keys(Keys.RETURN)

##################### SIGN UP CHALLENGE #############################
# driver.get("http://secure-retreat-92358.herokuapp.com/")
# first_name = driver.find_element(by="name", value="fName")
# first_name.send_keys("Angela")
# last_name = driver.find_element(by="name", value="lName")
# last_name.send_keys("Yu")
# email = driver.find_element(by="name", value="email")
# email.send_keys("angela@email.com")
#
# submit = driver.find_element(by="css selector", value="form button")
# submit.click()

driver.quit()