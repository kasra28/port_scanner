import socket
from time import sleep as l
from os import system as s
from IPy import IP

s("clear")

class bcolors:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

print(bcolors.BLUE + "online port scanner tool made by <kasra akhavan> iranian hacker")
l(1)
print(bcolors.RED + "enjoy informations gathering")
l(2)

def check_ip(ip):
    try:
        IP(ip)
        return(ip)
    except ValueError:
        return socket.gethostbyname(ip)
def check_port(ip, port):
    try:
        S = socket.socket()
        S.settimeout(0.5)
        S.connect((ip, port))
        print(bcolors.RED + "target----->" + str(ip) + bcolors.BLUE + "\nopen port: " + str(port))
    except :
        pass


def scan(ip):
    converted_ip = check_ip(ip)
    print('\n' + "+scan start+ on ----->" + str(ip))
    for port in range(int(port1) , int(port2) ):
        check_port(converted_ip, port)


def NMAP_RESULT(ip):
    con = input(bcolors.BLUE + "did you like to see nmap result: ")
    if con == "yes" or "y" or "Y" or "Yes":
        s("sudo nmap -sS " + ip)
    else:
        pass
ip = input(bcolors.GREEN + "enter target ip: ")
port1 = input(bcolors.BLUE + "enter first port: ")
port2 = input(bcolors.RED + "enter second port: ")
if ',' in ip :
    for ip_add in ip.split(','):
        scan(ip_add.strip(' '))
else:
    scan(ip)

NMAP_RESULT(ip)
