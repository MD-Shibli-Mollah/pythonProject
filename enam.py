import base64

msg = "aHR0cHM6Ly9mb3Jtcy5nbGUvWU5ZXQ0d2NRWHVLNnNwdjU=="
url = base64.b64decode(msg)
print(url)
