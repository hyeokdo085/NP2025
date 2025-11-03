# time_client.py
import socket #socket 모듈 불러오기

#TCP 소켓 생성
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = ('localhost', 5000) 
sock.connect(address) #서버에 연결 요청
print(f"현재 시각: {sock.recv(1024).decode()}") 
#수신 바이트 문자열 변환 출력
sock.close() #소켓 닫기