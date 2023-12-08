# Analyse URL and detect tech stack of the Web App (detection tool)

import subprocess # pip install wad
import json

url = "https://ucm.edu.co/"

subprocess.call("wad -u" + url + "> tech_pj.txt", shell = True)

tech_stack = open("tech_stack.txt", "r")
text = tech_stack.read()

print(type(text))
print(text)

json_object = json.loads(text)

print(type(json_object))

for tech in json_object[url]:
  print(tech["app"])

