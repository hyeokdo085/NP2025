# UDP_client.py
import socket
BUFFSIZE = 1024
port = 2500

# UDP 소켓 생성
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    msg = input("보낼 메세지: ")
    sock.sendto(msg.encode(), ('172.18.106.250', port)) #메세지 송신
    data, addr = sock.recvfrom(BUFFSIZE) #메시지 수신
    print(f"수신 메세지: {data.decode()}")
sock.close()