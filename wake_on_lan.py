import socket
import struct

mac = "70-85-C2-07-87-D5"	#본인의 MAC 주소를 입력해주세요!
macsplit = mac.split("-")

addrs = struct.pack("BBBBBB", int(macsplit[0], 16),int(macsplit[1], 16)
,int(macsplit[2], 16)
,int(macsplit[3], 16)
,int(macsplit[4], 16)
,int(macsplit[5], 16))

magic = b"\xFF" * 6 + addrs * 16

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
sock.sendto(magic,('192.168.0.255', 9))	#내부아이피주소가 다르다면 변경해주세요!
sock.close()