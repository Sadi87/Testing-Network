import getpass
import telnetlib

HOST = "192.168.122.136"
user = "admin"
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
tn.write(b"ip add 10.10.10.1 255.255.255.0\n")
tn.write(b"no shutdown\n")
tn.write(b"interface loop 2\n")
tn.write(b"ip add 11.10.10.1 255.255.255.0\n")
tn.write(b"no shutdown\n")
tn.write(b"exit\n")
tn.write(b"end\n")
print(tn.read_all().decode('ascii'))
