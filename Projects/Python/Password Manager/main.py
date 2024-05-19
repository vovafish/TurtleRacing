master_pwd = input("What is the master password? ")


def view():
    with open("password.txt", "r") as f:
        for line in f.readlines():
            print(line.rstrip())



def add():
    name = input("Account name: ")
    pwd = input("Password: ")

    with open("password.txt", "a") as f:
        f.write(name + " | " + pwd + "\n")


while True:
    mode = input("Would you like yo add new password or view existing ones (view, add)? Press q ti quit ").lower()
    if mode == "q":
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode")
