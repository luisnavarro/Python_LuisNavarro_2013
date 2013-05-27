from lib.operaciones import *

valor = int(raw_input('ingresa un valor'))
valor2 = int(raw_input('ingresa otro valor'))
operacion = raw_input('¿Que operaciones desea realizar : {s - r - m - d}')

if operacion.lower == 's':
    print suma(valor,valor2)

elif operacion.lower == 'r':
    print resta(valor,valor2)
    
elif operacion.lower == 'm':
    print multiplicar(valor,valor2)

elif operacion.lower == 'd':
    print dividir(valor,valor2)
        
