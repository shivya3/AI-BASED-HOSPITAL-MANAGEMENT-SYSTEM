from appointment import appointment

import pyttsx3
speech = pyttsx3.init()
speech.setProperty("rate", 150)
        
import mysql.connector as ms
mycon = ms.connect(host='localhost', user='root', db='medic', passwd='Shivya6565@')
cur1 = mycon.cursor()

def reception():
    print('1. Book a Appointment')
    print('2. Logout')
    ch = input('What do you want to do? ')
    print("\n--------------------------------------------\n")
    
##    if(ch == '1'):
##        img = cv.imread('map_hospital.jpg',1)
##        cv.imshow('image',img)
    
    if(ch == '1'):
        print('How may I help you Today?')
        speech.say("How may i help you today?")
        speech.runAndWait()
        doctor = preprocessing()
        booking(doctor)
        
    elif(ch == '2'):
        outpass = 'D'
        ch2 = input('Enter Logout Password: ')
        
        if(ch2 == 'D'):
            print("\n--------------------------------------------\n")
            print('Logout Successful')
            print("\n--------------------------------------------\n")
            return

        else:
            print("\n--------------------------------------------\n")
            print('Logout Failed')
            print("\n--------------------------------------------\n")
                    
    else:
        print("Wrong Input")
        print("\n--------------------------------------------\n")

    reception()

def preprocessing():
    
    listen = input("I am listening: ")
    print("\n--------------------------------------------\n")
    listen = listen.lower()
    listen = listen.replace(".","")
    listen = listen.replace("?","")
    listen = listen.replace(",","")
    listen = listen.replace("!","")
    l = listen.split()
    i = 0
    while(i<len(l)):
        if(len(l[i])<3):
            l.pop(i)
        else:
            i+=1
            
    sql = 'select * from keywords'
    cur1.execute(sql)
    result = cur1.fetchall()
    
    for i in result:
        for j in l:
            if(i[1] == j):
                doctor = i[2]
                break
        else:
            continue
        break

    else:
        doctor = 'general physician'

    return doctor


def booking(doctor):

    print('I think you should go to ' + doctor)
    speech.say('I think you should go to ' + doctor)
    speech.runAndWait()
    print("\n--------------------------------------------\n")
    
    print('1. To book appointment for '+ doctor)
    speech.say('Press one to book an appointment for' + doctor)
    speech.runAndWait()
    print('2. Show all the available Specialist')
    speech.say('Press two to see all the available specialist')
    speech.runAndWait()
    print('3. Back')
    speech.say('press three to return to previous page')
    speech.runAndWait()
    ch = input('What do you want to do? ')
    print("\n--------------------------------------------\n")
    
    if(ch == '1'):
        appointment(doctor,0)

    elif(ch == '2'):
        doctor = appointment('No One',1)
        

    elif(ch == '3'):
        return

    else:
        print("Wrong Input")
        print("\n--------------------------------------------\n")
   
