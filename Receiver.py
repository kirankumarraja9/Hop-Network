"""
This code is used as a receiver, which receives the data from the HOP and plots the AoI of each message and 
returns the number of messages received by the receiver from the HOP
"""

import socket
import random
import numpy as np
import time
from matplotlib import pyplot as plt
from goto import goto, label
from datetime import datetime

Host = '192.168.4.10' # IP address of Server (Local Host)
Port = 65432 # Port number of the Server

#Port to listen on - it can be any number between 1 and 65535 but in TCP better
tx = []
rx = []
age=[]
m =0
n=0
tsec = []
tmicro = []
i = 0
#nmsgs=80
msg_append=[]
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:# Socket command for the UDP
    s.bind((Host,Port))# bind to the host
    #for i in range(nmsgs):
    while True: # maximum no. of msgs should be received
        msg, addr = s.recvfrom(1024)# receive messages from the Host
        msg_append.append(msg)# add to the list messages
        if msg != bytes(4):# if msg not bytes(4)
            print('Received from:', addr)#address of the host
            #dt_string=bytes(now.strftime("%Y%m%d%H%M%S"),'utf-8')
            #print(int(now))
            print(msg)#message received
            if len(msg)>=31:#if length of the msg received is greater than 31
                #The below loop is executed if the message received is not the same received previous
                if msg !=msg_append[len(msg_append)-2]:
                    t=int(len(msg)/2)# dividing the length of the messages into half
                    tx.append(int(msg[t+2:len(msg)-1]))# make a list of the message generated time
                    now=bytes(str(int(round((time.time())*1000))),'utf-8')# calculating the received time now.
                    #in the above command we multiply the time.time(), which gives time in milliseconds
                    print(now)
                    rx.append(int(now))
                    age.append(rx[i] -tx[i])
                    i = i+1
                '''
            elif len(msg)==32:
                tx.append(int(msg[17:len(msg)-1]))
                now=bytes(str(int(round((time.time())*1000))),'utf-8')
                print(now)
                rx.append(int(now))
                age.append(rx[i] -tx[i])
                i = i+1
                '''
            #NOW = bytes(str(int(round((time.time())*1000))),'utf-8')
            #s.sendto(NOW, addr)
            #print(NOW)
            #time.sleep(random.randint(1,10))
        else:
            break
            #time.sleep(random.randint(1,10))
        #break

nmsgs = len(rx)        
j = rx[0]
for t in range(rx[0], rx[(nmsgs-1)]):
    tmicro.append(j)
    j = j+1
    tsec.append(m)
    m = m+1

b = np.zeros(len(tsec))
for k in range(0,(nmsgs-1)):
    a = tmicro.index(rx[k])
    b[a] = age[k]
    for l in range(len(tsec)):
        if a+l < len(tsec):
            b[a+l]= age[k]+l

#time.sleep(random.randint(1,10))
#print((np.trapz(b,tsec)))
plt.plot(tsec,b)
plt.xlabel('Time(milliseconds)')
plt.ylabel('Age of Information')
plt.title('AoI of Reciever')
plt.show()
print((np.trapz(b,tsec)))
print((np.trapz(b,tsec))/len(tsec))
res=[i for n, i in enumerate(rx) if i not in rx[:n]]# this command is used to remove the repeatation 
print(len(res))#total recceived messages without repetation
