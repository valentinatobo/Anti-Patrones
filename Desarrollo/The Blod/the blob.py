def main():

	
    ladoA = int (input("Ingrese medida del lado A:  "))

    ladoB = int (input("Ingrese medida del lado B:  "))

    opcion = int(input("Ingrese 1 para saber el area y 2 para saber el perimetro:  "))
    if opcion == 1 and opcion != 2:
        resultado = ladoA * ladoB
        print(resultado)
    elif opcion == 2:
        resultado = ((ladoA*2)+(ladoB*2))
        print (resultado)
    else :
        print ("Opcion no valida")


if __name__ == "__main__":
    main()
