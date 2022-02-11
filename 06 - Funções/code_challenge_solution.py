def calculator(first_number, second_number, operation='ADD'):
    if operation.upper() == 'ADD':
        return(float(first_number) + float(second_number))
    elif operation.upper() =='SUBTRACT':
        return(float(first_number) - float(second_number))
    else:
        return('Invalid operation please specify ADD or SUBTRACT')
 
print('Adding 6 + 4 = ' + str(calculator(first_number=6, second_number=4)))
print('Subtracting 6 - 4 = ' + str(calculator(first_number=6, second_number=4, operation='subtract')))


# def calculator(first_number, second_number, operation):
#     if operation.upper() == 'ADD':
#         return(float(first_number) + float(second_number))
#     elif operation.upper() =='SUBTRACT':
#         return(float(first_number) - float(second_number))
#     else:
#         return('Invalid operation please specify ADD or SUBTRACT')
 
# #
# print('Adding 6 + 4 = ' + str(calculator(6,4,'add')))
 
# print('Subtracting 6 - 4 = ' + str(calculator(6,4,'subtract')))
 
# print('Dividing 6 / 4 = ' + str(calculator(6,4,'divide')))