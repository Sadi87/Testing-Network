import imp
from ipaddress import ip_address
import telnetlib
import getpass


user = input("Enter the Username: ")
password = getpass.getpass("Enter the Telnet Password: ")

f_handle = open('ip.txt')

for line in f_handle:
    HOST = line.strip('\n')
    print("Telnet to host: " + HOST)
    tn = telnetlib.Telnet(HOST)

    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")
    
    tn.write(b"enable\n")
    tn.write(b"cisco\n")
    tn.write(b"configure terminal\n")

    for i in range(2, 10):
        j = str(i)
        tn.write(b"vlan " + j.encode('ascii') + b"\n")
        tn.write(b"name VLAN_" + j.encode('ascii') + b"\n")
        if i == 3:
            tn.write(b"name Management" + b"\n")
            tn.write(b"int vlan 3\n")
            tn.write(b"ip address 192.168." +j.encode('ascii') + b"1.1 255.255.255.0\n")
            tn.write(b"no shutdown\n")
            tn.write(b"exit\n")
        if i == 4:
            tn.write(b"name Student" + b"\n")
            tn.write(b"int vlan 4\n")
            tn.write(b"ip address 192.168." +j.encode('ascii') + b"1.1 255.255.255.0\n")
            tn.write(b"no shutdown\n")
            tn.write(b"exit\n")
        if i == 5:
            tn.write(b"name Staff" + b"\n")
            tn.write(b"int vlan 5\n")
            tn.write(b"ip address 192.168." +j.encode('ascii') + b"1.1 255.255.255.0\n")
            tn.write(b"no shutdown\n")
        
    

    
    tn.write(b"end\n")
    tn.write(b"exit\n")
    print(tn.read_all().decode())
