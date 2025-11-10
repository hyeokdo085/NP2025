# broadcast_client.py
from socket import *

addr = ('172.18.106.250', 10000) #브로드캐스트 주소와 포트

# 브로드캐스트를 위한 소켓 설정
sock = socket(AF_INET, SOCK_DGRAM)
sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
sock.setsockopt(SOL_SOCKET, SO_BROADCAST, 1) #브로드캐스트 옵션 설정

while True:
    smsg = input("브로드캐스트 메세지: ")
    sock.sendto(smsg.encode(), addr) #브로드캐스트 메세지 송신
    data, addr = sock.recvfrom(1024) #메세지 수신
    print(f"수신 메세지: {data.decode()}")
sock.close()