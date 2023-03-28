# from apscheduler.schedulers.background import BlockingScheduler
# def print_t():
#   print("Hi")
#
# sched = BlockingScheduler()
# sched.add_job(print_t, 'interval', seconds =5) #will do the print_t work for every 60 seconds
#
# sched.start()
####################################################
import time

# timeout variable can be omitted, if you use specific value in the while condition
timeout = 300   # [seconds]

timeout_start = time.time()
print(timeout_start)
print(timeout_start + timeout)


while time.time() < timeout_start + timeout:
    test = 0
    if test == 5:
        break
    test -= 1


timeout = time.time() + 5
five_min = time.time() + 60*5 # 5minutes

while True:
    #Every 5 seconds:
    if time.time() > timeout:
        pass
        # Add another 5 seconds until the next check
        timeout = time.time() + 5
        if time.time() > five_min:
            print("End")
            break