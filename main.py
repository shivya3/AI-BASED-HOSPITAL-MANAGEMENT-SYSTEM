from afterlogin import afterlogin

print("\n--------------------------------------------\n")
def main():
    print("Welcome!!!!")
    print("We will help you Manage your Hospital")
    print("As per your Needs")
    print("\n--------------------------------------------\n")
    
    print("1. Login")
    print("2. Exit")
    ch = input("Login as: ")
    print("\n--------------------------------------------\n")
    
    if(ch == "1"):
        user = input("Enter Username: ")
        passw = input("Enter Password: ")

        if(user == 'A' and passw == 'S'):
            print("\n--------------------------------------------\n")
            print('Login Successful')
            print("\n--------------------------------------------\n")
            afterlogin()
            
        else:
            print("\n--------------------------------------------\n")
            print('Either Username or Password is Wrong')
            print("\n--------------------------------------------\n")
       
    elif(ch == "2"):
        print("Thank you for Using letting me Help you")
        print("Have a Nice Day")
        print("\n--------------------------------------------")
        return
        
    else:
        print("Wrong Input")
        print("\n--------------------------------------------\n")
        
    main()
    
if __name__ == "__main__":
    main()
