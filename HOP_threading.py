##############################################################################
#                           HOP Threading
##############################################################################
# This code is written to transmit and receive simultaneously at the HOP
# In a regular Hop network, we can find some delay for the HOP to analyse and transmit
# in a regular hop network, we can find that as the loop execute sequentially
# there will be a delay which will add up to the Age of Information and increase the age of the messages and also loss of messages
# In this threading, the transmission and reception are done simultanoeusly thus there by saves time and loss of messages
#############################################################################
#                Initialising Libraries and Variables
##############################################################################
import socket
import random
import time
import threading

#
Host='192.168.4.1' #receiver address
Port= 46936

#
tx=[]
transmit1=[]# Array of the transmitter 1 values that are transmitted
transmit2=[]# Array of the transmitter 2 values that are transmitted
rx1=[] # Receiver 1 list with only message
rx2=[] # Receiver 2 list with only message
RX1=[] # Receiver 1 List
RX2=[] # Receiver 2 list
b=0
t1=0

###############################################################################
#                             FUNCTIONS    
###############################################################################
# the below Function 'Receive' is used to seperate the messages as per their destination.
def Receive():
    global msg
    #s.bind((Host,Port))
    #msg,addr=s.recvfrom(1024)
    tx.append(msg)
    a=tx[len(tx)-1]
    
    if a[0:12]==bytes(('192.168.4.10'),'utf-8'):
        if len(msg)==31: # if the length of the message is 31
            msg1=int(msg[17:len(msg)-1]) #seperating the time interval from the message
            RX1.append(msg)# making the list of the total message received
            rx1.append(msg1)# making the list of the time interval that was seperated from the message
            #print('added-1')
        elif len(msg)==32:# if the length of the message is 32
            msg1=int(msg[18:len(msg)-1]) # seperating the time interval from the message
            RX1.append(msg)# making the list of the total message received
            rx1.append(msg1)# making the list of the time interval that was seperated from the message

    if a[0:12]==bytes(('192.168.4.13'),'utf-8'):
        if len(msg)==31: # if the length of the message is 31
            msg2=int(msg[17:len(msg)-1])#seperating the time interval from the message
            RX2.append(msg)# making the list of the total message received
            rx2.append(msg2)# making the list of the time interval that was seperated from the message
            #print('added-2')

        elif len(msg)==32:# if the length of the message is 32
            msg2=int(msg[18:len(msg)-1])#seperating the time interval from the message
            RX2.append(msg)# making the list of the total message received
            rx2.append(msg2)# making the list of the time interval that was seperated from the message
            #print('loop-2')

        
# the below function ' transmit' is used to transmit the 
def transmit():
        global msg
        global t1
        # the below loop is if only one of the transmitters is transmitting
        if rx2==[] or rx1==[]:# if receiver 1 or receiver 2 is zero, enters the loop
            if rx2==[]: # if receiver 2 is zero that mean that transmitter 2 is not transmitting
               s.sendto(msg,('192.168.4.10',65432))#send data to the receiver 1
               #print('Message transmitted to receiver-1')
               transmit1.append(msg)#list of the messages transmitted from transmitter1
               #print('transmitted-1')
            if rx1==[]:# if receiver 1 is zero that mean that transmitter 1 is not transmitting
               s.sendto(msg,('192.168.4.13',65321))#send data to the receiver 2
               #print('Message transmitted to receiver-2')
               transmit2.append(msg)#list of the messages transmitted from transmitter2
               #print('transmitted-2')
        # the below loop is executed if both the transmitters are transmitting
        else:
            
          if rx1[len(rx1)-1]<=rx2[len(rx2)-1]: #enters the loop if rx1 time is less than rx2 time 
                     #print(i)
                     #print('entered into loop 1')
                     #msg,addr =s.recvfrom(1024)
                     #tx.append(msg) #append all the messages received from Transmitter
                     #a=tx[len(tx)-1]# last received message
                     if len(transmit1)>=1:#this is to enter if already 1st msg is sent, This message is to avoid repeatation
                          #print('loop1')
                          if  RX1[len(rx1)-1] != transmit1[len(transmit1)-1]:# this loop is to avoid repeatation at the receiver
                             s.sendto(RX1[len(rx1)-1],('192.168.4.10',65432)) # to send the last received message to the Receiver 1
                             #print('Message transmitted to receiver-1')
                             transmit1.append(RX1[len(rx1)-1]) # to add the last received message to the transmit 1
                             t1=t1+1 
                     elif len(transmit1)==0:# this is for first msg
                        s.sendto(RX1[len(rx1)-1],('192.168.4.10',65432)) # to send the last received message to the Receiver 1
                        #print('Message transmitted to receiver 1')
                        transmit1.append(RX1[len(rx1)-1])
                        
                        
          elif rx1[len(rx1)-1]>rx2[len(rx2)-1]:# enters the loop if the rx1 time is greater than rx2 time                                      
                #print(j)
                #print('entered into loop 2')
                #msg,addr =s.recvfrom(1024)
                #tx.append(msg) #append all the messages received from Transmitter
                #a=tx[len(tx)-1]# last received message
                if len(transmit2)>=1:#this is to enter if already 1st msg is sent, This message is to avoid repeatation
                    #print('loop-2')
                     if RX2[len(rx2)-1] != transmit2[len(transmit2)-1]:# this loop is to avoid repeatation at the receiver
                        s.sendto(RX2[len(rx2)-1],('192.168.4.13',65321))# to send the last received message to the Receiver 2
                        #print('Message transmitted to receiver-2')
                        transmit2.append(RX2[len(rx2)-1])# to add the last received message to the transmit 2
                elif len(transmit2)==0:
                    s.sendto(RX2[len(rx2)-1],('192.168.4.13',65321)) # to send the last received message to the Receiver 2
                    #print('Message transmitted to receiver 2')
                    transmit2.append(RX2[len(rx2)-1])# to add the last received message to the transmit 2
                        
                #j=time.time()
          #else:
            #return 0


                    
###############################################################################
#                               Main Code
###############################################################################

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s: #socket command for UDP
    s.bind((Host,Port)) # this command is compulsory as this will bind the Board to the host and receive messages from the Host
    while True: # enters the loop continously
        
        msg,addr=s.recvfrom(1024) # to receive message from the Host and takes message and address
        print(msg) # print the received message
        Receive_thread =threading.Thread(target=Receive)# threading to receive
        transmit_thread= threading.Thread(target=transmit)# threading to transmit
        Receive_thread.start()# starting the receive thread
        transmit_thread.start()# Starting the transmit thread
        if msg==bytes(4): # if the message is bytes(4) then enters the loop
           #socket.socket(socket.AF_INET, socket.SOCk_DGRAM) as s
            s.sendto(msg,('192.168.4.10',65432))# send the message to the Receiver 1
            print('Message transmitted to Receiver 1')# Print statement
            print(len(RX1))# print length of the Received array 1
            print(len(RX2))# print length of the Received array 2
            #python code for making a list of transmitted messages without repeat
            res1=[i1 for n1, i1 in enumerate(transmit1) if i1 not in transmit1[:n1]] # to remove the repeated messages from transmit1
            res2=[i2 for n2, i2 in enumerate(transmit2) if i2 not in transmit2[:n2]] # to remove the repeated messages from transmit2
            print(len(res1))# print of the length of transmitted messages from transmitter 1
            print(len(res2)) # print of the length of transmitted messages from  transmitter 2
            break# break the while loop
            
        
