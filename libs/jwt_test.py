import http.client

conn = http.client.HTTPSConnection("dev-rz4pu53g5jc2vgj2.us.auth0.com")

payload = "{\"client_id\":\"gqLsyr56AIXTAD96xVZpsC7iDr5sTr6E\",\"client_secret\":\"_VTDETXuGFMwG9fg6FiHh6-zB-eLfz2BhQ7NXz5A5BqhWknTjKK-vZ8_VoXC8Lqq\",\"audience\":\"https://dev-rz4pu53g5jc2vgj2.us.auth0.com/api/v2/\",\"grant_type\":\"client_credentials\"}"

headers = { 'content-type': "application/json" }

conn.request("POST", "/oauth/token", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))