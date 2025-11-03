# 가상머신에서 실행
# echo_server.py
from socket import *

port = 5000 #포트 설정
BUFSIZE = 1024 #최대 수신 바이트

sock = socket(AF_INET, SOCK_STREAM)
address = ('localhost', port)
sock.bind(address) #소켓을 주소에 바인딩
sock.listen(1)
print(f"서버가 {address}에서 시작되었습니다.")
conn, (remotehost, remoteport) = sock.accept() 
#연결소켓, 연결주소 반환
print(f"연결됨: {remotehost}:{remoteport}")

while True:

    try:
        data = conn.recv(BUFSIZE) #데이터 수신
    except:
        conn.close() #수신 예외발생시 소켓 종료
        print("수신 중 예외 발생")
        break
    else:
        print(f"수신: {data.decode()}") #수신 데이터(바이트)를 문자열 출력
        
    if not data:
        break #데이터가 없으면 종료
    
    try:
        conn.send(data) #수신한 데이터를 되돌려 전송
    except:
        conn.close()
        print("전송 중 예외 발생")
        break
conn.close() #연결 종료
sock.close() #소켓 종료
print("연결 종료")