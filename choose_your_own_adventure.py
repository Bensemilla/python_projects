print('(Insert Story which ends in choice of left through narrow alley or right through gardens)')
choice = input()
while choice != 'left' and choice != 'right':
    print('please choose left or right')
    choice = input()
    if choice == 'left' and choice == 'right':
        break
if choice == 'left':
    print('(Insert story through narrow alley)')
elif choice == 'right':
    print('(Insert story through gardens)')
