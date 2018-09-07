number =23
running = True

while running:
    guess = int(input('Enter an interger:'))
    if guess == number:
        print('ok you guessed it')
        print('but you donot win any prizes!')
        running=False
    elif guess < number:
        print('NO, it is a little higher than that')
    else:
        print('NO,it is  a little lower than that')
else:
        print('the while loop is over.')
print('Done')


for i  in range(1,5):
    print(i)
else:
    print('The for loop is over')


while True:
    s=input('enter someting:')
    if s=='quit':
        break
    print('len of the string is',len(s))
print('done')
