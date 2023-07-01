import urllib.request as request

req = request.Request('https://alx-intranet.hbtn.io/status')
with request.urlopen(req) as response:
    value = response.read()
    print(f"""Body response:
        - type: {type(value)}
        - content: {value}
        - utf8 content: {value.decode()}""")
