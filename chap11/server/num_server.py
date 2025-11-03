# 가상머신에서 실행
# num_server.py
import socket

table = {'1':'one', '2':'two', '3':'three', '4':'four',\
         '5':'five', '6':'six', '7':'seven', '8':'eight',\
         '9':'nine', '10':'ten'}

s = socket.socket() #기본적으로 AF_INET, SOCK_STREAM 사용
address = ("", 5000)
s.bind(address)
s.listen(5)
print(f"연결 대기")
c_socket, c_addr = s.accept()
print(f"연결 됨: {c_addr}")

while True:
    data = c_socket.recv(1024).decode()
    try:
        resp = table[data]
    except:
        c_socket.send("다시 시도하세요".encode())
    else:
        c_socket.send(resp.encode())

    if not data:
        break #데이터가 없으면 종료
c_socket.close() #연결 종료
s.close() #소켓 종료
print("연결 종료")