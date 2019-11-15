import json

def get_user_name():
    
    try:
        filename = 'username.json'
        with open(filename, 'r') as f_obj:
            username = json.load(f_obj)
    except:
        return None
    else:
        return username

def greet_user():
    username = get_user_name()
    if username:
        print('Welcome back, '+ username+'!')
    else:
        username = input('Enter Username: ')
        filename = 'username.json'
        with open(filename, 'w') as fw_obj:
            json.dump(username, fw_obj)
            print("We'll remember you when you come back, "+username)

greet_user()