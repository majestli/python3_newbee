ab={
        'swaprop':'swaprop@swaroopch.com',
        'Larry':'larry@wall.org',
        'matsumoto':'matz@ruby-lang.org',
        'spammer':'spammer@hotmail.com'
}
print("swaroop's address is",ab['swaprop'])


del  ab['spammer']

print('\n There are {}contacts in the address-book\n'.format(len(ab)))


for name, address in ab.items():
    print('contact {} at {}'.format(name,address))
if 'Guido' in  ab:
    print("\n Guido's     address is ",ab['Guido'])
