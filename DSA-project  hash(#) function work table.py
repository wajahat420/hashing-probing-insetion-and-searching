
dataCollect =  {0: {"key": 73 ,'name' : "Ukasha", "Roll number":  105}, 1: {"key" :  146 ,'name' : "saad", "Roll number": 92}, 2: {"key": 75 ,'name' : "anas", "Roll number": 94}, 3: {"key": 149 ,'name' : "wajahat", "Roll number":  79}, 4: {"key": 219 ,'name' : "immu Bhai", "Roll number": 102  }, 5: {}, 6: {}, 7: {}, 8: {}, 9: {}, 10: {}, 11: {}, 12: {}, 13: {}, 14: {}, 15: {}, 16: {}, 17: {}, 18: {}, 19: {}, 20: {}, 21: {}, 22: {}, 23: {}, 24: {}, 25: {}, 26: {}, 27: {}, 28: {}, 29: {}, 30: {}, 31: {}, 32: {}, 33: {}, 34: {}, 35: {}, 36: {}, 37: {}, 38: {}, 39: {}, 40: {}, 41: {}, 42: {}, 43: {}, 44: {}, 45: {}, 46: {}, 47: {}, 48: {}, 49: {}, 50: {}, 51: {}, 52: {}, 53: {}, 54: {}, 55: {}, 56: {}, 57: {}, 58: {}, 59: {}, 60: {}, 61: {}, 62: {}, 63: {}, 64: {}, 65: {}, 66: {}, 67: {}, 68: {}, 69: {}, 70: {}, 71: {}, 72: {}, 73: {}, 74: {}}



#Loop For Insertion

print(dataCollect,"\n")
for i in range(0,2):
    key = int(input("Enter key:  \t "))
    name = input("Enter name: \t")
    rollNo = int(input("Enter Roll Number: \t"))

    mod = key % 73
    count  = 1

    while len(dataCollect[mod]) != 0:
        if mod == 72:
            mod = -1
        count += 1
        mod += 1

    dataCollect[mod] = {"key": key ,'name' : name, "Roll number": rollNo}
    print("Number Of Probes For Insertion are: ",count ,"\n")
    print(dataCollect,"\n")

# Loop For Searching

for i in range(0,5):
    
    found = False
    key = int(input("Which value you have to search For.. \n Please enter the key \t "))
    mod = key % 73
    count = 1

    
    while len(dataCollect[mod]) != 0:
            if key == dataCollect[mod]["key"]:
                found = True
                break
            if mod == 72:
                mod = -1
            mod += 1
            count += 1
            
    if found :
        print("Successful Search \n Number Of Probes For Searching are: ",count, "probe(s) and item is on", mod,"\n" )
    else:
        print("Unsuccessful Search \n Number Of Probes  are: ",count,"\n")





    
