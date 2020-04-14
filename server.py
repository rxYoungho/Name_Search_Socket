import socket

server = socket.gethostname() # if you want to set your computer to be a server, just use this gethostname function. It will directly refer to your Ipv4 address
port = 1234 #Put any port number. eg) 4 digit number -> 1111 , 9999, 1234 , and etc

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #INET means IPV4 protocols (TCP), and SOCK_STREAM means to read or open existing file.

try:
    s.bind((server, port)) #socket.bind() function will get one argument that is a tuple type. -> address = (server, port) 
except socket.error as e: #catch any exceptions
    str(e) 
    
s.listen(5) #listen gets one argument as an integer that indicates the number of pending connections the system should queue.

#Try to connect more clients. It will work fine.

print("Waiting for a connection, Server Started") 

while True: 
    #Accept of connections
    conn, addr = s.accept()
    print("[NEW CONNECTION]",addr, "is connected")
    #Receive data from the client
    
    TYPE = 'R' #Response TYPE
    FULLNAME = ['Youngho Kim', 'Yeri Lee', 'Jihoon Ryoo', 'Dongyeob Lee', 'Whasuck Lee'] #data sturcture

    data_received = []
    error_msg = "Email not found."
    for i in range(3):
        data = conn.recv(255).decode() # since Type = 1byte, Length = 1byte, and Question/Response < 255byte, we can set the capacity as 255(MAX)
        
        if not data: #If no data is received, quit.
            break
        # if data_received[2] == "youngho.kim@gmail.com":
            #data_received.append(data) #store data received from the client
        data_received.append(data) #store data received from the client
        # print(data_received)
        if "youngho.kim@gmail.com" in data_received:
            if i == 0 : conn.send(bytes(TYPE, 'utf-8')) #if i == 0 is same as if the data received from the client is TYPE.
            if i == 1 : conn.send(bytes(str(len(FULLNAME[0])), 'utf-8')) #if i == 1 is same as if the data received from the client is LENGTH OF EMAIL.
            if i == 2 : conn.send(bytes(FULLNAME[0], 'utf-8')) #if i == 2 is same as if the data received from the client is EMAIL.
        elif "yeringvely@gmail.com" in data_received:
            #data_received.append(data) #store data received from the client
            if i == 0 : conn.send(bytes(TYPE, 'utf-8')) #if i == 0 is same as if the data received from the client is TYPE.
            if i == 1 : conn.send(bytes(str(len(FULLNAME[1])), 'utf-8')) #if i == 1 is same as if the data received from the client is LENGTH OF EMAIL.
            if i == 2 : conn.send(bytes(FULLNAME[1], 'utf-8')) #if i == 2 is same as if the data received from the client is EMAIL.
        elif "jihoon.ryoo@gmail.com" in data_received:
            #data_received.append(data) #store data received from the client
            if i == 0 : conn.send(bytes(TYPE, 'utf-8')) #if i == 0 is same as if the data received from the client is TYPE.
            if i == 1 : conn.send(bytes(str(len(FULLNAME[2])), 'utf-8')) #if i == 1 is same as if the data received from the client is LENGTH OF EMAIL.
            if i == 2 : conn.send(bytes(FULLNAME[2], 'utf-8')) #if i == 2 is same as if the data received from the client is EMAIL.
        elif "dongyeob.Lee@gmail.com" in data_received:
            #data_received.append(data) #store data received from the client
            if i == 0 : conn.send(bytes(TYPE, 'utf-8')) #if i == 0 is same as if the data received from the client is TYPE.
            if i == 1 : conn.send(bytes(str(len(FULLNAME[3])), 'utf-8')) #if i == 1 is same as if the data received from the client is LENGTH OF EMAIL.
            if i == 2 : conn.send(bytes(FULLNAME[3], 'utf-8')) #if i == 2 is same as if the data received from the client is EMAIL.
        elif "whasuck.lee@gmail.com" in data_received:
            #data_received.append(data) #store data received from the client
            if i == 0 : conn.send(bytes(TYPE, 'utf-8')) #if i == 0 is same as if the data received from the client is TYPE.
            if i == 1 : conn.send(bytes(str(len(FULLNAME[4])), 'utf-8')) #if i == 1 is same as if the data received from the client is LENGTH OF EMAIL.
            if i == 2 : conn.send(bytes(FULLNAME[4], 'utf-8')) #if i == 2 is same as if the data received from the client is EMAIL.
        else:
            pass
        print("Server Received: ",data) #for each data, server tells what he got from the client
        
        #If all data is well received, the server will finally print the total data it got from the client.
    print("Server Received ==> Type:", data_received[2] , ", Length:", data_received[1], ", Packet:", data_received[0])
    # data_received[0] = Query type
    # data_received[1] = Length of the Email
    # data_received[2] = Email Address
conn.close()
#close the server when finished