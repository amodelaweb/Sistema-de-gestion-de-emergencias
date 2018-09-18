import sys
import os
import threading

sys.path.insert(1, os.path.join(sys.path[0], '..'))
from Modelo.Balanceador import Balanceador

sys.path.insert(1, os.path.join(sys.path[0], '../..'))
from shared.Message import MessageType
from Broker.Modelo.Broker import Broker

def main():
    if (len(sys.argv) != 3):
        print (sys.argv[0] + " [ServerIp] [ServerPort]")
        sys.exit(1)

    balanceador = Balanceador(sys.argv[1], int(sys.argv[2]))
    balanceador.conection.init_server()
    print("Balanceador Iniciado ! ")

    while True:
        res,addr = balanceador.conection.listen(1024)
        balanceador.round_robin(res)
        if (res.get('messageType') == MessageType.BROKER):
            hilo_mis_brokers = threading.Thread(target=balanceador.send_brokers ,   args = (addr[0],addr[1],))
            hilo_mis_brokers.start()
            balanceador.add_broker(Broker(res.get('body').get('ip'),
                                     int(res.get('body').get('port')) ,
                                     True,
                                     '255.255.255.255')
                                    )

    balanceador.conection.close_socket()


main()
