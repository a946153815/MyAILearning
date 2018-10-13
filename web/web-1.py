import socket
def serve_client(client_link):
    request=client_link.recv(1024)
    print(request)
    response="HTTP/1.1 200 OK \r\n"
    response+="\r\n"
    response+="你好，李海巽！"
    client_link.send(response.encode("utf-8"))
    client_link.close()
    pass

def main():
    server_tcp_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server_tcp_socket.bind(("",5600))
    server_tcp_socket.listen(128)
    while True:
        client_link,addr=server_tcp_socket.accept()
        serve_client(client_link)
    server_tcp_socket.close()
    pass

if __name__ == '__main__':
    main()