
print("valores de ususario")
num1=int(input('Dame un valor 1'))
num2=int(input('Dame un valor 2'))

if(num1>num2):
    print("{} Este es mayor que este {}".format(num1,num2))
else:
    print("{1} Este es mayor que este {0}".format(num1,num2))