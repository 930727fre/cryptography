import os

if os.path.exists(credential.json):
    print("delete credential.json")
    os.remove("credential.json")

if os.path.exists(identification.cfg):
    print("delete identification.cfg")
    os.remove("identification.cfg")

print("delete all finished")
