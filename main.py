import gspread
import os

gc=gspread.service_account(filename="credential.json")
sh=gc.open_by_key("1DHI3k0KYCeTFyj_JwDnTWu8fGvAmwGZXkQvxN_xw9t4")

accounts_sheet=sh.worksheet("accounts").get_all_values()
worksheet=[[]]
loggedin=False


def check_account():
    try:
        sh.add_worksheet(title="accounts", rows="100", cols="2")
    except:
        pass
    accounts_sheet=sh.worksheet("accounts")


def check(username):
    while 1:
        keyword=input("enter the service you are looking for: (enter quit to quit)")
        if keyword=="quit":
             break
        worksheet=sh.worksheet(username).get_all_values()
        print(worksheet)
        for temp in range(len(worksheet)):
            if keyword in worksheet[temp][0]:
                index=temp
                print("service:"+worksheet[index][0])
                print("id:"+worksheet[index][1])
                print("password:"+worksheet[index][2])
                print("note:"+worksheet[index][3])
                break
            elif temp == len(worksheet)-1:
                print("the service is not found!")

def add(username):
    worksheet=sh.worksheet(username).get_all_values()
    same=True
    while same:
        service=input("enter service:")
        for temp in range(len(worksheet)):
            if service in worksheet:
                print("that service is already in use,please try another name")
                break
            if temp ==len(worksheet)-1:
                same=False
    id=input("enter id:")
    password=input("enter password:")
    note=input("enter note:")
    worksheet.append([service,id,password,note])
    sh.worksheet(username).update(worksheet)

def login():
    global loggedin
    while not loggedin:
        id=input("enter your id:(enter quit to quit)")
        if id=="quit":
            break
        password=input("enter your password:")


        for temp in range(len(accounts_sheet)):
            if id==accounts_sheet[temp][0]:
                if password== accounts_sheet[temp][1]:
                    print("right")
                    username=accounts_sheet[temp][0]
                    loggedin=True
                    break
        if loggedin==False:
            print("wrong password or account")
    if loggedin:
        print("Log in successfully!")
        while 1:
            print("1) add new password")
            print("2) check password")
            print("3) log out")
            cmd=input("command:")

            if cmd=="1":
                add(username)
            elif cmd=="2":
                check(username)
            elif cmd=="3":
                loggedin=False
                start()
                break
            else:
                print("please input number between 1~3")

def register():
    global accounts_sheet
    print("Registeration")
    same=True
    while same:
        username=input("please enter username:")
        userpassword=input("please enter password:")
        accounts_sheet=sh.worksheet("accounts").get_all_values()
        for temp in range(len(accounts_sheet)):
            if username == accounts_sheet[temp][0]:
                print("username already in use, please change another one.")
                break
            elif temp ==len(accounts_sheet)-1:
                same=False
    sh.add_worksheet(title=username, rows="100", cols="4")
    worksheet =sh.worksheet("accounts")
    accounts_sheet.append([username,userpassword])
    worksheet.update(accounts_sheet)
    check_account()

    print("register account successfully!")

def start():
    print("Hi, wellcome to password manager!")
    check_account()

    while 1:
        print()
        print("1)login")
        print("2)create a account")
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
