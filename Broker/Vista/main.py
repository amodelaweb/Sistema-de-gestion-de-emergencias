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
    broker = Broker("192.168.0.113", 5001, True, "192.168.0.255")
    broker.conection.init_server()
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

        elif (res.get('messageType') == MessageType.PUBLISHER):
            broker.add_publisher(Publisher(addr[0],
                                           res.get('body').get('nombre')
                                            ))
        elif (res.get('messageType') == MessageType.BROKER):
            broker.add_broker(Broker(res.get('body').get('ip'),
                                     res.get('body').get('puerto'),
                                     res.get('body').get('flag'),
                                     res.get('body').get('broadcast')
                                    ))

        elif (res.get('messageType') == MessageType.NEWS):
            print("ok")
            t = threading.Thread(target=broker.broadcast_to_clients ,   args = (res,))
            t.start()

    broker.conection.close_socket()

main()
