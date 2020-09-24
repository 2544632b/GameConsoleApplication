import ctypes
import os
import sys

# You may compile the python program as c binary.
cdef ProcessServer():	# Run as threading
	pDll = ctypes.WinDLL("./CustomProcessDymaicLibrary.dll")
	print(pDll)
	print "[Launcher] Processing server"
	pDll.Startup_Server()

cdef PoweroffServer():	# Run as threading
	pDll = ctypes.WinDLL("./CustomProcessDymaicLibrary.dll")
	print(pDll)
	print "[Launcher] Poweroffed server"
	pDll.Poweroff_Server()

cdef void_RestartServer():	# This is a virtual action
	pDll = ctypes.WinDLL("./CustomProcessDymaicLibrary.dll")
	print(pDll)
	print "[Launcher] Restarting server"
	pDll.Poweroff_Server()
	pDll.Startup_Server()