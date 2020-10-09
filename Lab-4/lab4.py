import urllib
import requests
import threading
import json

import random

# Lab 4 Programming Task

# Modified From Lab 2 Part 3


# Define a function that will post on server every 15 Seconds

def thingspeak_post():
    projectGroup = "L1-F-2";
    memberIdentifier = "b";
    cmailAddress = "jackharold@cmail.carleton.ca";
    
    URl='https://api.thingspeak.com/update?api_key='
    KEY='7481QW0APO2BO2BU'
    HEADER='&field1={}&field2={}&field3={}'.format(projectGroup, memberIdentifier, cmailAddress)
    NEW_URL=URl+KEY+HEADER
    print(NEW_URL)
    data=urllib.request.urlopen(NEW_URL)
    print(data)


if __name__ == '__main__': 
   thingspeak_post()
 

