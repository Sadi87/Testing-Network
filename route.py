
import telnetlib
import getpass

from vlan1 import HOST


user = input("Enter the Telnet Username: ")
password = getpass.getpass("Enter the telnet password: ")

f_handle = open('rp.txt')

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

    if f_handle == '192.168.211.159':
        tn.write(b"interface g0/1\n")
        tn.write(b"ip address 172.16.1.1 255.255.255.0 \n")
        tn.write(b"no shutdown\n")
        tn.write(b"exit\n")
    elif f_handle == '192.168.211.160':
        tn.write(b"interface g0/1\n")
        tn.write(b"ip address 172.16.2.1 255.255.255.0 \n")
        tn.write(b"no shutdown\n")
        tn.write(b"exit\n")
    else :
        tn.write(b"interface loopback0\n")
        tn.write(b"ip address 11.1.1.1 255.255.255.0 \n")
        tn.write(b"no shutdown\n")
        tn.write(b"exit\n")
    

tn.write(b"end\n")
tn.write(b"wr\n")
tn.write(b"exit\n")
print(tn.read_all().decode())
