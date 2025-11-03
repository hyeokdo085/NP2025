# client_demo.py
import socket
port = int(input("포트: "))
address = ('localhost', port) #서버주소,포트번호
BUFSUZE = 1024
s = socket.create_connection(address)
#소켓 생성과 동시에 연결

while True:
    msg = input("보낼 메세지: ")

    try:
        s.send(msg.encode()) #메세지 전송
    except:
        print("전송 중 예외 발생")
        continue

    try:
        data = s.recv(BUFSUZE) #서버로부터 메세지 수신
    except:
        print("수신 중 예외 발생")
        continue
    print(f"수신 메세지: {data.decode()}") #수신 바이트 문자열 변환 출력