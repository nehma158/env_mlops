def is_palindrom(my_string):
    '''
    Test if my_string is a palindrom
    '''
    if my_string[::-1] == my_string:
        return True
    else:
        return False