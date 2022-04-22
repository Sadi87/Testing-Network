import imp
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
    
    tn.write(b"end\n")
    tn.write(b"exit\n")
    print(tn.read_all().decode())
