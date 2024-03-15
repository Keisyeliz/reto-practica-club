
cantidadFlt = float(input("Ingrese la cantidad a convertir: "))
var_unidadStr = input("Ingrese la unidad a convertir (D/C): ")

if var_unidadStr =='D':
    valor_pesos = cantidadFlt * 390585
    print('la cantidad',cantidadFlt,'equivale a: ',valor_pesos,'COP')


if var_unidadStr =='C':
    valor_dolares = cantidadFlt / 390585
    print('la cantidad',cantidadFlt,'equivale a: ',valor_dolares,'USD')