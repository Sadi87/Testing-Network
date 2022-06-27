from netmiko import ConnectHandler


r1 = {
    "device_type": "cisco_ios",
    "ip":"192.168.211.170",
    "username": "admin",
    "password": "cisco",
    "secret": "cisco",
     }
     
net_connect = ConnectHandler(**r1)
net_connect.enable()

result = net_connect.send_command('show ip int br')

print(result)

