# DNS
import dns # pip install dnspython
import dns.resolver
import dns.name

dnsA = list(dns.resolver.resolve("google.com", "A"))
print("A")
for response in dnsA:
  print(response)

dnsAAAA = list(dns.resolver.resolve("google.com", "AAAA"))
print("AAAA")
for response in dnsAAAA:
  print(response)

dnsMx = list(dns.resolver.resolve("google.com", "MX"))
print("MX")
for response in dnsMx:
  print(response)

dnsNS = list(dns.resolver.resolve("google.com", "NS"))
print("NS")
for response in dnsNS:
  print(response)

name1 = dns.name.from_text("www.google.com")
name2 = dns.name.from_text("google.com")
print(name1)
print(name2)

print(name1.is_subdomain(name2))
print(name2.is_subdomain(name1))
