from reception import reception
import pyttsx3

def afterlogin():

    print('1. Reception')
    print('2. Doctor')
    print('3. Biometric')
    print("4. Patient's Feedback")
    print('5. Pharmaceutical')
    print('6. Medical Test')
    print('7. Emergency')
    print('8. Helper')
    print('9. Logout')
    ch = input('What do you want to do? ')
    print("\n--------------------------------------------\n")

    if(ch == '1'):
        speech = pyttsx3.init()
        speech.setProperty("rate", 150)
        print("Welcome")
        print("Your Health is our Priority")
        print("\n--------------------------------------------\n")
        reception()
    
    elif(ch == '2'):
        pass

    elif(ch == '9'):
        return
    
    else:
        print("Wrong Input")
        print("\n--------------------------------------------\n")

    afterlogin()

              
