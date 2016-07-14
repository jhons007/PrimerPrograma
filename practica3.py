import modulo
import sys,os,time
def nombre():
    print("ingrese su nombre")
    global a
    a=input()
    while(not modulo.verificar(a)):
        a=input("ingrese correctamente su nombre")
    os.system("clear")
    time.sleep(2)
    data_dni=""
    while True:
        try:
            print("ingrese su dni")
            global b
            b=input()
            b=int(b)
            while(len(str(b))!=8):
                b=input("ingrese correctamnte su dni")
            data_dni=str(b)
            break
        except ValueError:
            print("ingrese un numero entero porfavor")
def menu():
    os.system("clear")
    print("******banco de abonooo*****")
    print("1.- informe")
    print("2.- cambio tipo de fondo")
    print("3.- ahorros de fondo mutuo")
    print("4.- salir")
    while True:
        try:
            print("ingrese su opcion del 1 a 4")
            global c
            c=input()
            c=int(c)
            if(c>4):
                c=input("ingrese solo hasta la opcion 4")
            break
        except ValueError:
            print("debe ingresar un numero entero")
    if(c==1):
        modulo.report(a,b)
        menu()





nombre()
menu()