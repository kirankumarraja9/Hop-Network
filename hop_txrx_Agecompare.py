###########################################################################################
#                           HOP Network Transmission using Scheduling
###########################################################################################
#In this code, the HOP receives messages from both the transmitters and sends the messages to the transmitter, whose Age of Information of the last sent message is larger than the other transmitter.
#it mean  if the Age of Information of the last message received by the Transmitter 1 is larger than the Transmitter 2 then the message is transmitted to Transmitter1.
#similarly each and every message's AoI is calculated and messages are transmitted to the respective transmitter based on their Ages.
# #The Code can modified to create FIFO( First In and First Out) and LIFO( Last In First Out)
###########################################################################################
#                           Initialising libraries and Variables
###########################################################################################

import socket
import random
import time

Host ='192.168.4.1'#receiver address
Port=46936

tx=[]
rx1=[]#arrays with numbers
rx2=[]#arrays with numbers
RX1=[]#messages to Receiver1
RX2=[] #messages to Receiver2

#nmsgs=100


#################################################################################
#                        RECEPTION OF MESSAGES
################################################################################
#for i in range(nmsgs):
while True: # enters the loop continously
      with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:#socket command for UDP
            s.bind((Host,Port))# bind the HOP to the Host
            msg,addr =s.recvfrom(1024)# receive message from the Host
            #if msg!=bytes(4):
            print('message received')
            print(msg)
            tx.append(msg) #append all the messages received from Transmitter
            a=tx[len(tx)-1]# last received message
            #else:
                  #break
#if loop for bifurcating the messages and addresses
#if loop for receiver 1

            if a[0:12]==bytes(('192.168.4.10'),'utf-8'): # checking the address of the receiver and entering into loop
                if len(msg)==31:# if the length of the message is 31
                      msg1=int(msg[17:len(msg)-1])#seperating the time interval from the message
                      RX1.append(msg)# making the list of the total message received
                      rx1.append(msg1) # append messages of the receiver1
                elif len(msg)==32:# if the length of the message is 32
                      msg1=int(msg[18:len(msg)-1])#seperating the time interval from the message
                      RX1.append(msg)# making the list of the total message received
                      rx1.append(msg1)#append messages of the receiver1
                elif len(msg)==4:# if the length of the message is 4
                      RX1.append(msg)# making the list of the total message received
                      rx1.append(msg)#append messages of the receiver1
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
                  elif len(msg)==32:# if the length of the message is 32
                      msg2=int(msg[18:len(msg)-1])#seperating the time interval from the message
                      RX2.append(msg)# making the list of the total message received
                      rx2.append(msg2)#append messages of the receiver2

                  #print('Message Transmitted to receiver')
      
                  #s.sendto(msg,('192.168.4.13',65321))#send data to the receiver
#loop for transmitting the messages based on the age of each message received at the HOP 
            if msg !=bytes(4):
                  if rx2==[] or rx1==[]:# if receiver 1 or receiver 2 is zero, enters the loop
                        if rx2==[]: # if receiver 2 is zero that mean  transmitter 2 is not transmitting
                              s.sendto(msg,('192.168.4.10',65432))#send data to the receiver 1
                              print('Message transmitted to receiver-1')

                        if rx1==[]: # if receiver 1 is zero that mean that transmitter 1 is not transmitting
                              s.sendto(msg,('192.168.4.13',65321))#send data to the receiver 2
                              print('Message transmitted to receiver-2')
                  #enters the loop if both the transmitters are transmitting
                  else:
                        if rx2[len(rx2)-1]-rx1[len(rx1)-1]>=0:# if age of Receiver 2 is greater than Receiver 1 then transmit receiver 2 message 
                              #s.sendto(RX1[len(rx1)-1],('192.168.4.10',65432))#send data to the receiver 1
                              s.sendto(RX2[len(rx2)-1],('192.168.4.13',65321))#send data to the receiver 2
                              print('Message transmitted to receiver 2')
                        elif rx1[len(rx1)-1]-rx2[len(rx2)-1]>0:# if age of Receiver 1 is greater than Receiver 2 then transmit receiver 1 message
                              #s.sendto(RX2[len(rx2)-1],('192.168.4.13',65321))#send data to the receiver 2
                              s.sendto(RX1[len(rx1)-1],('192.168.4.10',65432))#send data to the receiver 1
                              print('Message transmitted to receiver 1')

            else:
                  s.sendto(msg,('192.168.4.10',65432))#send data to the receiver 1
                  print('Message transmitted to receiver-1')
            #if RX1[len(rx1)-1]==bytes(4):
                  break# to break the while loop
