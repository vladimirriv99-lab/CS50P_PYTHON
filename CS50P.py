#preguntar nombre
name = input("waht's your name? ").strip().title()

#eliminar espacios al inicio y final (.strip())
#name = name.strip()

#mayuscula o kpital letter solo la 1ra letra (.capitalize())
#name = name.capitalize()

#mayusculas all str (.strip().title())
#name = name.strip().title()
'''
Saludar Usuario de manera conjunta (+) util si es solo 1 dato
    print("hello," + name)    
Saludar con mas de 1 dato (,)
    print('hello, ', name, 'welcome back')
'''
'''
syntaxis de manual 
    print(*object, sep=' ', end=/n) 
        print('hello,', end='')
        print(name)
'''
# Format str (F str)
print (f'hello, {name} jhgjhghjg')
