import random

'''
 Dummy reference user id generator
'''
def create_user_reference():
    prefix = ''.join((random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')) for x in range(2))
    postfix = random.randint(0,100000)
    return prefix + "-"+ str(postfix)

def validate_user(user):
    if user and len(user) > 5:
        return True
    return False

def validate_dob(dob):
    pass

def validate_address(address):
    pass

def validate_phone(phone):
    pass

