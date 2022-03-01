#functions

#variables
end = "y"
#main code
print("""
Welcome To
 __________   ___ .______   
|   ____\  \ /  / |   _  \  
|  |__   \  V  /  |  |_)  | 
|   __|   >   <   |   ___/  
|  |____ /  .  \  |  |      
|_______/__/ \__\ | _|      
 EXP for TI84+CE Python v1.0.7; Beta
 Durian Technologies 2022
 By TR77
 """)
while (end != "z"):
    end = val_a = input("Your Value for a:")
    end = val_x = input("Your expresion value (p/n)")
    end = val_b = input("Your Value for b:")
    end = val_t = input("Your Value for x:")
    if val_x == "p":
        val_y = (float(val_a) * (1 + float(val_b)) ** float(val_t))
        print("Your valye for y is " + str(val_y))
    if val_x == "n":
        val_y = (float(val_a) * (1 - float(val_b)) ** float(val_t))
        print("Your valye for y is " + str(val_y))