def greeting():
    print('Welcome to the Launch Console!')
    name = input('What is your name? ')
    print(f'\nHi, {name}!')

def menu():
    running = True
    while running == True:
        print("\n1. About me \n2. My goals \n3. Fun fact \n4. Exit")
        choice = input('\npick 1, 2, 3, or 4: ')
        if choice == '1':
            print('\nI have a strong curiosity for programming and engineering, and I like exploring how technology can be used to solve problems.')
        elif choice == '2':
            print('\nI hope to create an original app that people can find useful.')
        elif choice == '3':
            print('\nOutside of programming and engineering, I enjoy playing basketball!')
        elif choice == '4':
            print('\nGoodbye!')
            running = False
        else:
            print('\nPlease pick one of the options (1, 2, 3, or 4).)')

greeting()
menu()