import gspread
import clipboard
import pprint
import bcrypt
import getpass
import configparser
import telebot

config = configparser.ConfigParser()
config.read('config.cfg')

gc=gspread.service_account(filename="credential.json")
sh=gc.open_by_key(config["google-cloud"]["token"])

bot=telebot.Telebot(config["telegram-api"]["token"])

bot.send_message("hi there!")

@bot.message_handler(commands=["hi"])
def command():
    print(config["google-cloud"]["token"])


salt = bcrypt.gensalt()

try:
    accounts_sheet=sh.worksheet("accounts").get_all_values()
except:
    pass
worksheet=[[]]
loggedin=False
quit=False


def check_account():
    try:
        sh.add_worksheet(title="accounts", rows="100", cols="2")
        temp=[["username","userpassword"]]
        sh.worksheet("accounts").update(temp)
    except:
        pass
    accounts_sheet=sh.worksheet("accounts")


def check(username):
    while 1:
        keyword=input("enter the service you are looking for: (enter quit to quit)")
        if keyword=="quit":
             break
        worksheet=sh.worksheet(username).get_all_values()
        for temp in range(len(worksheet)):
            if keyword == worksheet[temp][0]:
                index=temp
                print("service:"+worksheet[index][0])
                print("id:"+worksheet[index][1])
                print("password:"+worksheet[index][2])
                print("note:"+worksheet[index][3])
                print("the password has been copied to your clipboard!")
                clipboard.copy(worksheet[index][2])
                break
            if temp == len(worksheet)-1:
                print("the service is not found!")

def add(username):
    worksheet=sh.worksheet(username).get_all_values()
    same=True
    while same:
        service=input("enter service:")
        for temp in range(len(worksheet)):
            if service == worksheet[temp][0]:
                print("that service is already in use,please try another name")
                break
            if temp ==len(worksheet)-1:
                same=False
    id=input("enter id:")
    password=input("enter password:")
    note=input("enter note:")
    worksheet.append([service,id,password,note])
    sh.worksheet(username).update(worksheet)

def check_all(username):
    worksheet=sh.worksheet(username).get_all_values()
    pprint.pprint(worksheet,depth=4)

def login():
    global loggedin,quit
    while not loggedin:
        id=input("enter your id:(enter quit to quit)")
        if id=="quit":
            break
        password=getpass.getpass("enter your password:")


        for temp in range(len(accounts_sheet)):
            if id==accounts_sheet[temp][0]:
                if  bcrypt.checkpw(password,accounts_sheet[temp][1]) :
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
    same=True
    while same:
        username=input("please enter username:")
        userpassword=input("please enter password:")
        hashed = bcrypt.hashpw(userpassword, salt)
        accounts_sheet=sh.worksheet("accounts").get_all_values()
        for temp in range(len(accounts_sheet)):
            if username == accounts_sheet[temp][0]:
                print("username already in use, please change another one.")
                break
            elif temp ==len(accounts_sheet)-1:
                same=False
    sh.add_worksheet(title=username, rows="100", cols="4")
    worksheet=sh.worksheet(username)
    worksheet.update([["service","id","password","note"]])
    worksheet =sh.worksheet("accounts")
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
