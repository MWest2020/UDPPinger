# # 10 pings to server
# # 1 send ping msg using UDP
# #  print res msg (if any)
# #  calculate RTT in sec, if server responds
# # else print("Timeout")
# from socket import *
# serverName ='hostname'
# serverPort = 12000

# # AF_INET = address family IPv4
# # create socket
# clientSocket = socket(AF_INET, SOCK_DGRAM)

# # loop 10 x
# i = 1

# # message 
# # : Ping sequence_number time
# message = 'Ping sequence_number time'

# # while i < 10:
# #     message = '' 
# # send the message
# clientSocket.sendto(message.encode(),(serverName, serverPort))

# # get msg from server (if any), serverAddress cotains both IP & addy
# # buffer size is recommended as it works for most.
# modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

# # if server responds, prit the msg, else print Req timed out
# if modifiedMessage == True: 
#     # print the response msg
#     print(modifiedMessage.decode)
# else: print('Request timed out') 

# # close conenction
# # clientSocket.close()

from socket import *
serverName = 'hostname'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = input('Input lowercase sentence:')
clientSocket.sendto(message.encode(),(serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage.decode())
clientSocket.close()