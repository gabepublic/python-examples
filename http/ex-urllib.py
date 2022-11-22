import urllib.request as request

u = request.urlopen('https://randomuser.me/api/?results=50')
data = u.read()    # JSON
print(data)

