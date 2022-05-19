
from ast import Index
import telnetlib
import getpass

user = input("Enter the Telnet Username: ")
password = getpass.getpass("Enter the telnet password: ")


with open('rp.txt') as f:
    ip_list = f.read().splitlines()
count = 2
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
    tn.write(b"no ip domain-lookup\n")
    tn.write(b"banner motd #This is Network Automation Assesment. Done By Sadi#\n")
	    
    for i in range (1,20):
        count = count + 2
        
        if Index(line) == HOST:
           
           ## interface g0/1 configuration 
            tn.write(b"int g0/1\n")
            tn.write(b"ip address 172.16." + str(count + 1).encode('ascii') + b".1 255.255.255.0\n")
            tn.write(b"description to S1\n")
            tn.write(b"no shutdown\n")
            tn.write(b"exit\n")

            ## interface g0/2 configuration
            tn.write(b"int g0/2\n")
            tn.write(b"ip address 172.16." + str(count + 2).encode('ascii') + b".1 255.255.255.0\n")
            tn.write(b"description to S2\n")
            tn.write(b"no shutdown\n")
            tn.write(b"exit\n")

            ## Dhcp for Interface For G0/1
            tn.write(b"ip dhcp exclude 172.16." + str(count + 1).encode('ascii') + b".1 172.16." + str(count + 1).encode('ascii') + b".10\n")
            tn.write(b"ip dhcp pool VLAN_" + str(count + 1).encode('ascii') + b"\n")
            tn.write(b"network 172.16." + str(count + 1).encode('ascii') + b".0 255.255.255.0\n")
            tn.write(b"defau 172.16." + str(count + 1).encode('ascii') + b".1\n")
            tn.write(b"dns 8.8.8.8\n")
            tn.write(b"exit\n")

            ## Dhcp for Interface For G0/2
            tn.write(b"ip dhcp exclude 172.16." + str(count + 2).encode('ascii') + b".1 172.16." + str(count + 2).encode('ascii') + b".10\n")
            tn.write(b"ip dhcp pool VLAN_" + str(count + 2).encode('ascii') + b"\n")
            tn.write(b"network 172.16." + str(count + 2).encode('ascii') + b".0 255.255.255.0\n")
            tn.write(b"defau 172.16." + str(count + 2).encode('ascii') + b".1\n")
            tn.write(b"dns 8.8.8.8\n")
            tn.write(b"exit\n")

            ## Routing Protocol config
            tn.write(b"router ospf 10\n")
            tn.write(b"router-id " + str(i).encode('ascii') + b"." + str(i).encode('ascii') + b"." + str(count).encode('ascii') + b"." + b"1 \n")
            tn.write(b"network 172.16." + str(count + 1).encode('ascii') + b".0 0.0.0.255 area 0 \n")
            tn.write(b"network 172.16." + str(count + 2).encode('ascii') + b".0 0.0.0.255 area 0 \n")
            tn.write(b"network 0.0.0.0 0.0.0.0 area 0\n")
            tn.write(b"network " + str(HOST).encode('ascii') + b" 0.0.0.255 area 0\n")
            
            break
        

    tn.write(b"end\n")
    tn.write(b"wr\n")
    tn.write(b"show ip int br\n")
    tn.write(b"exit\n")
    print(tn.read_all().decode())