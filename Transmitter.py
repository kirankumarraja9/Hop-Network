'''
this code is for transmitter of a Hop Network. Here the Transmitter transmits the message
to the Hop from there it is transmitted to the designated receiver
The transmitted messages should contain
1. address of the message
2. unique message ID
3.Time of the message generation
the result is shown in the below line
b"192.168.46.1 J b'1664874529786'"
'''

import socket
import time
import random
import string
from string import ascii_uppercase 
import numpy as np
import itertools
import threading
from matplotlib import pyplot as plt
from datetime import datetime
##############################################################################
############################### Variables ####################################
##############################################################################

Host ='192.168.4.1' #IP address of the receiver
Port=46936
Transmit_time=[]
nmsgs=50
s1=[]

##############################################################################
# loop for creating more variables like A,B,..AA,AB...

#loop for creating a string of universal nature like in excel
def msg_index(num):
    for size in range(num):
        #print(size)
        for s in itertools.product(ascii_uppercase, repeat=size):
            yield "".join(s)
            
for s in msg_index(3):
    s1.append(s)
    if s=='BBB': #break the generation of variables after s=BBB
        break


for i in range(nmsgs):
    now=time.time()
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        dt=bytes(str(int(round(now*1000))),'utf-8')#converting datetime to bytes
        recv_addr='192.168.4.10'
        msg_id=s1[i+1]
        msg=bytes(str(recv_addr)+str(' ')+str(msg_id)+str(' ' )+str(dt),'utf-8')  # this line will create the format b"192.168.4.1 A b'1664874389689'"
        #s.sendto(msg,(Host,Port))
        #print(msg)

        if i>=nmsgs: #for last msg
            msg=bytes(4)
            s.sendto(msg,(Host,Port))
            print(msg)

        else:
            s.sendto(msg,(Host,Port))
            print(msg)
        #time.sleep(random.randint(3,5))#sleep time 100 milliseconds or 0.1 seconds
        time.sleep(8)
        
