import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from Interfaz.Conection import Conection

def main():
    conection = Conection("" , 5001)
    conection.init_server()
    while True:
        res = conection.listen(1024)
        print (res)
        
    conection.close_socket()

main()
