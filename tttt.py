import telnetlib
import getpass

from multi import HOST

user = input("Enter the username : ")
password = getpass.getpass("Enter the password: ")

f_handle = open('rp.txt')

for line in f_handle:
    HOST = line.strip("\n")
    print("Telnet to the Host: " + HOST)
    tn = telnetlib.Telnet(HOST)

    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")
    
    tn.write(b"enable\n")
    tn.write(b"cisco\n")
    tn.write(b"config t\n")
    tn.write(b"no ip domain-lookup\n")
    tn.write(b"banner motd #This is Network Automation#\n")

    if f_handle == HOST:
        for i in range(2,10):
            tn.write(b"int g0/2\n")
            tn.write(b"ip address 10.10." + str(i) + b".1\n")
            tn.write(b"no shutdown\n")
    
            tn.write(b"ip dhcp excluded 192.168." + str(i) + ".1 192.168." + str(i) + ".20\n" )
            tn.write(b"ip dhcp pool Router_1\n")
            tn.write(b"network 192.168." + str(i) + "0 255.255.255.0\n")
            tn.write(b"default 192.168." + str(i) + ".1\n")
            tn.write(b"domain cisco.com\n")
            tn.write(b"dns 8.8.8.8\n")
            tn.write(b"end\n")

tn.write(b"end\n")
tn.write(b"wr\n")
tn.write(b"exit\n")
tn.write(b"exit\n")
print(tn.read_all().decode())
