#Lists
ports = [22, 80, 443, 8080]
print(ports[0]) #Acess the first item

ports.append(21) #Add a new port
print(ports)

#Dictionary (worth to keep key-valor data)
scan_result = {
    "host": "192.168.1.1",
    "open_ports": [22,80],
    "os": "Linux"
}
print(scan_result["os"])