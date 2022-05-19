from netmiko import ConnectHandler

cisco_iso = {
    "device name": "cisco_iso",
    "ip": "192.168.211.144",
    "username": "admin",
    "password": "cisco",
    "secret": "cisco"
}
net_connect = ConnectHandler(**cisco_iso) 
net_connect.enable()

output = net_connect.send_command("show ip int br")
print(output)

