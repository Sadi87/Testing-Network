from netmiko import ConnectHandler

iosv_l2_R1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.211.146',
    'username': 'admin',
    'password': 'cisco'



all_devices = [iosv_l2_s1]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    for n in range (2,21):
       print ("Creating VLAN " + str(n))
       config_commands = ['vlan ' + str(n), 'name Python_VLAN ' + str(n)]
       output = net_connect.send_config_set(config_commands)
       print (output)