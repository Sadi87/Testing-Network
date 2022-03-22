import getpass
import getpass
import sys
import telnetlib

HOST = raw_input("Enter Device IP: ")
user = raw_input("Enter your Telnet username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until("Username: ")
tn.write(user + "\n")
if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")

tn.write("enable\n")
tn.write("cisco123\n")
tn.write("config t\n")
tn.write("int loop 1\n")
tn.write("ip address 10.10.10.1 255.255.255.0\n")
tn.write("no shutdown\n")
tn.write("end")
tn.write("exit\n")
tn.write("wr\n")

print tn.read_all()