# ROSE CLI - CMD utility to display notification on task completion

# Running Rose:


# Standard libraries
import sys
import logging
import threading
from os import path
from time import sleep
import subprocess

# Third party libraries
from win10toast import ToastNotifier

class RoseTask:

    def __init__(self):
        print("Thank you for using ROSE CLI. To view a list of available commands, type 'rose help'\n")

        # Constants
        self.ROSE_VERSION = '0.0.1'

    # function that displays the application version
    def version(self):
        print("Current rose version : ", self.ROSE_VERSION)

    # function to execute the CMD task
    def cmdTask(self, command):
        subprocess.call(command, shell=True)



# Create RoseTask Object
task = RoseTask()

# When rose is executed without any arguments...
if(len(sys.argv) == 1):
    print("Please use syntax as 'rose [command] [options]'\n")

# When rose is executed with atleast an argument...
if(len(sys.argv) > 1):
    task.cmdTask(sys.argv[1])








# toaster = ToastNotifier()
# toaster.show_toast("Hello World!!!",
#                    "Python is 10 seconds awsm!",
#                    icon_path="custom.ico",
#                    duration=10)
#
# toaster.show_toast("Example two",
#                    "This notification is in it's own thread!",
#                    icon_path=None,
#                    duration=5,
#                    threaded=True)
# # Wait for threaded notification to finish
# while toaster.notification_active(): sleep(0.1)
