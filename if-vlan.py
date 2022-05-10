
import getpass
from ssl import _PasswordType
import sys
import telnetlib

from paramiko import PasswordRequiredException

HOST = input ("Enter Device IP: ")
user = input ("Enter your Telnet username: ")
try:
    p = getpass.getpass()
except Exception as error:
    print('ERROR', error)
else:
    print('Password entered:', p)

tn = telnetlib.Telnet(HOST)

tn.read_until("Username: ")
tn.write(user + "\n")
if _PasswordType:
    tn.read_until("Password: ")
    tn.write(PasswordRequiredException + "\n")

tn.write("enable\n")
tn.write("cisco\n")
tn.write("config t\n")
tn.write("int loop 1\n")
tn.write("ip address 10.10.10.1 255.255.255.0\n")
tn.write("no shutdown\n")
tn.write("end")
tn.write("exit\n")
tn.write("wr\n")

print(tn.read_all)