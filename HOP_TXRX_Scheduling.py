###########################################################################################
#                           HOP Network Transmission using Scheduling
###########################################################################################
# In this code, the HOP is scheduled to transmit messages from Transmitter1 to Receiver 1 for some time interval and transmit messages from Transmitter2 to Receiver2 for another time interval.
# In this code, we can modify the length of the time interval for each transmitter and also keep equal time intervals to each transmitter.
# we divide the time interval between Transmitter1 and Transmitter 2


###########################################################################################
#                           Initialising libraries and Variables
###########################################################################################
import socket
import random
import time

Host ='192.168.4.1'#receiver address
Port=46936

tx=[]
transmit1=[]
transmit2=[]
rx1=[]#arrays with numbers
rx2=[]#arrays with numbers
RX1=[]#messages to Receiver1
RX2=[] #messages to Receiver2
b=0 #no of epochs
nmsgs=100
T0=time.time() #starting of the time T0
T1=T0
#T2=T0+1000
Ti=5
#print(T1)
#for i in range(nmsgs):
#while True:
 
##########################################################################################
#                        FUNCTIONS
##########################################################################################

# the below function 'Receive' is used to seperate the messages to the designated receivers based on the address of the receiver 
def Receive():
   if a[0:12]==bytes(('192.168.4.10'),'utf-8'): # checking the address of the receiver and entering into loop
                if len(msg)==31:# if the length of the message is 31
                    msg1=int(msg[17:len(msg)-1])#seperating the time interval from the message
                    RX1.append(msg)# making the list of the total message received
                    rx1.append(msg1) # append messages of the receiver1
                    #print('loop1')
                elif len(msg)==32:# if the length of the message is 32
                    msg1=int(msg[18:len(msg)-1])#seperating the time interval from the message
                    RX1.append(msg)# making the list of the total message received
                    rx1.append(msg1)#append messages of the receiver1
                    #print('loop2')
                elif len(msg)==4:# if the length of the message is 4
                    RX1.append(msg)# making the list of the total message received
                    rx1.append(msg)
     # loop for  checking the youngest to transmit to rx1
                    #print(' this message was from transmitter')
                    #addr1=addr
                    #s.sendto(msg,('192.168.4.10',65432))#send data to the receiver 1
    #if loop for receiver 2
                    
   if a[0:12]==bytes(('192.168.4.13'),'utf-8'):
                if len(msg)==31:# if the length of the message is 31
                    msg2=int(msg[17:len(msg)-1])#seperating the time interval from the message
                    RX2.append(msg)# making the list of the total message received
                    rx2.append(msg2) # append messages of the receiver2
                    #print('loop-1')
                elif len(msg)==32:# if the length of the message is 32
                    msg2=int(msg[18:len(msg)-1])#seperating the time interval from the message
                    RX2.append(msg)# making the list of the total message received
                    rx2.append(msg2)#append messages of the receiver2
                    #print('loop-2')

 
#the below function ' Transmit' is used to transmit the seperated messages to the receivers based on sechedule
def transmit():
                global msg  
               # the below loop is if only one of the transmitters is transmitting
                if rx2==[] or rx1==[]:# if receiver 1 or receiver 2 is zero, enters the loop
                    if rx2==[]:# if receiver 2 is zero that mean that transmitter 2 is not transmitting
                        s.sendto(msg,('192.168.4.10',65432))#send data to the receiver 1
                        #print('Message transmitted to receiver-1')
                        transmit1.append(msg)#adding the last sent messages to the list
                    if rx1==[]:# if receiver 1 is zero that mean that transmitter 1 is not transmitting
                        s.sendto(msg,('192.168.4.13',65321))#send data to the receiver 2
                        #print('Message transmitted to receiver-2')
                        transmit2.append(msg)#adding the last sent messages to the list
               # the below loop is executed if both the transmitters are transmitting
                else:
                    t0=int(time.time())# to is the time of this command
                    i=t0
                    while i<=t0+4:    # enters the loop when i is less than 4 seconds
                        #print('entered into loop 1')
                        msg,addr =s.recvfrom(1024)#receive message from Host
                        tx.append(msg) #append all the messages received from Transmitter
                        a=tx[len(tx)-1]# last received message
                        Receive()#calling the function Receive
                        if len(transmit1)>=1:#if number of the received message is more than 1
                            if transmit1[len(transmit1)-1] !=RX1[len(rx1)-1]:# this loop is to avoid repeatation at the receiver
                               s.sendto(RX1[len(rx1)-1],('192.168.4.10',65432)) # to send the last received message to the Receiver 1
                               print('Message transmitted to receiver 1')
                               transmit1.append(RX1[len(rx1)-1])#adding the last sent messages to the list
                        else: # enters the loop if the number of received message is zero
                            s.sendto(RX1[len(rx1)-1],('192.168.4.10',65432)) # to send the last received message to the Receiver 1
                            print('Message transmitted to receiver 1')
                            transmit1.append(RX1[len(rx1)-1])#adding the last sent messages to the list
                        i=time.time()# updating i after every loop
                        
                                                
                    j=time.time() #initialising j as time.
                    
                    while j<=t0+8: # enters the loop when t0 is less than 8 seconds and at the same time this loop will execute only if the loop before is executed.
                        #print('entered into loop 2')
                        msg,addr =s.recvfrom(1024)#receive message from the address
                        tx.append(msg) #append all the messages received from Transmitter
                        a=tx[len(tx)-1]# last received message
                        Receive()# calling the receive function
                        if len(transmit2)>=1:# if the length of the message is greater than 1
                            if transmit2[len(transmit2)-1] !=RX2[len(rx2)-1]:# this loop is to avoid repeatation at the receiver
                               s.sendto(RX2[len(rx2)-1],('192.168.4.13',65321))# send message to the receiver 2
                               print('Message transmitted to receiver 2')
                               transmit2.append(RX2[len(rx2)-1])#adding the last sent messages to the list
                        else:
                            s.sendto(RX2[len(rx2)-1],('192.168.4.13',65321))# send message to the receiver 2
                            print('Message transmitted to receiver 2')
                            transmit2.append(RX2[len(rx2)-1])#adding the last sent messages to the list
                        
                        j=time.time() #updating time at j


           


###############################################################################
#                               Main Code
###############################################################################


for b in range(1000):# indicates the number of epochs b is  
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.bind((Host,Port))# bind to the Host
            msg,addr =s.recvfrom(1024)# receive message from host
            if msg!=bytes(4):#if message is not equal to bytes(4)
                    
                print('message received')
                print(msg)
                Lmsg=len(msg)
                #print(len(msg))
                tx.append(msg) #append all the messages received from Transmitter
                a=tx[len(tx)-1]# last received message
                Receive()# calling the Receive function
                transmit()# calling the Transmit function
                
            elif msg==bytes(4):
               sendto(msg,('192.168.4.10',65432))#send data to the receiver 1
               print('Message transmitted to receiver-1')
               print(len(RX1))#total number of messages sent to Receiver 1
               print(len(RX2))#total number of messages sent to Receiver 2
               break
