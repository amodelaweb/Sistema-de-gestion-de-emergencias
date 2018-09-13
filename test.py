import socket
import json

# DATOS DEL SERVIDOR
UDP_IP = "192.168.0.113"
PORT = 5001

# INICIALIZAR NUESTRO SOCKET DE ENVIO
ip_addr = socket.gethostbyname(socket.getfqdn())
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print ("Publicador ha iniciado")

# INICIALIZAR JSON STRING
json_string = {}
json_string ["publicacion"] = {"topico": "papas", "contenido":"Subio la papa 300 pesos"}
print (str(json_string).replace("'",'"'))

# PREPARAR MENSAJE PARA EL ENVIO
mensaje = str(json_string).replace("'",'"')
mensaje = mensaje.encode('utf-8')

# ENVIO DEL MENSAJE
sock.sendto(mensaje,(UDP_IP, PORT))
print ('Mensaje Enviado:= ', mensaje)
