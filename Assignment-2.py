# To get combinations of parenthesis and print it out
def print_parenthesis(my_str, position, count, open, close):
	if close == count :
		parenthesis = "'"
		for i in my_str:
			parenthesis += i
		print(parenthesis, end = "', ")
		return
	else:
		if open > close :
			my_str[position] = ')'
			print_parenthesis(my_str, position + 1, count, open, close + 1)
		if open < count :
			my_str[position] = '('
			print_parenthesis(my_str, position + 1, count, open + 1, close)

# To get input from user
count = int(input("Enter number of combinations required: "))
if count > -1 and count <= 8 :
    my_str = [""] * 2 * count
    print_parenthesis(my_str, 0, count, 0, 0)
else:
    print("Enter number between -1 to 8")