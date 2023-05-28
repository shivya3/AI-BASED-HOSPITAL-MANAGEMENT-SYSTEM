import cv2 as cv
from tabulate import tabulate

import datetime as dt
x = dt.datetime.now()

import mysql.connector as ms
mycon = ms.connect(host='localhost', user='root', db='medic', passwd='Shivya6565@')
cur1 = mycon.cursor()

import pyttsx3
speech = pyttsx3.init()
speech.setProperty("rate", 150)


def appointment(doctor,a):

    if(a == 1):
        print(' 1. Cardiologist')    
        print(' 2. Radiologist')    
        print(' 3. Ophthalmologist')   
        print(' 4. Dentist')     
        print(' 5. Ent_Specialist')  
        print(' 6. Gynaecologist')
        print(' 7. Orhtopedic')   
        print(' 8. PediatricianN')  
        print(' 9. Psychiatrist')   
        print('10. Pulmonologist')  
        print('11. Endocrinologist') 
        print('12. Dermatolosist')  
        print('13. Oncologist')      
        print('14. Neurologist')
        print('15. General Physician')
        print('16. Back')
        ch2 = input('Pick your specialist: ')
        print("\n--------------------------------------------\n")


        if(ch2 == '1'):
            doctor = 'cardiologist'

        elif(ch2 == '2'):
            doctor = 'radiologist'

        elif(ch2 == '3'):
            doctor = 'opthalmologist'

        elif(ch2 == '4'):
            doctor = 'dentist'

        elif(ch2 == '5'):
            doctor = 'ent_specialist'

        elif(ch2 == '6'):
            doctor = 'gynaecologist'

        elif(ch2 == '7'):
            doctor = 'orthopedic'

        elif(ch2 == '8'):
            doctor = 'pediatrician'

        elif(ch2 == '9'):
            doctor = 'psychiatrist'

        elif(ch2 == '10'):
            doctor = 'pulmonologist'

        elif(ch2 == '11'):
            doctor = 'endocrinologist'

        elif(ch2 == '12'):
            doctor = 'dermatologist'

        elif(ch2 == '13'):
            doctor = 'oncologist'

        elif(ch2 == '14'):
            doctor = 'neurologist'
        

        elif(ch2 == '15'):
            doctor = 'general physician'

        elif(ch2 == '16'):
            return
            
        else:
            print("Wrong Input")
            print("\n--------------------------------------------\n")
            appointment(doctor,1)

    sql = 'select name,speciality,tot_appoint,cur_patient from daily where speciality = %s'
    data = [doctor]
    cur1.execute(sql,data)
    result = cur1.fetchall()
    
    while(True):
        print('Following doctors have specialisation in',doctor,'->')
        keys = ['Name','Speciality','Total Appointments','Current Patients']
        print(tabulate(result, headers = keys, tablefmt = 'pretty',showindex = False))
        ch = input('Which doctor do you want?(1/2) ')
        
        if(ch == '1'):
            special = result[0][0]
            break

        elif(ch == '2'):
            special = result[1][0]
            break

        else:
            print('Wrong Input')
            print("\n--------------------------------------------\n")
            
    print("\n--------------------------------------------\n")
    record(doctor,special)


def record(doctor,special):

    while(True):
        f_name = input("Enter patient's First name: ")
        l_name = input("Enter patient's Last name: ")
        print("\n--------------------------------------------\n")
        print("Patient's Full Name: "+f_name+" "+l_name)
        print("\n--------------------------------------------\n")
        ch = input('Is your Name correct?(y/n) ')
        print("\n--------------------------------------------\n")
        if(ch.lower() == 'y'):
            break

    while(True):
        try:
            age = int(input("Enter patient's age: "))
            print("\n--------------------------------------------\n")
            if(age > 130):
                print('Invalid Age')
                print("\n--------------------------------------------\n")
                continue

        except:
            print("\n--------------------------------------------\n")
            print('Wrong Input, Try Again')
            print("\n--------------------------------------------\n")

        else:
            print("Patient's age is: ",age)
            print("\n--------------------------------------------\n")
            ch = input('Is your Age correct?(y/n) ')
            print("\n--------------------------------------------\n")
            if(ch.lower() == 'y'):
                break
            
    date = str(x.day) + '-' + str(x.month) + '-' + str(x.year)
    time = str(x.hour) + ':' + str(x.minute) + ':' + str(x.second)


    while(True):
        try:
            c_code = int(input("Enter your country code +"))
            phone_no = input("Enter your phone_no: ")
            print("\n--------------------------------------------\n")

        except:
            print("\n--------------------------------------------\n")
            print('Wrong Input, Try Again')
            print("\n--------------------------------------------\n")

        else:
            phone_no = '+' + str(c_code) + str(phone_no)
            print("Patient's Phone Number is:",phone_no)
            print("\n--------------------------------------------\n")
            ch = input('Is your Phone Number correct?(y/n) ')
            print("\n--------------------------------------------\n")
            if(ch.lower() == 'y'):
                break

    
    sql = '''insert into record
            (f_name,l_name,age,phone_no,spec,spec_name,date,time)
             values(%s,%s,%s,%s,%s,%s,%s,%s)'''
    data = [f_name,l_name,age,phone_no,special,doctor,date,time]
    cur1.execute(sql,data)
    mycon.commit()

    sql = '''update daily
             set tot_appoint = tot_appoint + 1
             where name = %s'''
    data = [special]
    cur1.execute(sql,data)
    mycon.commit()
    
    print('Appointment is Successfully Made')
    print("\n--------------------------------------------\n")

def payment():
    print('1. Cash Payment')
    speech.say('Press one for payement in cash')
    speech.runAndWait()
    
    print('2. Online Payment')
    speech.say('Press two for online payment')
    speech.runAndWait()

    speech.say('What do you want to do?')
    speech.runAndWait()
    ch = input('What do you want to do?(1/2) ')
    print("\n--------------------------------------------\n")
    
    if(ch == '1'):
        speech.say('Enter payment successful password')
        speech.runAndWait()
        pass1 = input('Enter payment successful password ')
        print("\n--------------------------------------------\n")
    
        if(pass1 == 'A'):
            print('Payment Successful')
            speech.say('payment successful')
            speech.runAndWait()
            print("\n--------------------------------------------\n")
            return 1
            
        else:
            print('Wrong Password. TRY AGAIN!!!')
            print("\n--------------------------------------------\n")
            speech.say('wrong password. try again')
            speech.runAndWait()
            payment()
           
        
    elif(ch == '2'):
        img = cv.imread('QR_code.png',1)
        cv.imshow('image',img)
        cv.waitKey(2000)            
        cv.destroyWindow('image')
        print('Payment Successful')
        speech.say('payment successful')
        speech.runAndWait()
        print("\n--------------------------------------------\n")
        return 1
