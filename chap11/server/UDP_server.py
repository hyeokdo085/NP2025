# 가상머신에서 실행
# UDP_server.py
import socket
port = 2500
BUFFSIZE = 1024
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', port))
print(f"UDP 서버 시작: 포트 {port}")
while True:
    data, addr = sock.recvfrom(BUFFSIZE) 
    print(f"수신 메세지: {data.decode()}")

    sock.sendto(data, addr) #에코 메세지 송신
sock.close()