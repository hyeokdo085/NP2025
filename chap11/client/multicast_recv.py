# multicast_recv.py
from socket import *
import struct

BUFFER = 1024
group_addr = "224.0.0.255"
r_sock = socket(AF_INET, SOCK_DGRAM)
r_sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1) #주소 재사용 설정
r_sock.bind(("", 5005)) #모든 인터페이스, 포트5005 바인드

# 멀티캐스트 그룹 주소
mreq = struct.pack("4sl", inet_aton(group_addr), INADDR_ANY) 
# 멀티캐스트 그룹 가입
r_sock.setsockopt(IPPROTO_IP, IP_ADD_MEMBERSHIP, mreq)
print("멀티캐스트 수신기 시작")

while True:
    rmsg, addr = r_sock.recvfrom(BUFFER)
    print(f"{addr}로부터 수신 메세지: {rmsg.decode()}")
    r_sock.sendto('ACK'.encode(), addr) #응답 전송
r_sock.close()