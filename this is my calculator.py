first = ("enter first number : ")
operator = ("enter operator (+,-,*,/,%) : ")
second = ("enter second number : ")

first = int(first)
second = int(second)

if operator == "+" :
    print(first + second)
elif operator == "-" :
    print(first - second)
elif operator == "*" :
    print(first * second)
elif operator == "/" :
    print(first / second)
elif operator == "%" :
    print(first % second)

else :
    print( "envalid operator")
