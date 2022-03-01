#functions

#variables
end = "y"
#main code
print("""
Welcome To
 __________   __________          
|   ____\  \ /  /|   _   \     _   
|  |__   \  V  / |  |_)  |   _| |_ 
|   __|   >   <  |   ____/  |_   _|
|  |____ /  _  \ |  |         |_|  
|_______/__/ \__\| _|             
 EXPplusv1.0.1
 Durian Technologies 2022
 By TR77""")
while (end != "z"):
    end = val_a = input("Your Value for a: ")
    end = val_x = input("Your expresion value (p/n) ")
    end = val_b = input("Your Value for b: ")
    end = val_t = input("Your Value for x: ")
    if val_x == "p":
        val_y = (float(val_a) * (1 + float(val_b)) ** float(val_t))
        print("Your valye for y is " + str(val_y))
    if val_x == "n":
        val_y = (float(val_a) * (1 - float(val_b)) ** float(val_t))
        print("Your value for y is \n" + str(val_y))
    input("New equasion? (y/n): ")
        if input == "y":
            print("----------")
        if input == "n":
            