expression = input("Expression: ")
x, z, y = expression.split(" ")

if z == '+' :
    print(float(x) + float(y))

elif z == '-' :
    print(float(x) - float(y))

elif z == '*' :
    print(float(x) * float(y))

elif z == '/' :
    print(float(x) / float(y))