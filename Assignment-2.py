# To get combinations of parenthesis and print it out
def printParenthesis(Str, Position, Count, Open, Close):
	if Close == Count :
		Parenthesis = "'"
		for i in Str:
			Parenthesis += i
		print(Parenthesis, end = "', ")
		return
	else:
		if Open > Close :
			Str[Position] = ')'
			printParenthesis(Str, Position + 1, Count, Open, Close + 1)
		if Open < Count :
			Str[Position] = '('
			printParenthesis(Str, Position + 1, Count, Open + 1, Close)
			
# To get input from user
Count = int(input("Enter number of combinations required: "))
if Count > -1 and Count <= 8 :
    Str = [""] * 2 * Count
    printParenthesis(Str, 0, Count, 0, 0)
else:
    print("Enter number between -1 to 8")
