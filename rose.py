# ROSE CLI - CMD utility to display notification on task completion

# Running Rose:
# rose [command] [parameters]

# Standard libraries
import sys
import urllib.request
import pandas as pd
import logging
import threading
from os import path
from time import sleep
import subprocess

# Third party libraries
from win10toast import ToastNotifier

class RoseTask:

    def __init__(self):
        print("Thank you for using ROSE CLI. To view a list of available commands, type 'rose help'")

        # Constants
        self.ROSE_VERSION = '0.0.1'

    # function that displays the application version
    def version(self):
        print("Current rose version : ", self.ROSE_VERSION)

    # function to execute the CMD task
    def cmdTask(self, command, arguments=None):
        toaster = ToastNotifier()
        toaster.show_toast("Command execution started",
                           "Command: " + command + " Arguments: " + str(arguments),
                           icon_path=None,
                           duration=5)
        # Running the command received as parameter
        subprocess.call(command, shell=True)
        toaster.show_toast("Command execution over",
                           "Command: " + command + " Arguments: " + str(arguments) + " has exited",
                           icon_path=None,
                           duration=5,
                           threaded=True)

        # Wait for threaded notification to finish
        while toaster.notification_active(): sleep(0.1)




    def URLTask(self, argument=None):
        if argument == None:
            print("Please provide a valid URL")
            return
        toaster = ToastNotifier()
        toaster.show_toast("Command execution started",
                           "Command type:  Content Download  URL: " + argument,
                           icon_path=None,
                           duration=5)
        try:
            print("Use 1 or 2 to highlight choice :")
            download_type = int(input(" ? Download as 1. CSV or 2. Raw : "))
            filename = input("Enter a file name to save the response: ")

            with open('Downloads/'+filename, 'w+') as file:
                if download_type == 1:
                    data = pd.read_csv(argument)
                    df = data.applymap(str)
                    file.write(str(df))
                if download_type == 2:
                    data = urllib.request.urlopen(argument)
                    file.write(str(data.read()))
                else:
                    print(" ! Please choose a download type")

        except Exception as e:
            print(str(e))


    def help(self):
        print("\nROSE CLI Help:")
        print("Syntax: rose [command] [options]\n")
        print("List of all available commands:")
        print("--------------------------------")
        print("url - Usage : rose url [some url] Details : Downloads url content to a file and notifies when task completes")
        print("run - Usage : rose run [command] Details : Runs Windows commands and notifies on completion")



# Create RoseTask Object
task = RoseTask()

# When rose is executed without any arguments...
if(len(sys.argv) == 1):
    print("Please use syntax as 'rose [command] [options]'\n")

# When rose is executed with atleast an argument...
if(len(sys.argv) > 1):
    # Download a file (probably, a CSV for data science project !)
    if(sys.argv[1] == "url"):
        task.URLTask(sys.argv[2])


    # Displays the generic help message
    if(sys.argv[1] == "help"):
        task.help()

    if(sys.argv[1] == "run"):
        task.cmdTask(sys.argv[2])









# toaster = ToastNotifier()
# toaster.show_toast("Hello World!!!",
#                    "Python is 10 seconds awsm!",
#                    icon_path="assets/icon.png",
#                    duration=10)
#
