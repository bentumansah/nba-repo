import time

def countdown_timer(time_sec):
    while time_sec:
        min, sec = divmod(int(time_sec), 60)
        timer = "{:02d} : {:02d}".format(min,sec)     #Round min and sec to 2 decimal places
        print(timer)
        time.sleep(1)   #Delay timer by 1 sec
        time_sec -= 1           #Decrease time_sec by 1 sec and store it into time_sec
    print("Time UP")


time_sec = input("Enter the time in seconds: ")
countdown_timer(int(time_sec))