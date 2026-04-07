x = input('dame un numero: ')
y = input('dame otro numero: ')

'''
input admite str asi que debo declarar el tipo de dato a usar (int) 
para que los tome como numeros y se haga la suma correcta de no ser asi
solo va a CONCATENAR los datos
'''
z = int(x) + int(y)

print(f'la suma da {z}')

#Igual se puede anidar desde un principio pero es mas propenso a errores
a = int(input('dame un numero: '))
b = int(input('dame otro numero: '))

c = a+b

print(f'la suma da {c}')

#El mismo ejemplo pero con decimales (float)
d = float(input('dame un numero con decimales: '))
e = float(input('dame otro numero tambien con decimales: '))

#inclusive podemos redondear la cifra a x cantidad de decimales
f = round(d+e, 2)

print(f'la suma da {f:,}')

def val_cuadrado():
    x = int(input('Dame un numero y te doy su valor al cuadrado: '))
    print(f'El cuadrado de {x} es: {valsqr(x)}')

def valsqr(n):
    return pow(n, 2)
    
val_cuadrado()

'''
de igual manera podemos definir la operacion del valor al cuadrado
para solo llamarla en el codigo y no ponerla demanera directa

def Valsqr(n):
    return n * n
        o
    return n ** 2
        o
    return pow(n, 2)
    
'''
