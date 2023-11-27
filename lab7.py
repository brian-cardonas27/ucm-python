# Shodan
import shodan # pip install shodan
import requests

ip = input("Please enter an IP address: ")
api_key = "YourShodanAPIKey"
api_shodan = shodan.Shodan(api_key)
host = api_shodan.host(ip)

with open("lab7.txt", "w") as file:
  file.write("host info:\n")
  file.write("--------------------------------------\n")
  file.write("IP: " + ip + "\n")
  file.write("country: " + host.get("country_name", "N/A") + "\n")
  file.write("region_code: " + host.get("region_code", "N/A") + "\n")
  file.write("area_code: " + str(host.get("area_code", "N/A")) + "\n")
  file.write("org: " + host.get("org", "N/A") + "\n")
  file.write("latitude: " + str(host.get("latitude", "N/A")) + "\n")
  file.write("longitude: " + str(host.get("longitude", "N/A")) + "\n")
  file.write("last_update: " + host.get("last_update", "N/A") + "\n")
  file.write("tags: " + str(host.get("tags", "N/A")) + "\n")
  file.write("--------------------------------------\n")
  file.write("vulnerabilities:\n")
  file.write("--------------------------------------\n")

api_cve = "https://cve.circl.lu/api/cve/"
vulns = host.get("vulns", "N/A")
for vuln in vulns:
  response = requests.get(api_cve + vuln)
  with open("lab7.txt", "a") as file:
    file.write(response.json()["id"] + "\n")
    file.write("--------------------------------------\n")
    file.write("CVSS: " + str(response.json()["cvss"]) + "\n")
    file.write("--------------------------------------\n")
    file.write("impact:\n")
    file.write("--------------------------------------\n")
    file.write("availability: " + response.json()["impact"]["availability"] + "\n")
    file.write("confidentiality: " + response.json()["impact"]["confidentiality"] + "\n")
    file.write("integrity: " + response.json()["impact"]["integrity"] + "\n")
    file.write("--------------------------------------\n")
    file.write("summary: " + response.json()["summary"] + "\n")
    file.write("--------------------------------------\n")
