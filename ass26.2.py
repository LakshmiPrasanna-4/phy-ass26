# Write a program to identify the file format.

file=input()
if file.endswith('.jpeg'):
    print('Photo Document')
elif file.endswith('.doc'):
    print('Word Document')
elif file.endswith('.xls'):
    print('Excel Document')
elif file.endswith('.ppt'):
    print('Powerpoint Document')
else:
    print('Invalid Document')
