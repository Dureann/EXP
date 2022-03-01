#functions

#variables
end = "y"
#main code
print("""
Welcome To
 __________   ___ ______   
|   ____\  \ /  /|   _   \  
|  |__   \  V  / |  |_)  | 
|   __|   >   <  |   ____/  
|  |____ /  _  \ |  |      
|_______/__/ \__\|__|      
 EXPv1.1.1
 Durian Technologies 2022
 By TR77""")
while (1 == 1):
    val_a = input("Your Value for a: ")
    val_x = input("Your expresion value (p/n) ")
    val_b = input("Your Value for b: ")
    val_t = input("Your Value for x: ")
    if val_x == "p":
        val_y = (float(val_a) * (1 + float(val_b)) ** float(val_t))
        print("Your valye for y is " + str(val_y))
    if val_x == "n":
        val_y = (float(val_a) * (1 - float(val_b)) ** float(val_t))
        print("Your value for y is \n" + str(val_y))
