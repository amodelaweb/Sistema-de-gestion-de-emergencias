import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from Interfaz.Conection import Conection
from Modelo.Client import Client

def main():
    port = 5002 # Random Port
    client = Client("Juan pablo", "residencia" , "ingeniro" , "localhost" , 5001 , "localhost" , port, [1,2,3] , [1,2,4])
    conection = Conection ("127.0.0.1" , port)
    client.subscribe()
    conection.init_server()
    while True :
        res = conection.listen(1024)
        print(res)
main()