from ast import Index
import telnetlib
import getpass

user = input("Enter the Username: ")
password = getpass.getpass("Enter the Telnet Password: ")

with open('Sip.txt') as f:
    ip_list = f.read().splitlines()

count = 3

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
    tn.write(b"ip routing\n")

    if Index(line) == HOST:
        tn.write(b"int g0/2\n")
        tn.write(b"switchport trunk encapsulation dot1q\n")
        tn.write(b"switchport mode trunk\n")
        tn.write(b"Switchport trunk allowed vlan 1-99\n")
        tn.write(b"exit\n")

    for i in range(2, 10):
        count = count + 1
        if Index(line) == HOST:
            ip =  b"ip address 12.12." + str(count).encode('ascii') + b".1 255.255.255.0\n"
        
            tn.write(b"vlan " + str(i).encode('ascii') + b"\n")
            tn.write(b"name VLAN_" + str(i).encode('ascii') + b"\n")

            if i == 3:
                tn.write(b"name Management" + b"\n")
                tn.write(b"int vlan 3\n")
                tn.write(b"ip address 172.30." + str(count + 1).encode('ascii') + b".2 255.255.255.0\n")
                tn.write(b"no shutdown\n")
                tn.write(b"exit\n")
                tn.write(b"int g1/1\n")
                tn.write(b"switchport mode access\n")
                tn.write(b"switchport access vlan 3\n")
                tn.write(b"exit\n")
                tn.write(b"ip default-gateway 172.30." + str(count + 1).encode('ascii') + b".1\n")

                ## Management DHCP
                tn.write(b"ip dhcp exclude 172.32." + str(count + 1).encode('ascii') + b".1 172.30." + str(count + 1).encode('ascii') + b".10\n")
                tn.write(b"ip dhcp pool VLAN_Management_" + str(i).encode('ascii') + b"\n")
                tn.write(b"network 172.30." + str(count + 1).encode('ascii') + b".0 255.255.255.0\n")
                tn.write(b"defau 172.30." + str(count + 1).encode('ascii') + b".1\n")
                tn.write(b"dns 8.8.8.8\n")
                tn.write(b"exit\n")

                ## routing switch
                tn.write(b"router ospf 3\n")
                tn.write(b"router-id " + str(i+1).encode('ascii') + b"." + str(i).encode('ascii') + b"." + str(count + 5).encode('ascii') + b"." + b"1 \n")
                tn.write(b"network 172.30." + str(count + 1).encode('ascii') + b".0 0.0.0.255 area 0\n")
                tn.write(b"network 0.0.0.0 0.0.0.0 area 0\n")
                tn.write(b"network " + str(HOST).encode('ascii') + b" 0.0.0.255 area 0\n")
        
            if i == 4:
                tn.write(b"name Student" + b"\n")
                tn.write(b"int vlan 4\n")
                tn.write(b"ip address 172.30." + str(count + 2).encode('ascii') + b".2 255.255.255.0\n")
                tn.write(b"no shutdown\n")
                tn.write(b"exit\n")
                tn.write(b"int g1/2\n")
                tn.write(b"switchport mode access\n")
                tn.write(b"switchport access vlan 4\n")
                tn.write(b"exit\n")
                tn.write(b"ip default-gateway 172.30." + str(count + 2).encode('ascii') + b".1\n")

                ## Student DHCP
                tn.write(b"ip dhcp exclude 172.30." + str(count + 2).encode('ascii') + b".1 172.30." + str(count + 2).encode('ascii') + b".10\n")
                tn.write(b"ip dhcp pool VLAN_Student_" + str(i).encode('ascii') + b"\n")
                tn.write(b"network 172.30." + str(count + 2).encode('ascii') + b".0 255.255.255.0\n")
                tn.write(b"defau 172.30." + str(count + 2).encode('ascii') + b".1\n")
                tn.write(b"dns 8.8.8.8\n")
                tn.write(b"exit\n")


                ## routing switch
                tn.write(b"router ospf 4\n")
                tn.write(b"router-id " + str(i+2).encode('ascii') + b"." + str(i).encode('ascii') + b"." + str(count + 5).encode('ascii') + b"." + b"1 \n")
                tn.write(b"network 172.30." + str(count + 2).encode('ascii') + b".0 0.0.0.255 area 0\n")
                tn.write(b"network 0.0.0.0 0.0.0.0 area 0\n")
                tn.write(b"network " + str(HOST).encode('ascii') + b" 0.0.0.255 area 0\n")
        
            if i == 5:
                tn.write(b"name Staff" + b"\n")
                tn.write(b"int vlan 5\n")
                tn.write(b"ip address 172.30." + str(count + 3).encode('ascii') + b".2 255.255.255.0\n")
                tn.write(b"no shutdown\n")
                tn.write(b"exit\n")
                tn.write(b"int g1/3\n")
                tn.write(b"switchport mode access\n")
                tn.write(b"switchport access vlan 5\n")
                tn.write(b"exit\n")
                tn.write(b"ip default-gateway 172.30." + str(count + 3).encode('ascii') + b".1\n")

             ## Staff DHCP
                tn.write(b"ip dhcp exclude 10.10." + str(count + 3).encode('ascii') + b".1 172.30." + str(count + 3).encode('ascii') + b".10\n")
                tn.write(b"ip dhcp pool VLAN_Staff_" + str(i).encode('ascii') + b"\n")
                tn.write(b"network 172.30." + str(count + 3).encode('ascii') + b".0 255.255.255.0\n")
                tn.write(b"defau 172.30." + str(count + 3).encode('ascii') + b".1\n")
                tn.write(b"dns 8.8.8.8\n")
                tn.write(b"exit\n")


                ## routing switch
                tn.write(b"router ospf 5\n")
                tn.write(b"router-id " + str(i+3).encode('ascii') + b"." + str(i).encode('ascii') + b"." + str(count + 5).encode('ascii') + b"." + b"1 \n")
                tn.write(b"network 172.30." + str(count + 3).encode('ascii') + b".0 0.0.0.255 area 0\n")
                tn.write(b"network 0.0.0.0 0.0.0.0 area 0\n")
                tn.write(b"network " + str(HOST).encode('ascii') + b" 0.0.0.255 area 0\n")
                break
        

    tn.write(b"end\n")
    tn.write(b"wr\n")
    tn.write(b"show ip int br\n")
    tn.write(b"show vlan br\n")
    tn.write(b"exit\n")
    print(tn.read_all().decode())