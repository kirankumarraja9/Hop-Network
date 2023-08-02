Created By P. Kiran Kumar Raja on 30 December 2022.

This file contains instructions on how to set up your HOP Network and execute the files:

Configuring Your HOP Network
==================================
To create your HOP Network, You need to use a Private WiFi Network to connect all the Raspberry Pis to the network and configure one Raspberry Pi board as a HOP and two boards as Transmitters and two boards as Receivers 
 

------------- Creating a Private Network -----------

To create a private network using Raspberry Pi 
we need to open the terminal in Raspberry Pi and follow the commands below
	sudo apt update
	sudo apt upgrade
	sudo apt install hostapd
	sudo systemctl unmask hostapd
	sudo systemctl enable hostapd
	sudo apt install dnsmasq
	sudo DEBIAN_FRONTEND=noninteractive apt install -y netfilter-persistent iptables-persistent 
	sudo nano /etc/dhcpcd.conf 

		interface wlan0 

		static ip_address=192.168.4.1/24 

		nohook wpa_supplicant 

	sudo nano /etc/sysctl.d/routed-ap.conf 

		net.ipv4.ip_forward=1 

	sudo iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE 
	sudo netfilter-persistent save
	sudo mv /etc/dnsmasq.conf /etc/dnsmasq.conf.old 
	sudo nano /etc/dnsmasq.conf 
		interface=wlan0 
		dhcp-range=192.168.4.2,192.168.4.20,255.255.255.0,24h 
		domain=wlan 
	sudo rfkill unblock wlan 
	sudo nano /etc/hostapd/hostapd.conf 
	#Access point with password (WPA2): 
		country_code=GB 
		interface=wlan0 
		ssid=YourNetworkName 
		hw_mode=g 
		channel=7 
		macaddr_acl=0 
		auth_algs=1 
		ignore_broadcast_ssid=0 
		wpa=2 
		wpa_passphrase=YourPassword 
		wpa_key_mgmt=WPA-PSK 
		wpa_pairwise=TKIP 
		rsn_pairwise=CCMP 

After the above commands 
check your country code: localectl status
if you want your access point to be open( no password):
	interface=wlan0
	driver=nl80211
	ssid=YourNetworkName
	hw_mode=g
	channel=6
	sudo reboot
By the above commands, your raspberry pi will not be able to use a WiFi antenna for other WiFi but it will be 
using the same antenna as a Hotspot. so that other devices can connect to it
To enable internet access to the board, you can use the Ethernet port.

This board acts as a HOP and all the Raspberry Pi's, transmitters, and receivers are connected to the Hotspot of the Hop.



------------- Transmitter.py ----------------
The transmitter.py file contains the Python code used for the transmission of messages from the transmitter to the HOP.
To run the file, Open the file using a Python IDE and run the file in the environment. You can also run the file in Command Prompt
The code works both in Python 2.0 and Python 3.0
The same code is to be executed at both transmitters. 
Each code has a delay command which helps to change the transmission times between the messages. 

------------- Receiver.py -------------------

Receiver.py file contains the Python code used for the Reception of messages from the HOP which was sent to it from the Transmitter.
To run the file, Open the file using a Python IDE and run the file in the environment.  You can also run the file in Command Prompt
The code works both in Python 2.0 and Python 3.0
The same code is to be executed at both Receivers.

------------- HOP_threading.py -------------
HOP_threading.py is the Python code of the HOP. The HOP receives messages from the transmitter and sends the messages to the Receiver. 
To run the file, Open the file using a  Python IDE and run the file in the environment.  You can also run the file in Command Prompt
The code works both in Python 2.0 and Python 3.0
In this code, a concept of threading was taken from other software programming solutions used in real-time applications in programming languages like Java and Python.
In the concept of threading two operations are executed simultaneously without any delay. In many communication applications, the device can only transmit after it has received data.
But this creates a delay in the communication network as the message received from the transmitter has to be analyzed by the Transceiver and then sent to the Receiver. This creates a delay
so to overcome the delay we are using the concept of threading to Transmit and Receive the messages simultaneously at the Transceiver(HOP). 

------------- HOP_TXRX_Scheduling.py---------------------------
HOP_TXRX_Scheduling.py is the Python code of the HOP. The HOP receives messages from the transmitter and sends the messages to the Receiver. 
To run the file, Open the file using a  Python IDE and run the file in the environment.  You can also run the file in Command Prompt
The code works both in Python 2.0 and Python 3.0
In this code, the HOP is scheduled to transmit messages from Transmitter1 to Receiver 1 for some time interval and transmit messages from Transmitter2 to Receiver2 for another time interval. 
in this code, we can modify the length of the time interval for each transmitter and also keep equal time intervals to each transmitter.

------------- HOP_txrx_Agecompare.py---------------------------
HOP_txrx_Agecompare.py is the Python code of the HOP. The HOP receives messages from the transmitter and sends the messages to the Receiver. 
To run the file, Open the file using a  Python IDE and run the file in the environment.  You can also run the file in Command Prompt
The code works both in Python 2.0 and Python 3.0
In this code, the HOP receives messages from both the transmitters and sends the messages to the transmitter, whose Age of Information of the last sent message is larger than the other transmitter.
it means that if the Age of Information of the last message received by Transmitter 1 is larger than Transmitter 2 then the message is transmitted to Transmitter1. 
similarly, each and every message's AoI is calculated and messages are transmitted to the respective transmitter based on their Ages. 
The Code can be modified to create FIFO( First In and First Out) and LIFO( Last In First Out)

------------ Execution---------------------------
Initially open the Python codes in 3 or 5 Raspberry Pi. with 1 or 2 Transmitters and 1 or 2 Receivers and 1 HOP

Execute the Receiver.py code at the first instant so that no loss of information takes place at the receiver.
Secondly, execute the HOP_TXRX_Scheduling.py at the HOP Raspberry Pi. 
Thirdly execute the Transmitter.py at the Transmitter and this helps in the transmission of the messages from the transmitter to the receiver without loss.

--------------Graphical Representation--------------
The same code is  executed with different conditions like when the HOP transmission time is varying with the Transmitter transmission time which can done by changing the delay value in the HOP_TXRX_SCHEDULING.py and
Transmitter.py. The delay value of 1000 is equal to 1000 milliseconds which is 1 second.
After the execution of the code. In the Python console, the number of messages received is displayed at the receiver. along with an Age of Information plot of the messages. 
By taking note of the number of messages received at different instances like changes in the number of messages transmitted from the receiver and different transmission delays.
The probability of reception is calculated by dividing the number of messages by that of the number of messages transmitted from the Transmitter.
The average of the probabilities in each case is taken and the graph is plotted in Matlab with the x-axis mapped to the number of messages and the y-axis mapped to the Probabilities of reception.   



