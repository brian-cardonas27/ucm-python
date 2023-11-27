# ICMP
from subprocess import CalledProcessError, check_output

connectedIps = []
for ip in range(1, 256):
  ipAddress = "192.168.1." + str(ip)
  print(ipAddress)

  try:
    # Ping
    check_output(["ping", "-c", "1", ipAddress])
    print("IP is connected")
    connectedIps.append(ipAddress)
  except CalledProcessError:
    print("IP is not connected")

print("Connected IPs:", connectedIps)
