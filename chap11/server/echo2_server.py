# 가상머신에서 실행
# echo2_server.py
import MyTCPServer as mt
import sys
port = 5000
if len(sys.argv) > 1: #명령 실행시 포트 지정하면 지정 포트 사용
    port = int(eval(sys.argv[1]))
sock = mt.TCPServer(port)
print(f"연결 대기")
c, addr = sock.Accept() #소켓과 주소 반환
print(f'연결 됨: {addr[0], addr[1]}') #주소와 포트
while True:
    data = c.recv(1024)
    if not data:
        break
    print(f'수신메세지: {data.decode()}')
    c.send(data) #수신한 데이터를 그대로 전송
c.close()
sock.sock.close()
print("연결 종료")