# NMAP
# Pre-requirements
# sudo apt install nmap

# Console line:
# >>> python3
# >>> import nmap
# >>> port_scanner = nmap.PortScanner()
# >>> scan = port_scanner.scan("localhost", "1-1000")
# >>> print(scan)

import nmap # pip install python-nmap

# create the port scanner
port_scanner = nmap.PortScanner()
scan = port_scanner.scan("localhost", "1-1000")
# print(scan)

# print(scan.keys())
print("--------------------------------------")
print("Total scan elapsed time: " + scan["nmap"]["scanstats"]["elapsed"])
print("--------------------------------------")

# print(scan["scan"].keys())

# host = scan["scan"]["127.0.0.1"]
# print(host.keys())

for host in port_scanner.all_hosts():
  print("Results for host: " + host)
  print("--------------------------------------")

  for protocol in port_scanner[host].all_protocols():
    print("Protocol: " + protocol)
    print("--------------------------------------")
    for port in port_scanner[host][protocol].keys():
      current_port = port_scanner[host][protocol][port]
      print("Port: " + str(port))
      print("State: " + current_port["state"])
      print("Reason: " + current_port["reason"])
      print("Name: " + current_port["name"])
      print("Product: " + current_port["product"])
      print("Version: " + current_port["version"])
      print("Extrainfo: " + current_port["extrainfo"])
      print("Conf: " + current_port["conf"])
      print("CPE: " + current_port["cpe"])
      print("--------------------------------------")
