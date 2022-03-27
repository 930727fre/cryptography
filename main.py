import gspread, clipboard, pprint, bcrypt

YOUR_KEY=""
gc=gspread.service_account(filename="authentication.json")
sh=gc.open_by_key(YOUR_KEY)
salt = bcrypt.gensalt()
try:
    accounts_sheet=sh.worksheet("accounts").get_all_values()
except:
    pass
worksheet=[[]]
loggedin=False
quit=False


def check_account():
    try: # open the worksheet "accounts" in the first run
        sh.add_worksheet(title="accounts", rows="100", cols="2")
        temp=[["username","userpassword"]]
        sh.worksheet("accounts").update(temp)
    except:
        pass
    accounts_sheet=sh.worksheet("accounts")


def check(username):
    while True:
        service=input("enter the service you are looking for: (enter quit to quit)")
        if service == "quit":
             break
        worksheet=sh.worksheet(username).get_all_values()
        for temp in range(len(worksheet)):
            if service == worksheet[temp][0]:
                index=temp
                print()
                print("service:"+worksheet[index][0])
                print("id:"+worksheet[index][1])
                print("password:"+worksheet[index][2])
                print("note:"+worksheet[index][3])
                print("[the password has been copied to your clipboard!]")
                print()
                clipboard.copy(worksheet[index][2])
                break
            if temp == len(worksheet)-1:
                print("the service is not found!")

def add(username):
    worksheet=sh.worksheet(username).get_all_values()
    same=True
    service=input("enter service:")
    if service in worksheet:
        print("that service is already in use, please try another name")
    else:
        id=input("enter id:")
        password=input("enter password:")
        note=input("enter note:")
        worksheet.append([service,id,password,note])
        sh.worksheet(username).update(worksheet)

def check_all(username):
    worksheet=sh.worksheet(username).get_all_values()
    print()
    pprint.pprint(worksheet,depth=4)
    print()

def login():
    global loggedin,quit
    while not loggedin:
        username=input("enter your username:(enter quit to quit)")
        if username=="quit":
            break
        password=input("enter your password:")

        for temp in range(len(accounts_sheet)):
            if username == accounts_sheet[temp][0]:
                if  bcrypt.checkpw(str(password).encode('utf-8'),accounts_sheet[temp][1].encode('utf-8')):
                    username=accounts_sheet[temp][0]
                    loggedin=True
                    break
        if loggedin==False:
            print("Invalid account or password.")
    if loggedin:
        print("Log in successfully!")
        while 1:
            print("1) add new password")
            print("2) check password")
            print("3) check all password")
            print("4) log out")
            cmd=input("command:")

            if cmd=="1":
                add(username)
            elif cmd=="2":
                check(username)
            elif cmd=="3":
                check_all(username)
            elif cmd=="4":
                loggedin=False
                start()
                quit=True
                break
            else:
                print("please input number between 1~3")

def register():
    global accounts_sheet
    print("Registeration")
    while True:
        username=input("please enter username:")
        userpassword=str(input("please enter password:"))
        hashed = bcrypt.hashpw(userpassword.encode("utf-8"), salt)
        accounts_sheet=sh.worksheet("accounts").get_all_values()
        if username in accounts_sheet:
            print("this username already in use, please use another one.")
        else:
            break
    sh.add_worksheet(title=username, rows="30", cols="4")
    worksheet=sh.worksheet(username)
    worksheet.update([["service","id","password","note"]])
    worksheet=sh.worksheet("accounts")
    hashed=hashed.decode("utf-8")
    accounts_sheet.append([username,hashed])
    worksheet.update(accounts_sheet)
    check_account()

    print("register successfully!")

def start():
    global quit
    print("Hi, wellcome to password manager!")
    check_account()

    while not quit:
        print("1)login")
        print("2)create an account")
        print("3)quit")
        cmd=input("command:")

        if cmd=="1":
            login()
        elif cmd=="2":
            register()
        elif cmd=="3":
            print("bye bye!")
            break
        else:
            print("please input number between 1~3")


start()
