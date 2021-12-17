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

    # Network Info
    print("----Network Info----")
    table = PrettyTable(['Network', 'Status', 'Speed'])
    for key in psutil.net_if_stats().keys():
        name = key
        up = "Up" if psutil.net_if_stats()[key].isup else "Down"
        speed = psutil.net_if_stats()[key].speed
        table.add_row([name, up, speed])
    print(table)

    # Memory Info
    print("----Memory----")
    memory_table = PrettyTable(["Total", "Used",
                                "Available", "Percentage"])
    vm = psutil.virtual_memory()
    memory_table.add_row([
        vm.total,
        vm.used,
        vm.available,
        vm.percent
    ])
    print(memory_table)