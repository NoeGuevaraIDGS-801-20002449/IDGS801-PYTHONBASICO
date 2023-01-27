


class OperaBas:
    #propiedades de clase
    n1=0
    n2=0
    res=0
    #constructor
    def __init__(self, a, b):
        self.n1=a
        self.n2=b
    #metodos de clase
    def suma(self):
        self.res=self.n1+self.n2
    def resta(self):
        self.res=self.n1-self.n2
    def multiplicacion(self):
        self.res=self.n1*self.n2
    def division(self):
        self.res=self.n1/self.n2

def main():
    while True:
        print("1. suma")
        print("2. resta")
        print("3. Multiplicacion")
        print("4. Division")
        print("5. Salir")
        choice = int(input("Dame la opcion: "))
        if(choice==1):
            v1=int(input('Dame un valor 1 '))
            v2=int(input('Dame un valor 2 '))
            obj=OperaBas(v1,v2)
            obj.suma()
            print("La suma es: {}".format(obj.res))
        elif(choice==2):
            v1=int(input('Dame un valor 1 '))
            v2=int(input('Dame un valor 2 '))
            obj=OperaBas(v1,v2)
            obj.resta()
            print("La resta es: {}".format(obj.res))
        elif(choice==3):
                v1=int(input('Dame un valor 1 '))
                v2=int(input('Dame un valor 2 '))
                obj=OperaBas(v1,v2)
                obj.multiplicacion()
                print("La multiplicacion es: {}".format(obj.res))
        elif(choice==4):
                v1=int(input('Dame un valor 1 '))
                v2=int(input('Dame un valor 2 '))
                obj=OperaBas(v1,v2)
                obj.division()
                print("La division es: {}".format(obj.res))
        elif(choice==5):
                print("Elije un numero del 1 al 4")
                break

if __name__ == '__main__':
    main()
