# SuperFastPython.com
# example of extending the Thread class
from time import sleep
from threading import Thread
import json, boto3, pandas, io, urllib3
from datetime import datetime
from boto3.dynamodb.conditions import Key, Attr
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

 
# custom thread class
class CustomThread(Thread, nombre):


    # override the constructor
    def __init__(self, value):
        # execute the base constructor
        Thread.__init__(self)
        # store the value
        self.value = value

        print('This is coming from another thread')
    
    # override the run function
    def run(self):
        # block for a moment
        # display a message
        print('This is coming from another thread'+self.value)
 
# create the thread
thread = CustomThread("Pablo")
thread.start()
# wait for the thread to finish
thread = CustomThread("Pablo2")
thread.start()