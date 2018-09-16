import sys
import os
import threading

sys.path.insert(1, os.path.join(sys.path[0], '..'))
from Modelo.Broker import Broker
from Modelo.Cliente import Cliente
from Modelo.Publisher import Publisher
sys.path.insert(1, os.path.join(sys.path[0], '../..'))
from shared.Message import MessageType

def main():
    if (len(sys.argv) < 4 or len(sys.argv) > 7):
        print (sys.argv[0] + " [ServerIp] [ServerPort] [Broadcast] ")
        print (sys.argv[0] + " [ServerIp] [ServerPort] [Broadcast] -s [Main_Broker_IP] [Main_Broker_PORT]")
        sys.exit(1)
    broker = Broker(sys.argv[1], int(sys.argv[2]), True, sys.argv[3])
    broker.conection.init_server()
    print("Broker Iniciado ! ")

    if (len(sys.argv) == 7):
        broker.subscribe(sys.argv[5] , sys.argv[6])

    while True:
        res,addr = broker.conection.listen(1024)
        if (res.get('messageType') == MessageType.SUBSCRIBER):
            broker.add_client(Cliente( addr[0],
                                       res.get('body').get('puerto') ,
                                       res.get('body').get('nombre'),
                                       res.get('body').get('residencia'),
                                       res.get('body').get('profesion'),
                                       res.get('body').get('comp_familiar'),
                                       res.get('body').get('temas')
                                      )  )
            hilo_difusion =  threading.Thread(target=broker.boadcast_brokers ,   args = (res,))
            hilo_difusion.start()
        elif (res.get('messageType') == MessageType.PUBLISHER):
            broker.add_publisher(Publisher(addr[0],
                                           res.get('body').get('nombre')
                                            ))
            hilo_difusion =  threading.Thread(target=broker.boadcast_brokers ,   args = (res,))
            hilo_difusion.start()
        elif (res.get('messageType') == MessageType.BROKER):
            hilo_difusion =  threading.Thread(target=broker.boadcast_brokers ,   args = (res,))
            hilo_difusion.start()
            broker.add_broker(Broker(res.get('body').get('ip'),
                                     int(res.get('body').get('port')) ,
                                     True,
                                     '255.255.255.255')
                                    )
        elif (res.get('messageType') == MessageType.NEWS):
            hilo_match = threading.Thread(target=broker.broadcast_to_clients ,   args = (res,))
            hilo_match.start()
    broker.conection.close_socket()

main()
