ciclo = True
while ciclo:
    print('''
          Menu Principal
          1) Compra
          2) Vender
          3) Salir
          
          ''')
    op = int(input("Seleccione: "))
    match op:
        case 1:
            print("Comprar")
        case 2:
            print("Vender")
        case 3:
            ciclo = False
        case _:
            print("Opcion incorrecta")
            
            