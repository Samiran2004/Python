import os
import datetime

# command = "df -h"

def checkCpu(command):
    print(os.system(command))

def checkDate(command):
    print(os.system(command))

def checkUpTime(command):
    print(os.system(command))

def checkRam(command):
    print(os.system(command))

def show_date():
    print(datetime.datetime.today())

show_date()