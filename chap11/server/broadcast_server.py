# 가상머신에서 실행
# broadcast_server.py
from socket import *

sock = socket(AF_INET, SOCK_DGRAM) #UDP 소켓 생성
sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1) #주소 재사용 설정
sock.bind(('', 10000)) #모든 인터페이스, 포트2500 바인드
print("브로드캐스트 서버 시작")

while True:
    msg, addr = sock.recvfrom(1024) #메세지 수신
    print(f"수신 메세지: {msg.decode()}")
    sock.sendto(msg, addr) #에코 메세지 송신
sock.close()