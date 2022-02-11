
def get_initial(name):
    initial = name[0:1].upper()
    return initial

first_name = input('Enter your first name: ')
middle_name = input('Enter your middle name: ')
last_name = input('Enter your last name: ')

print('Your initials are: ' \
    + get_initial(first_name) \
    + get_initial(middle_name) \
    + get_initial(last_name))