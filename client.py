###  HOW TO USE  ###
# Please read readme.txt file.

# 1. open a command prompt and run server.py
# 2. open ANOTHER command prompt and run client.py
# 3. If an error occurs, try to change the port number to a 4 digit natural number.

# Client sends a query message to the server containing an email address.

import socket

#the socket initialized here is reciving the data as bytes and sending the data as bytes.
#So, I added a encoding and decoding function to literally encode and encode the data.  
#utf-8 = (8-bit Unicode Transformation Format
run = True
email_list = ["youngho.kim@gmail.com", "yeringvely@gmail.com", "jihoon.ryoo@gmail.com", "dongyeob.Lee@gmail.com", "whasuck.lee@gmail.com"] 
while run == True:
    print("Write down ONE email address from the following list,", "\n", email_list)
    email = input()
    if email not in email_list:
        print("================================================")
        print("The email is not in the server. Please try again.")
        print()
        run = True
    else:
        run = False
TYPE = "Q" #Querry 
question = [email, str(len(email)), TYPE] #question will be used to send each data to the server.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #INET corresponds to Ipv4, and SOCK_STREAM corresponds to TCP.
#rather than binding, client needs to be connected.
s.connect((socket.gethostname(), 1234)) #change the server to your IP address.

data_receieved = []

for item in question:
    input("Press Enter to send each data [total 4 times].")
    s.send(bytes(item, 'utf-8')) #sending order: type, Length, Email
    data = s.recv(255).decode() #receive data from server, and decode utf-8 to string.
    data_receieved.append(data) #All data received from the server is sotred to a list.
if not data_receieved:
    print("Fail to get answer from the server")

print("Client Received ==> Type:", data_receieved[0], ", Length:", data_receieved[1], ", Packet:", data_receieved[2])
#client received --> Type: R , Length: 11, Packet = Youngho Kim

