# short script that shows system info

import shutil
import psutil

def checkDiskUsage(disk):
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free

def checkCpuUsage():
    usage = psutil.cpu_percent(1)
    return usage < 75

if not checkDiskUsage('/') or not checkCpuUsage():
    print('ERROR!')
else:
    print("Everything is OK!")