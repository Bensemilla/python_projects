print('You ran after the suspect for five blocks now and your lungs start to burn but you cant let them escape, the information they hold might be too useful. Suddenly your foot hits something solid on the ground and you start to stumble. As you catch yourself and look up again you cant see the suspect anymore. You run up to the spot where you last saw them and look around. You see two possible ways they could have gone: over the fence to the right through the gardens or down a narrow alley to the left. Which way are you taking, left or right?')
choice = input()
if not choice == 'left''right':
    print('please choose left or right')
if choice == 'left':
    print('(Insert story through narrow alley)')
if choice == 'right':
    print('(Insert story through gardens)')
