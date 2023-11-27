# Shodan search: hosts with possible FTP port open
import ftplib
import shodan

api_key = "yourAPIkey"
api_shodan = shodan.Shodan(api_key)

result = api_shodan.search("port: 21 Anonymous user logged in")

print(result.keys())
print(result["total"])

sites = []
for match in result["matches"]:
  sites.append(match["ip_str"])

for site in sites:
  try:
    ftp = ftplib.FTP(site)
    ftp.login()
    print("Connected to site:", site)
    print(ftp.retrlines("LIST"))
    ftp.quit()
  except:
    print("Couldn't connect to site:", site)

