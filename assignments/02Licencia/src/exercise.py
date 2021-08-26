
def main():
    #Escribe tu código debajo de esta línea
    edad=int(input("Ingresa tu edad: "))
    if (edad>=18):
        id=str(input('¿Tienes identificación oficial? (s/n): '))
        if  id=='s':
            print('Trámite de licencia concedido')
        elif id=='n':
            print('No cumples requisitos')

        else:
            print('Respuesta incorrecta')
    
    elif (edad<18 and edad!=0):
        print('No cumples requisitos')

    else:
        print('Respuesta incorrecta')
    pass


if __name__ == '__main__':
    main()
