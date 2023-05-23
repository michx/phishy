from requests_tor import RequestsTor

# If you use the Tor
rt = RequestsTor(tor_ports=(9050,), tor_cport=9051)

url = 'https://repubblica.it'
r = rt.get(url)
print(r.text)
