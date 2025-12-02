###
# Functions to read any data type from the keyboard
#
def input_string(message):
    user_input = input(message)
    return user_input

def input_integer(message):
    user_input = input(message)
    return int(user_input)

def input_real(message):
    user_input = input(message)
    return float(user_input)

def input_boolean(message):
    user_input = input(message)
    return user_input.lower() == 'y'