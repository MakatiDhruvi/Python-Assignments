# for input comparision
Number_Dictionary = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

# TO get LCM
def Get_LCM(Number1, Number2):
   if Number1 > Number2:
       Greater = Number1
   else:
       Greater = Number2
   while True:
       if (Greater % Number1 == 0) and (Greater % Number2 == 0):
           LCM = Greater
           break
       Greater += 1
   return int(LCM)

# To get GCD
def Get_GCD(Numerator, Denominator):
    GCD = str(int(Numerator / Denominator))
    Number_Dictionary_Count = 0
    while Number_Dictionary_Count < len(Number_Dictionary):
        GCD = GCD.replace(str(Number_Dictionary_Count), Number_Dictionary[Number_Dictionary_Count])
        Number_Dictionary_Count += 1
    return GCD

# To get input from user
Number1 = input("Enter First Number:").replace(" ", "")
Number2 = input("Enter Second Number:").replace(" ", "")
Number_Dictionary_Count = 0
while Number_Dictionary_Count < len(Number_Dictionary):
    Number1 = Number1.replace(Number_Dictionary[Number_Dictionary_Count], str(Number_Dictionary_Count))
    Number2 = Number2.replace(Number_Dictionary[Number_Dictionary_Count], str(Number_Dictionary_Count))
    Number_Dictionary_Count += 1
Number1 = int(Number1)
Number2 = int(Number2)

# To get final result
print(Get_GCD(Number1 * Number2, (Get_LCM(Number1, Number2))))
