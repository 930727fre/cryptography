import os

if not os.path.isfile("credential.json"):
    print("credential.json is missing")
else:
    print("credential.json checked")
