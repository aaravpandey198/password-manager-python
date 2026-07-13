def view():
    f=open("password.txt","r")
    print("========================================================")
    for line in f.readlines():
        data=line.rstrip()
        user,passwd=data.split("||")
        print("account name:",user + " , password:",passwd)
        print("========================================================")

    f.close()

def add():
    acc=input("enter account name: ")
    passw=input("enter the pass word: ")
    with open("password.txt","a") as f:
    f.write(acc + "||" + passw +"\n")
    


with open("master.txt", "r") as f:
    saved_password = f.read().strip()

master_password = input("Enter master password: ")

if master_password != saved_password:
    print("Wrong password!")
    exit()

else:

    while True:
        mode=input("what would you like to do?\n(view(v)/add(a)/quit(q))").lower()
        if mode=='q':
            break
        elif mode=='a':
            add()
        elif mode=='v':
            view()
        else:
            print("enter valid character.")




