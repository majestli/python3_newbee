name = 'swaroop'

if name.startswith('Swa'):
    print('Yes, the string starts with "swa"')
if 'a' in name:
    print('Yes,it contains the string "a"')
if name.find('war') != -1:
    print('Yes,it contains the string "war"')


delimiter='_*_'
mylist=['brazil','russia','india','china']
print(delimiter.join(mylist))
