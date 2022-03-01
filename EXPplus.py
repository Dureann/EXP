#EXPplus
#Intro
print("""
Welcome To
 __________   __________          
|   ____\  \ /  /|   _   \   _   
|  |__   \  V  / |  |_)  | _| |_ 
|   __|   >   <  |   ____/|_   _|
|  |____ /  _  \ |  |       |_|  
|_______/__/ \__\| _|             
 EXPplusv1.0.9
 Durian Technologies 2022
 By TR77""")
#While
while 1 == 1:
#Function Type
    ftyp = input("""Function type
    "e" = Exponential Function
    "l" = Linear Function""")
    if ftyp == "e":
        expon()
    if ftyp == "l":
        line()
#Linear Functions
        def line():
            print("New Equasion:------")
            al_m2 = input("Your Value for a: ")
            val_x2 = input("Your expresion value (p/n) ")
            val_b2 = input("Your Value for b: ")
            val_y2 = ((float(val_m2) * float(val_x2)) + float(val_b2))
            print("Your valye for y is " + str(val_y2))
#Exponential Fucntions
        def expon():
            print("New Equasion:------")
            val_a = input("Your Value for a: ")
            val_x = input("Your expresion value (p/n) ")
            val_b = input("Your Value for b: ")
            al_t = input("Your Value for x: ")
            if val_x == "p":
                val_y = (float(val_a) * (1 + float(val_b)) ** float(val_t))
                print("Your valye for y is " + str(val_y))
            if val_x == "n":
                val_y = (float(val_a) * (1 - float(val_b)) ** float(val_t))
                print("Your value for y is" + str(val_y))
