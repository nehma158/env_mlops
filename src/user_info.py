import re

# get email from user input
def get_email_from_input():
    """ 
    Contains '@' and '.' 
    """
    email = input("Tell me your email: ")

    if ("@" not in email or "." not in email):
        print('Email is not valid.')
    else:
        return email

# get name from user input        
def get_name_from_input():
    """ 
    Not empty string. No spaces. 
    """
    name = input("Create your user name: ")
    
    if (' ' in name):
        print('Name not valid, should not have spaces')
    else:
        return name

# get password from user input
def get_password_from_input():
    """ 
    Password needs to be at least 8 characters long with at least one number, one special character and one letter. 
    """
    # ask the user to enter password
    password = input("Create your password: ")
        
    # to check if there is a special character in the password
    string_check= re.compile('[@_!#$%^&*()<>?/\|}{~:]')

    if len(password)<8:
        # if the password doesn't contain 8 characters
        print('Invalid password: Password needs to be at least 8 characters long with at least one number, one special character and one letter.')
    elif not list(filter(lambda c: c.isupper(), password)) :
        # if there is no uppercase
        print('Invalid password: Password needs to be at least 8 characters long with at least one number, one special character and one letter.')
    elif string_check.search(password) == None:
        # if there is no special character 
        print('Invalid password: Password needs to be at least 8 characters long with at least one number, one special character and one letter.')
    elif not re.findall('[0-9]+', password):
        # if there is no digit
        print('Invalid password: Password needs to be at least 8 characters long with at least one number, one special character and one letter.')
    else:
        return password
    
    
    
    