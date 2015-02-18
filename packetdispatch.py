__author__ = 'constantinose'

import socket
import sys
import random


def sendPackets(address, port, requests, size):
    to_socket = socket.socket(socket.AF_INET,  # Internet
                              socket.SOCK_DGRAM)  # UDP

    # Convert input arguments to required type
    targ_addr = str(address)
    targ_port = int(port)
    targ_reqs = int(requests)
    packet_size = int(size)

    i = 0
    while i != targ_reqs:
        to_socket.sendto(_generatePacket(packet_size), (targ_addr, targ_port))
        i += 1
        sys.stdout.write("\rSent %i" % i + " packets")
    return


def _generatePacket(size):
    chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A',
             'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
             'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',
             'X', 'T', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
             'i', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
             'u', 'v', 'w', 'x', 'y', 'z']

    packet = ''
    for i in range(0, size):
        packet += chars[random.randint(0, 60)]

    return bytes(packet, "utf-8")