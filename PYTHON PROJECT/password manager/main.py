

def add():
    Name = input("Account name: ")
    pwd = input("password: ")
    with open('password.txt', 'a')as p:
      p.write(Name+" | "+pwd+"\n")


def view():
    with open('password.txt','r')as p:
        for lines in p:

            print(lines)
           


while True:
    mode = input("Would you like to add new password or view existing one(add/view) or press 'q' to quit: ").lower()

    if mode == "q":
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invailed choice!")
        continue