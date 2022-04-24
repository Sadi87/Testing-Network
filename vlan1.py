from netmiko import ConnectHandler

network_device = {
        "device_type": "cisco_ios",
        "host": "192.168.211.159",
        "username": "admin",
        "password" : "cisco",
        }
Connect = ConnectHandler(**network_device)
Connect.enable()
problm = "show ip int br"
print(Connect.send_command(problm))