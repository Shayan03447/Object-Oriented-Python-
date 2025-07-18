class chatbook:
    __user_id=0
    def __init__(self):
        self.id=chatbook.__user_id
        chatbook.__user_id+=1
        
        self.__name='Default user'
        self.username=""
        self.password=""
        self.loggedin=False
        #self.menu()

    def get_name(self):
        return self.__name
    def set_name(self, value):
        self.__name=value
    
    def menu(self):
        user_input=input("""Welcome to the Chatbook !! How would you like to proceed?
                         1. Press 1 to signup
                         2. Press 2 to signin
                         3. Press 3 to write a post
                         4. press 4 to message a friend
                         5. press any other key to exit
                         
                         -> """)
        if user_input=="1":
            self.signup()
        elif user_input=="2":
            self.signin()
        elif user_input=="3":
            self.my_post()
        elif user_input=="4":
            self.sendmsg()
        else:
            exit

    def signup(self):
        email=input("Enter your email here ->")
        pwd=input("Setup your password here ->")
        self.username=email
        self.password=pwd
        print("You have signed up successfully !!")
        print("\n")
        self.menu() 

    def signin(self):
        if self.username=="" and self.password=="":
            print("please signup first by pressing 1 in the main menu")
        else:
            username=input("enter your email/username here ->")
            pwd=input("Enter your password here ->")
            if self.username==username and self.password==pwd:
                print("You have signed in successfully !!")
                self.loggedin=True
            else:
                print("please enter correct credential")
        print("\n")
        self.menu()

    def my_post(self):
        if self.loggedin==True:
            txt=input("Enter your message here ->")
            print(f"following content has been posted -> {txt}")
        else:
            print("You need to signin first to post something....")
        print("\n")
        self.menu()
    
    def sendmsg(self):
        if self.loggedin==True:
            txt=input("Enter your message here ->")
            friend=input("whom to send the message? ->")
            print(f"your message has been send to {friend}")
        else:
            print("You need to signin first to send the message")
        print("\n")
        self.menu()

        

    




object=chatbook()

