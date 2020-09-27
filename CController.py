import ctypes
import os
import sys
import threading
import time
import socket

# GameConsole simple
def ProcessServer():	# Run as threading
	print(pDll)
	print "[Launcher] Processing server"
	pDll.Startup_Server()

def PoweroffServer():	# Run as threading
	print(pDll)
	print "[Launcher] Poweroffed server"
	pDll.Poweroff_Server()

def void_RestartServer():	# This is a virtual action
	print(pDll)
	print "[Launcher] Restarting server"
	pDll.Poweroff_Server()
	pDll.Startup_Server()

def socket_application():
	networkd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	networkd.bind(('127.0.0.1', 6500))
	networkd.listen(10000)
	print "Server is listening on %s:%s"%("127.0.0.1", 6500)
	while 1:
		conn, addr = networkd.accept()
		data = conn.recv(2048)
		
		if(data == b'\x00\x0f\x00\x00'):
			threading.Thread(target=ProcessServer).start()
			conn.sendall(b'\x00\x0f\x01\x00')

		if(data == b'\x00\x0f\x00\x01'):
			threading.Thread(target=PoweroffServer).start()
			conn.send(b'\x00\x0f\x01\x01')

		if(data == b'\x00\x0f\x0f\x00')
			threading.Thread(target=void_RestartServer).start()
			conn.send(b'\x00\x0f\x0f\x01')

		conn.close()

pDll = ctypes.WinDLL("./CustomProcessDynamicLibrary.dll")	#Override pDll
socket_application()
