#EXPplus
#Imports
import time
    #Functions
#Linear Functions
def line():
    print("Div Line:------")
    val_m2 = input("Your Value for a: ")
    val_x2 = input("Your Value for x: ")
    val_b2 = input("Your Value for b: ")
    val_y2 = ((float(val_m2) * float(val_x2)) + float(val_b2))
    print("Your valye for y is " + str(val_y2))
#Exponential Fucntions
def expon():
    print("Div Line:------")
    val_a = input("Your Value for a: ")
    val_b = input("Your Value for b: ")
    val_t = input("Your Value for x: ")
    val_y = (float(val_a) * (float(val_b)) ** float(val_t))
    print("Your valye for y is " + str(val_y))
#Intro
print("""
Welcome To
 __________   __________          
|   ____\  \ /  /|   _   \   _   
|  |__   \  V  / |  |_)  | _| |_ 
|   __|   >   <  |   ____/|_   _|
|  |____ /  _  \ |  |       |_|  
|_______/__/ \__\| _|             
 EXPplusv1.1.6
 Durian Technologies 2022
 By TR77""")
time.sleep(1.5)
#While
while 1 == 1:
#Function Type
    ftyp = input("""Div Line:------
    Function type
    "q" = Quit Program
    "e" = Exponential Function (y=a(b)^x)
    "l" = Linear Function (y=mx+b)
    Input: """)
    if ftyp == "q":
        quit()
    if ftyp == "e":
        expon()
    if ftyp == "l":
        line()
