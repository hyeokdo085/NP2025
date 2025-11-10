# 가상머신에서 실행
# multicast_send.py
from socket import *
import struct
group_addr = ("224.0.0.255", 5005) #멀티캐스트 그룹 주소와 포트
s_sock = socket(AF_INET, SOCK_DGRAM) #UDP 소켓 생성
s_sock.settimeout(0.5) #타임아웃 설정
TTL = struct.pack('@i', 2) #TTL=2, 4바이트 정수형

s_sock.setsockopt(IPPROTO_IP, IP_MULTICAST_TTL, TTL) #TTL 설정
s_sock.setsockopt(IPPROTO_IP, IP_MULTICAST_LOOP, True) #루프백 비활성화
print("멀티캐스트 전송 시작")

while True:
    msg = input("전송 메세지 입력 ")
    s_sock.sendto(msg.encode(), group_addr) #메세지 전송

    while True:
        try:
            response, addr = s_sock.recvfrom(1024) #모든 수신자로부터 응답 수신
        except timeout:
            break
        else:
            print(f"{addr}로부터 응답 메세지: {response.decode()}")
s_sock.close()