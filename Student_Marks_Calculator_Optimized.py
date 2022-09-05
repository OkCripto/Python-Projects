name = input('Enter Your Name:')                        

L_100 = str('Enter a number less then 100')
G_0 = str('Enter a number Greater then 0')

Sub_1 = int(input('Enter Your Marks for Subject 1 :'))  

if ( Sub_1 > 100):
    print( L_100 )              
    exit()

elif ( Sub_1 < 0):                                      
    print( G_0 )
    exit()

Sub_2 = int(input('Enter Your marks for Subject 2 :'))  

if ( Sub_2 > 100):                                     
    print( L_100 )  
    exit()

elif ( Sub_2 < 0):                                    
    print( G_0 )
    exit()

Sub_3 = int(input('Enter York marks for Subject 3 :'))  

if ( Sub_3 > 100):                                      
    print( L_100 )
    exit()

elif ( Sub_3 < 0):                                      
    print( G_0 )
    exit()
    
Total =  Sub_1 + Sub_2 + Sub_3

print("Enter Your Name :", name )
print("Your Total Marks are :", Total)

