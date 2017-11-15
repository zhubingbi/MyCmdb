#!/usr/bin/python
# -*- coding: utf-8 -*-
from scapy.all import *
from time import ctime,sleep
import threading
TIMEOUT = 4
conf.verb=0

def pro(cc,handle):
    dst = "192.168.1." + str(cc)
    packet = IP(dst=dst, ttl=20)/ICMP()
    reply = sr1(packet, timeout=TIMEOUT)
    if not (reply is None):
        handle.write(reply.src+" is online"+"\n")

def main():
    threads=[]
    f=open('ip.log','a')
    for i in range(2,254):
        t=threading.Thread(target=pro,args=(i,f))
        threads.append(t)
        print "main Thread begins at ",ctime()
    for t in threads :
        t.start()
    for t in threads :
        t.join()
        print "main Thread ends at ",ctime()
if __name__=="__main__" :
    main()