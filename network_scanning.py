from scapy.all import Ether,ARP,conf,srp
import sys
import datetime

def arp_scan(iface,ip_range):
    print("[+]scanning ",ip_range)
#    cr_time=datetime.datetime.now()
#    print("scanning start at ",cr_time)
    conf.verb=0
    broadcast="ff:ff:ff:ff:ff:ff"
    ether_layer=Ether(dst=broadcast)
    arp_layer=ARP(pdst=ip_range)
    packet=ether_layer/arp_layer

    ans,uans=srp(packet,iface=iface,timeout=2,inter=0.1)

    for snd,rcv in ans:
        ip=rcv[ARP].psrc
        mac=rcv[Ether].src
        print(ip,mac)


if __name__ == '__main__':
    iface=sys.argv[1]
    ip_range=sys.argv[2]
    arp_scan(iface,ip_range)
