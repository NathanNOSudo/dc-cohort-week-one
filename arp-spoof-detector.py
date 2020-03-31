#!/usr/bin/env python
import scapy.all as scapy
import sys
import time
from termcolor import colored


def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    retries = 4
    for i in range(retries):
        answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
        if answered_list:
            return answered_list[0][1].hwsrc
    return answered_list[0][1].hwsrc


def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)


def process_sniffed_packet(packet):
    if packet.haslayer(scapy.ARP) and packet[scapy.ARP].op == 2:
        try:
            real_mac = get_mac(packet[scapy.ARP].psrc)
            response_mac = packet[scapy.ARP].hwsrc
            if real_mac != response_mac:
                print(colored("\r[+] SYSTEM UNDER ATTACK", 'green', 'on_red', attrs=['bold']) + colored(" - Your ARP has been spoofed!", 'red', attrs=['reverse'])),
                sys.stdout.flush()
                time.sleep(2)
        except IndexError:
            pass


sniff("en0")

