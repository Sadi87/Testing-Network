import telnetlib
import getpass

user = input("Enter the Username: ")
password = getpass.getpass("Enter the Password: ")

with open('ip.txt') as f:
    ip_list = f.read().splitlines()

for line in ip_list:
    HOST = line.strip('\n')
    print("Telnet Connection Host is: " + HOST)
    tel = telnetlib.Telnet(HOST)

    tel.read_until(b"Username: ")
    tel.write(user.encode('ascii') + b"\n")
    if password:
        tel.read_until(b"Password: ")
        tel.write(password.encode('ascii') + b"\n")
    
    tel.write(b"enable\n")
    tel.write(b"cisco\n")
    tel.write(b"configure terminal\n")
    tel.write(b"banner motd #This is Network Automation Program#\n")
    
    for i in range (2,10):

        tel.write(b"vlan " + str(i).encode('ascii') + b"\n")
        tel.write(b"name vlan_" + str(i).encode('ascii') + b"\n")

        if i == 3:
            tel.write(b"name Management\n")
            tel.write(b"interface vlan 3\n")
            

        if i == 4:
            tel.write(b"name Student\n")
            tel.write(b"interface vlan 4\n")
            

        if i == 5:
            tel.write(b"name Staff\n")
            tel.write(b"interface vlan 5\n")
            
        if i == 6:
            tel.write(b"name native\n")
            tel.write(b"exit\n")

    if HOST == '192.168.211.157':

        tel.write(b"interface g0/0 \n")
        tel.write(b"no shutdown\n")
        tel.write(b"int vlan 1 \n")
        tel.write(b"ip address dhcp\n")
        tel.write(b"no shutdown\n")
        
    if HOST == '192.168.211.158':

        tel.write(b"interface g0/0 \n")
        tel.write(b"no shutdown\n")
        tel.write(b"int vlan 1 \n")
        tel.write(b"ip address dhcp\n")
        tel.write(b"no shutdown\n")
        
    
    if HOST == '192.168.211.153':

        tel.write(b"interface g0/0 \n")
        tel.write(b"no shutdown\n")
        tel.write(b"int vlan 1 \n")
        tel.write(b"ip address dhcp\n")
        tel.write(b"no shutdown\n")

    if HOST == '192.168.211.154':

        tel.write(b"interface g0/0 \n")
        tel.write(b"no shutdown\n")
        tel.write(b"int vlan 1 \n")
        tel.write(b"ip address dhcp\n")
        tel.write(b"no shutdown\n")



    tel.write(b"end\n")
    tel.write(b"wr\n")
    tel.write(b"exit\n")
    tel.write(b"end\n")
    print(tel.read_all().decode())