from collections import defaultdict
List_Of_Items = []
LimitPassed = False

# To get input from user
Data = input("Insert data in comma(,) separate: ")
if len(Data) < 1 or len(Data) > 104:
    print("Data must be between 1 to 104")
    LimitPassed = True
    
# Check limit passed or not
if LimitPassed == False :
    Count = 0
    # Split data of given input
    for i in Data.split(",") :
        if len(i.strip()) >= 0 and len(i.strip()) <= 100 and LimitPassed == False:
            List_Of_Items.insert(Count, i.strip())
        else :
            LimitPassed = False
        Count += 1
    # Check limit passed or not
    if LimitPassed == False :
        Temp_List = defaultdict(list)
        for Item in List_Of_Items:
            #Add data in array with group
            Temp_List[str(sorted(Item))].append(Item)
        Result = list(Temp_List.values())
        print(str(Result))
    else :
        print("Per string data must be between 0 to 100")