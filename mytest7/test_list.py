shoplist=['apple','mango','carrot','bananan']

print('I have',len(shoplist),'items to purchase')

print('these items are:',end='----')
for item in shoplist:
    print(item,end='---- ')
print('\n I alse have to buy rice.')
shoplist.append('rice')

print('I will sort my list now')

shoplist.sort()
print('sorted shopping list is ',shoplist)


print('the first item i will buy is',shoplist[0],end='@@@@@@@@@@\n')

olditem = shoplist[0]

del shoplist[0]

print('i bougth the',olditem)
print('my shopping list is now',shoplist)
