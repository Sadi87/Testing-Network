from ast import Index


with open('ip.txt') as f:
    ip_list = f.read().splitlines()
count = 2
for line in ip_list:
    HOST = line.strip('\n\n')
    print("Telnet to host: " + HOST)

    for i in range (1,5):
        for j in range(i):
            if Index(line) == HOST :
                