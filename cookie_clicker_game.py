from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import threading
from apscheduler.schedulers.background import BlockingScheduler
import time



chrome_drive_path = "C:/Users/User/Desktop/Python-course/chromedriver_win32.exe"
ser = Service(chrome_drive_path)

driver = webdriver.Chrome(service=ser)

driver.get("http://orteil.dashnet.org/experiments/cookie/")
####################### BUTTON ##########################
# cookie = driver.find_element(by="css selector", value="#cookie")
# cursor = driver.find_element(by="css selector", value="#buyCursor")
# grandma = driver.find_element(by="css selector", value="#buyGrandma")
# factory = driver.find_element(by="css selector", value="#buyFactory")
# mine = driver.find_element(by="css selector", value="#buyMine")
# shipment = driver.find_element(by="css selector", value="#buyShipment")
# # alchemy_lab = driver.find_element(by="css selector", value="#buyAlchemy lab")
# portal = driver.find_element(by="css selector", value="#buyPortal")
# # time_machine = driver.find_element(by="css selector", value="#buyTime machine")
#
# money = driver.find_element(by="css selector", value="#money")

####################### Valua ##########################
# cursor_value = driver.find_element(by="css selector", value="#buyCursor b")
# grandma_value = driver.find_element(by="css selector", value="#buyGrandma b")
# factory_value = driver.find_element(by="css selector", value="#buyFactory b")
# cursor_cost = int((cursor_value.text).split(" - ")[1])
# grandma_cost = int((grandma_value.text).split(" - ")[1])
# factory_cost = int((factory_value.text).split(" - ")[1])

portal = driver.find_element(by="css selector", value="#buyPortal")
portal_value = driver.find_element(by="css selector", value="#buyPortal b")
portal_cost = portal_value.text.split(" - ")[1]
print(portal_cost)
portal_cost_fin = int(portal_cost[:1] + portal_cost[2:5] + portal_cost[6:])
print(portal_cost_fin)
# money_int = int(money.get_attribute('innerHTML'))



# def hello():
#     print("hello, world")
#
# t = threading.Timer(30.0, hello)
# t.start()

# for n in range(500):
#     cookie.click()
#     if n == 100:
#         grandma.click()


# def buy():
#   # if num == 15:
#   #     threading.Timer(5.0, buy).start()
#   #     sched.add_job(buy, 'interval', seconds=15)
#   #     sched.start()
#       cursor.click()


sched = BlockingScheduler()

# game_on = True
# while game_on:
#     cookie.click()
#     money = driver.find_element(by="css selector", value="#money")
#     curr_money = int(money.text)
#     # sched.add_job(buy, 'interval', seconds=15)
#     # sched.start()
#     # buy(int(money.text))
#     if curr_money > cursor_cost:
#         cursor.click()
#     # elif cursor_cost > grandma_cost:
#     #     grandma.click()
#     # elif curr_money > factory_cost:
#     #     factory.click()
#     # sched.add_job(buy, 'interval', seconds=15)
###########################################################################
timeout = 300
timeout_start = time.time()
print(timeout_start)
while time.time() < timeout_start + timeout:
    money = driver.find_element(by="css selector", value="#money")
    curr_money = int(money.text)
    test = 0
    cookie = driver.find_element(by="css selector", value="#cookie")
    cookie.click()
    # ---------------------- CURSOR ----------------------------------#
    cursor = driver.find_element(by="css selector", value="#buyCursor")
    cursor_value = driver.find_element(by="css selector", value="#buyCursor b")
    cursor_cost = int(cursor_value.text.split(" - ")[1])

    # ---------------------- GRADNMA ----------------------------------#
    grandma = driver.find_element(by="css selector", value="#buyGrandma")
    grandma_value = driver.find_element(by="css selector", value="#buyGrandma b")
    grandma_cost = int(grandma_value.text.split(" - ")[1])

    # ---------------------- FACTORY ----------------------------------#
    factory = driver.find_element(by="css selector", value="#buyFactory")
    factory_value = driver.find_element(by="css selector", value="#buyFactory b")
    factory_cost = int(factory_value.text.split(" - ")[1])

    # ---------------------- MINE ----------------------------------#
    mine = driver.find_element(by="css selector", value="#buyMine")
    mine_value = driver.find_element(by="css selector", value="#buyMine b")
    mine_cost = mine_value.text.split(" - ")[1]
    mine_cost_fin = int(mine_cost[:1] + mine_cost[2:])

    # ---------------------- SHIPMENT ----------------------------------#
    shipment = driver.find_element(by="css selector", value="#buyShipment")
    shipment_value = driver.find_element(by="css selector", value="#buyShipment b")
    shipment_cost = shipment_value.text.split(" - ")[1]
    shipment_cost_fin = int(shipment_cost[:1] + shipment_cost[2:])

    # ---------------------- PORTAL ----------------------------------#
    portal = driver.find_element(by="css selector", value="#buyPortal")
    portal_value = driver.find_element(by="css selector", value="#buyPortal b")
    portal_cost = portal_value.text.split(" - ")[1]
    portal_cost_fin = int(portal_cost[:1] + portal_cost[2:5] + portal_cost[6:])

    if curr_money > cursor_cost:
        cursor.click()
    elif curr_money > grandma_cost:
        grandma.click()
    elif curr_money > factory_cost:
        factory.click()
    elif curr_money > mine_cost_fin:
        mine.click()
    if curr_money > shipment_cost_fin:
        shipment.click()
    if curr_money > portal_cost_fin:
        portal.click()
    if test == 5:
        print((driver.find_element(by="css selector", value="#cps")).text)
        break
    test -= 1


driver.quit()