from selenium import webdriver
from selenium.webdriver.chrome.service import Service


chrome_drive_path = "C:/Users/User/Desktop/Python-course/chromedriver_win32.exe"
ser = Service(chrome_drive_path)

driver = webdriver.Chrome(service=ser)

# driver.get("https://www.amazon.com/dp/B07XHQKM6W/ref=sbl_dpx_kitchen-electric-cookware_B08GC6PL3D_0")
# price = driver.find_element(by="class name", value="a-offscreen")
# print(price.get_attribute('innerHTML'))

driver.get("https://www.python.org/")
#get element by name
# search_bar = driver.find_element(by="name", value="q")
# print(search_bar.get_attribute("placeholder"))

#get element by class name
# logo = driver.find_element(by="class name", value="python-logo")
# print(logo.size)

#find element by css selector
# documentation_link = driver.find_element(by="css selector", value=".documentation-widget a")
# print(documentation_link.text)


#find element using xpath
# bug_link = driver.find_element(by="xpath", value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)


#task
#MY WAY
# # upcoming_events_link = driver.find_elements(by="css selector", value=".shrubbery ul li time")
# upcoming_events_data_link = driver.find_elements(by="css selector", value=".event-widget time")
#
# # events = upcoming_events_link[0].get_attribute('innerHTML')
# # print(events)
# #
# # new_event = events[26:31] + events[38:]
#
# event_date_list = [event.get_attribute('innerHTML')[26:31] + event.get_attribute('innerHTML')[38:] for event in upcoming_events_data_link]
# print(event_date_list)
#
# event_title_link = driver.find_elements(by="css selector", value=".event-widget .shrubbery ul li a")
#
#
# event_title_link_list = [event.get_attribute('innerHTML') for event in event_title_link]
# print(event_title_link_list)
#
# # dict_time = {"time": date for date in event_date_list}
# # print(dict(zip(event_date_list, event_title_link_list)))

####### ANGELA"S WAY ############
upcoming_events_data_link = driver.find_elements(by="css selector", value=".event-widget time")
event_times = [event.get_attribute('innerHTML')[26:31] + event.get_attribute('innerHTML')[38:] for event in upcoming_events_data_link]
print(event_times)
event_names = driver.find_elements(by="css selector", value=".event-widget .shrubbery ul li a")

events = {}

for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n],
        "name": event_names[n].text,
    }

print(events)


# print(new_event)
# driver.close()
driver.quit()
