def get_sftp():
    print('start sftp')

def regist(name, sex, *args):
    print(f"name: {name})")
    print(f"sex: {sex}")
    print(f"args: {args}")

def regist2(name, sex, *args, **kwargs):
    print(f"name: {name})")
    print(f"sex: {sex}")
    print(f"args: {args}")
    email = kwargs.get("email") or None
    phone = kwargs.get("phone") or None
    if email:
        print(f"email: {email}")
    if phone:
        print(f"phone: {phone}")

