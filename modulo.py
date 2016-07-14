import os
import time


def verificar(a):
    for c in a :
        if(ord(c)<65 or ord(c)>90) and (ord(c)<97 or ord(c)>122)and (ord(c)!=32):
            return False
    return True
def report(a,b):
    os.system("clear")
    print("reporte")
    print("BUenos dias ",a,"con dni",b)
    print("tipos ")
    print("1.- 2%")
    print("1.- 4%")
    print("1.- 7%")
    time.sleep(2)
