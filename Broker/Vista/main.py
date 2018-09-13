import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from Modelo.Broker import Broker

def main():
    broker = Broker("192.168.0.113", 5001, True, "192.168.0.255")
    broker.conection.init_server()
    while True:
        res = broker.conection.listen(1024)
        print (res)

    broker.conection.close_socket()
main()
