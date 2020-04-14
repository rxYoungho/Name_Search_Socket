### Name_Search_Socket
Youngho Kim 
#110710626


**If port error or server error occurs, please change the port number to a 4-digit number.
**e.g) 4567, 5555, 9999, and etc


How to use:

1. Run socket_server.py file 
 -it will print out the following statement: "Waiting for a connection, Server Started"

2. Run socket_client.py file from another terminal!
 - it will print out the following statement:
 " Write down ONE email address from the following list, 
  ['youngho.kim@gmail.com', 'yeringvely@gmail.com', 'jihoon.ryoo@gmail.com', 'dongyeob.Lee@gmail.com', 'whasuck.lee@gmail.com']
 - After this statement is shown, please write down one email address from the list above.
 - Then the program will ask you to press Enter 4 times.

Example of client.py:
	Write down ONE email address from the following list, 
 	['youngho.kim@gmail.com', 'yeringvely@gmail.com', 'jihoon.ryoo@gmail.com', 'dongyeob.Lee@gmail.com', 'whasuck.lee@gmail.com']
>input:	jihoon.ryoo@gmail.com
	Press Enter to send each data [total 4 times].
	Press Enter to send each data [total 4 times].
	Press Enter to send each data [total 4 times].
	Client Received ==> Type: R , Length: 11 , Packet: Jihoon Ryoo

3. As you press Enter, the server will receive each data: [Type, Length of the packet, Packet]

Example of server.py:
	[NEW CONNECTION] ('10.12.49.24', 50522) is connected
	Server Received:  jihoon.ryoo@gmail.com
	Server Received:  21
	Server Received:  Q
	Server Received ==> Type: Q , Length: 21 , Packet: jihoon.ryoo@gmail.com

4. If you type an email address that is not in the data structure, it will tell you to re-write the email address.

