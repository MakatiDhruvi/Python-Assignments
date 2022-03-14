# for input comparision
number_dictionary = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

# TO get LCM
def get_lcm(number1, number2):
   if number1 > number2:
       greater = number1
   else:
       greater = number2
   while True:
       if (greater % number1 == 0) and (greater % number2 == 0):
           LCM = greater
           break
       greater += 1
   return int(LCM)

# To get GCD
def get_gcd(numerator, denominator):
    GCD = str(int(numerator / denominator))
    number_dictionary_count = 0
    while number_dictionary_count < len(number_dictionary):
        GCD = GCD.replace(str(number_dictionary_count), number_dictionary[number_dictionary_count])
        number_dictionary_count += 1
    return GCD

# To get input from user
number1 = input("Enter First Number:").replace(" ", "")
number2 = input("Enter Second Number:").replace(" ", "")
number_dictionary_count = 0
while number_dictionary_count < len(number_dictionary):
    number1 = number1.replace(number_dictionary[number_dictionary_count], str(number_dictionary_count))
    number2 = number2.replace(number_dictionary[number_dictionary_count], str(number_dictionary_count))
    number_dictionary_count += 1
number1 = int(number1)
number2 = int(number2)

# To get final result
print(get_gcd(number1 * number2, (get_lcm(number1, number2))))
