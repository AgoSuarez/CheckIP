import os
import os.path as path
import platform
from colorama import init, Fore, Back, Style

class CheckIP:
    def __init__(self):
        #Verificar el sistema operativo
        #Detectar si estamos en Windows, Linux o Mac
        self.sistema = platform.system()
        if (self.sistema == "Windows"):
            self.LimpiaPantalla = "cls"
        else:
            self.LimpiaPantalla = "clear"
        self.ipList = []

    def muestraMenu(self):
        #Mostrar el menu por pantalla
        op=''
        while True:
            os.system(self.LimpiaPantalla)
            print("{}#".format(Fore.RED)*80)
            print("{} MENU  CHECK-IP {}".format("#"*32,"#"*32))
            print("{}#{}".format(Fore.RED,Fore.RESET)*80)
            print('\n')
            print('{} (1) {} Hacer ping a una sola IP'.format(Fore.YELLOW, Fore.RESET))
            print('{} (2) {} Hacer ping a una lista de IP (ip_list.txt)'.format(Fore.YELLOW, Fore.RESET))
            print('{} (S) {} Salir'.format(Fore.YELLOW, Fore.RESET))
            #ip = input("Introduce la IP a verificar: ")
            op = input('\n{} Elige una opción: {}'.format(Fore.LIGHTWHITE_EX, Fore.RESET))
            if op == '1':
                self._pingIP()
            elif op == '2':
                self._pingFile()
            elif op == 's' or op == 'S':
                self._salir()
                break

    def _salir(self):
        #Metodo para salir del programa
        os.system(self.LimpiaPantalla)
        print('{} Gracias por usar Check IP {}'.format(Fore.LIGHTBLUE_EX, Fore.RESET))

    def _pingIP(self):
        #Pide la IP para hacer el ping a una unica Direccion IP.
        print("*"*80)
        ip = input("Introduce la IP:")
        self.ipList.append({"ip":ip, "host":"Host único", "estado":"0"}) 
        self._checkIP()

    def _pingFile(self):
        if path.isfile("ip_list.txt"):
            #print("El fichero existe")
            f = open("ip_list.txt", 'r')
            #Abrimos el fichero
            for linea in f:
                #Recorremos el fichero linea a linea
                if linea[-1] == '\n':
                    #Si el ultimo caracter de la linea es un retorno de carro lo eliminamos
                    linea = linea[:-1]
                linea = str.split(linea, ',')
                #Creamos un diccionario con el nombre del host y la direccion IP
                ip = ({"host":linea[0],"ip":linea[1],"estado":"0"})
                #Lo añadimos a la lista de IPs para hacer PING
                self.ipList.append(ip)
            #cont= input()
            self._checkIP()
            f.close()
        else:
            print("{} * - *  El fichero NO EXISTE * - *{}".format(Fore.RED, Fore.RESET))
            cont = input('''Debe de existir el fichero ip_list.txt. Debe contener nombre el host y dirección IP (host,ip) en cada linea''')
    

    def _doPing(self, ip):
        #Hace el PING  a la IP
        print("*"*80)
        print("{}{}Iniciando PING al equipo: {}{} ({}) {}  ".format(" "*15, Fore.BLUE,Fore.LIGHTBLUE_EX, ip["host"], ip["ip"], Fore.RESET ))
        print("_"*80)
        ping = os.system('ping -n 3 {}'.format(ip["ip"]))
        

    def _checkIP(self):
        #Recorre la lista de IPs para luego hacer PING a cada IP        
        for ip in self.ipList:
            print(ip)
            self._doPing(ip)
        cont = input("Presione cualquier tecla para continuar")



if __name__ == '__main__':
    app = CheckIP()
    app.muestraMenu()