# 가상머신에서 실행
# time_server.py
import socket #소켓 모듈 불러오기
import time #시간 모듈 불러오기

# TCP 소켓 생성
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = ('localhost', 5000) #임의 주소와 포트 설정
s.bind(address) #소켓을 주소에 바인딩
s.listen(5) #클라이언트 연결 대기(5개까지)
print(f"서버가 {address}에서 시작되었습니다.")

while True:
    client, addr = s.accept() #클라이언트 연결 수락
    print(f"{addr}로부터 연결 요청")
    client.send(time.asctime().encode()) #현재 시간 전송
    client.close() #소켓 종료
    print(f"{addr}와의 연결 종료")