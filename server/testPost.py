import requests

url = 'http://localhost:5000/post'
myobj = {
    'username': 'mutayyabtariq',
    'email': 'mutayyabtariq9@gmail.com',
    'password': "burger123"
    }

x = requests.post(url, data = myobj)

print(x.text)
print("Complete...")