from socket import *
import time

serverName ='127.0.0.1'
serverPort = 12000

# # AF_INET = address family IPv4
# # create socket UDP -- SOCK_DGRAM
clientSocket = socket(AF_INET, SOCK_DGRAM)

# timeout 500ms (only 1 time out)
clientSocket.settimeout(0.5)


message = "Sending from client"

for ping in range(10):
    send_time = time.time()
    message = 'Ping sequence ' + str(ping +1)
    # # send the message
    clientSocket.sendto(message.encode(),(serverName, serverPort))

    try:
        # # get msg from server (if any), serverAddress cotains both IP & addy
        # # buffer size is recommended as it works for most.
        modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
        received_time = time.time()
        rtt = received_time - send_time
        print("Message received", modifiedMessage)
        print("RTT", rtt)
        print()
        
    except timeout:
        print("Request timed out")
        print()



# # close conenction
clientSocket.close()