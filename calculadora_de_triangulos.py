# -*- coding: utf-8 -*-
"""
Programa de triángulos
by @da070808
"""
#entrada
print("Dame el valor de a: ")
a=float(input())
print()
print("dame el valor de b: ")
b=float(input())
print()
print("dame el valor de c: ")
c=float(input())
print()
print(chr(27)+"[1;33m"+" ")

#cálculos
suma_b_c=b**2+c**2
suma_a_c=a**2+c**2
suma_a_b=a**2+b**2

P=a+b+c
S=P/2
A=(S*(S-a)*(S-b)*(S-c))**(1/2)

mayor1=((a**2)>suma_b_c and (b**2)<suma_a_c and (c**2)<suma_a_b)
mayor2=((b**2)>suma_a_c and (a**2)<suma_b_c and (c**2)<suma_a_b)
mayor3=((c**2)>suma_a_b and (a**2)<suma_b_c and (b**2)<suma_a_c)

#Salidas en pantalla

#desigualdad triangular
if a<b+c and b<a+c and c<a+b:
    print("Sí se puede")
else:
    print("no se puede")

#clasificacion segun angulo
if (a**2)==suma_b_c or (b**2)==suma_a_c or (c**2)==suma_a_b:
    print("Triángulo rectángulo")
elif mayor1 or mayor2 or mayor3:
    print("triángulo obtusángulo")
else:
    print("trangulo agudo")

#clasificacion segun lado
if a==b and b==c and c==a:
    print("equilatero")
elif a==b or b==c or c==a:
    print("isoseles")
else:
    print("escaleno")
#area, perimetro
print("El área es: ", A)
print("el perimetro es ",P)


print(chr(27)+"[1;37m"+" ")