import socket
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print('Запуск сервера...')
server.bind(('localhost',9090))
print('Начало прослушивания порта...')
server.listen()
print('Подключение клиента...')
conn,addr = server.accept()
print(addr)
msg = ''
while True:
	print('Прием данных')
	data = conn.recv(1024)
	if not data:
		break
	msg+=data.decode()
	print('Отправка данных')
	conn.send(data.upper())

print(msg)
print('Отключение клиента')
conn.close()
print('Сервер остановлен')
