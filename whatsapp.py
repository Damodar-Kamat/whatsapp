
import json

class Chat:
    def __init__(self, name):
        self.name = name
        self.ch = input("1. Send message\n2. display messages\n3. Login using other account\n0. Exit\n\nEnter your choice: ")
        if self.ch == '1':
            self.chatmsg = input("Type Message: ")
            try:
                with open('chats.txt', 'a') as f:
                    f.write(name + ': '+self.chatmsg)
                    f.write('\n')
                    f.close()
            except:
                print("error in sending message!!")
            finally:
                try:
                    f.close()
                except:
                    pass
            self.ch = input("Enter 1 to continue: ")
            if self.ch == '1':
                Chat(self.name)
            else:
                print("logged out!!")
                exit(0)
        if self.ch == '2':
            display=display_messages()
            display.display(self.name)
        if self.ch == '3':
            users=login()
            users.login_user()
        elif self.ch == '0':
                print("logged out!!")
                exit(0)

class Message:
    def __init__(self, sender, body):
        self.sender = sender
        self.body = body
        if self.sender == 'Whatsapp':
            self.sender = 'Whatsapp'
        else:
            self.sender = 'Me'
        self.body = body

class display_messages:
    def __init__(self):
        pass
    def display(self, name):
        self.name = name
        try:
            with open('chats.txt', 'r') as f:
                chats = f.readlines()
                for chat in chats:
                    if chat.split(':')[0] == self.name:
                        print(chat)
                    else:
                        print("\t\t\t\t"+chat.split(':')[0] + ': ' + chat.split(':')[1])
        except FileNotFoundError:
            print("nothing to display")
        finally:
            try:
                f.close()
            except:
                pass

class register:
    def newuser(self):
        self.name = input('Enter your user name: ')
        self.password = input('Enter your user password: ')
        self.account = {'name': self.name, 'password': self.password}
        try:
            with open('users.json', 'r') as f:
                users = json.load(f)
                for user in users:
                    if user['name'] == self.name:
                        print('account already exist')
                        exit(0)
        except:
            pass
        closefile()
        try:
            with open('users.json', 'r') as f:
                users = json.load(f)
                users.append(self.account)
                f.close()
        except FileNotFoundError:
            with open('users.json', 'w') as f:
                users = [self.account]
                f.close()
        closefile()
        with open('users.json', 'w') as f:
            json.dump(users, f)
            f.write('\n')
            closefile()
        print('account created')
        
class login:
    def login_user(self):
        self.name = input('Enter your user name: ')
        self.password = input('Enter your user password: ')
        with open('users.json', 'r') as f:
            users = json.load(f)
            for user in users:
                if user['name'] == self.name and user['password'] == self.password:
                    print('Login successfully')
                    while True:
                        chat=Chat(self.name)
                    break
        closefile()
                
def closefile():
    try:
        pass
    finally:
            try:
                f.close()
            except:
                pass


while True:
    ch = input('1. create new account\n2. Login to account\n3. Exit\n\n Enter your choice: ')
    if ch == '1':
        users=register()
        users.newuser()
    elif ch == '2':
        users=login()
        users.login_user()
    elif ch == '3':
        print("logged out!!")
        users.closefile()
        exit(0)