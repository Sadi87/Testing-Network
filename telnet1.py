import getpass
import telnetlib

HOST = "192.168.211.142"
user = input("Enter username ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"en\n")
tn.write(b"cisco\n")
tn.write(b"conf t\n")
tn.write(b"interface loop 1\n")


print(tn.read_all().decode('ascii'))