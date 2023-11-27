# FTP
import ftplib

site = ""

try:
  ftp = ftplib.FTP(site)
  ftp.login()
  print("Connected to site:", site)
  print(ftp.retrlines("LIST"))
  ftp.quit()
except:
  print("Couldn't connect to site:", site)


