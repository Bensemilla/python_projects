print('(Insert Story which ends in choice of left through narrow alley or right through gardens)')
choice = input()
if choice == 'left':
    print('(Insert story through narrow alley)')
elif choice == 'right':
    print('(Insert story through gardens)')
elif choice != ('left' or 'right'):
    print('please choose left or right')
