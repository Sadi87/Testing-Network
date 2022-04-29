import telnetlib
import getpass


user = input("Enter the Username: ")
password = getpass.getpass("Enter the Telnet Password: ")

with open('ip.txt') as f:
    ip_list = f.read().splitlines()

for line in ip_list:
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

 
        
        
    tn.write(b"end\n")
    tn.write(b"wr\n")
    tn.write(b"exit\n")
    tn.write(b"end\n")
    print(tn.read_all().decode())
