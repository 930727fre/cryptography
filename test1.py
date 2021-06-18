import bcrypt

passwd = b's$cret12'

salt = bcrypt.gensalt()
hashed = bcrypt.hashpw(passwd, salt)

print(hashed)
hashed="$2a$12$R5qwnnXHkemo/itoSzvuhe3pD7iRqBWqr6x4kCmNuueCWo5uDFDZC"
print(hashed)

if bcrypt.checkpw(passwd, hashed):
    print("match")
else:
    print("does not match")
