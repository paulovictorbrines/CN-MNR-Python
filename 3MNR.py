# Método de Newton-Raphson #

import math
e = 2.71828

E = float(input("E = ").replace(",",".")) # O resultado da aproximação será o mais perto de "E"

def f(x): # Coloque a função f(x) depois de return
    ####################################

    return 
    #Exemplo: return x**5+x**2*math.cos(x)-(6*x)-5

    ####################################

def f_linha(x): # Coloque a derivada de f(x) depois de return
    ####################################

    return
    # Exemplo: return (5*x**4)-(x**2*math.sin(x))+(2*x*math.cos(x))-6

    ####################################

#a = float(input("a = ").replace(",","."))
#b = float(input("b = ").replace(",","."))
x = float(input("x0 = ").replace(",","."))
lista_x, lista_fx = [],[]

print(f"  ||   x   ||   f(x)  ||\n"," ||-------||---------||")
print(f"0 || {x:.8f} || {f(x):.8f} ||")

i=0
while abs(f(x))>E: #and (x >= a and x <= b)
    x=x-(f(x)/f_linha(x))
    lista_x.append(x)
    f(x)
    lista_fx.append(f(x))

    i=i+1

for i in range(len(lista_x)):
    if i!=len(lista_x)-1:
        print(f"{i+1} || {lista_x[i]:.8f} || {lista_fx[i]:.8f} ||") 
    else:
        print(f"{i+1} || ({lista_x[i]:.8f}) || {lista_fx[i]:.8f} ||") 
print(f"solução aproximada = {lista_x[-1]} | (f(x) = {lista_fx[-1]})")
print()