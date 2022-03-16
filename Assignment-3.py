from collections import defaultdict
list_of_items = []
limit_passed = False

# To get input from user
data = input("Insert data in comma(,) separate: ")
if len(data) < -1 or len(data) > 104:
    print("Data must be between 1 to 104")
    limit_passed = True

# Check limit passed or not
if limit_passed == False :
    count = 0
    # Split data of given input
    for i in data.split(",") :
        if len(i.strip()) >= 0 and len(i.strip()) <= 100 and limit_passed == False:
            list_of_items.insert(count, i.strip())
        else :
            limit_passed = False
        count += 1
    # Check limit passed or not
    if limit_passed == False :
        temp_list = defaultdict(list)
        for item in list_of_items:
            #Add data in array with group
            temp_list[str(sorted(item))].append(item)
        result = list(temp_list.values())
        print(str(result))
    else :
        print("Per string data must be between 0 to 100") 