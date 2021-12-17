import psutil
import time
from subprocess import call
from prettytable import PrettyTable

while True:
    # Clear and title
    call('clear')
    print("==============================Process Monitor\
        ======================================")

    # Battery
    battery = psutil.sensors_battery().percent
    print("----Battery Available: %d " % (battery,) + "%")

    #