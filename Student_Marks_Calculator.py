name = input('Enter Your Name:')                        #Giving Variable for Name of the Student

Sub_1 = int(input('Enter Your Marks for Subject 1 :'))  #Giving Variable For Subject 1

if ( Sub_1 > 100):
    print('Enter a number less then 100')               #Giving Condition, don't Run the the code if Sub_1 < 100
    exit()

elif ( Sub_1 < 0):                                      #Giving Condition, don't Run the the code if Sub_1 > 0
    print('Enter a Number Greater the 0')
    exit()

Sub_2 = int(input('Enter Your marks for Subject 2 :'))  #Giving Variable For Subject 1

if ( Sub_2 > 100):                                      #Giving Condition, don't Run the the code if Sub_2 < 100
    print('Enter a number less then 100')  
    exit()

elif ( Sub_2 < 0):                                      #Giving Condition, don't Run the the code if Sub_2 > 0
    print('Enter a Number Greater the 0')
    exit()

Sub_3 = int(input('Enter York marks for Subject 3 :'))  #Giving Variable For Subject 1

if ( Sub_3 > 100):                                      #Giving Condition, don't Run the the code if Sub_3 < 100
    print('Enter a number less then 100')
    exit()

elif ( Sub_3 < 0):                                      #Giving Condition, don't Run the the code if Sub_3 > 0
    print('Enter a Number Greater the 0')
    exit()
    
Total =  Sub_1 + Sub_2 + Sub_3

print("Enter Your Name :", name )
print("Your Total Marks are :", Total)
