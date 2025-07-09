class ChatBook:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.loggedIn = False
        self.menu()

    def menu(self):
        user_input = input('''WelCome to our app!!! go through the following options
        1. Press 1 for signUp.
        2. Press 2 for signIn.
        3. Press 3 for writing the Post.
        4. Press 4 for sending the Message.
        5. Press any key to exit.
        
        -->
        ''')
        if user_input == '1':
            self.signUp()
        elif user_input == '2':
            self.signIn()
        elif user_input == '3':
            self.postContent()
        elif user_input == '4':
            self.sendMessage()
        else:
            exit()

    def signUp(self):
        userName = input('Enter Your UserName: ')
        pwd = input('Set your Password : ')

        self.username  = userName
        self.password = pwd

        print('You Signed Up Successfully!!! Now press 2 for Sign In.')
        print('\n')
        self.menu()

    def signIn(self):
        if self.username == '' and self.password == '':
            print('Press 1 to signup first!!!')
            print('\n')
            self.menu()
        else:
            userName = input('Enter Your UserName : ')
            pwd = input('Enter your Password : ')

            if self.username == userName and self.password == pwd:
                print('Signed In Successfully!!!')
                self.loggedIn = True
                print('\n')
                self.menu()
            else:
                print('Invalid Username or Password... Try Again!!!')
                print('\n')
                self.menu()

    def postContent(self):
        if self.loggedIn:
            text = input("Write your Post here ->  ")
            print(f'Your Current Post->  {text}')
            print('\n')
            self.menu()
        else:
            print('Press 2 to SignIn first')
            print('\n')
            self.menu()

    def sendMessage(self):
        if self.loggedIn:
            msg = input("Write your msg here ->  ")
            frnd = input("Write the name of your friend: ")
            print(f'Your message :"{msg}" is sent to your friend -> {frnd} successfully...')
            print('\n')
            self.menu()
        else:
            print('Press 2 to SignIn first')
            print('\n')
            self.menu()


user1 = ChatBook()