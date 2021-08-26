def main():
    # Escribe el código adecuado para completar el programa
    x = int(input("Ingresa el primer número: "))
    y = int(input("Ingresa el segundo número: "))
    z = int(input("Ingresa el tercer número: "))
    if (x>=y and x>=z):
        if (y>=z):
            print(z)
            print(y)
            print(x)
        elif(z>=y):
            print(y)
            print(z)
            print(x)
    elif (y>=x and y>=z):
        if (x>=z):
            print(z)
            print(x)
            print(y)
        elif(z>=x):
            print(x)
            print(z)
            print(y)
    elif (z>=x and z>=y):
        if (x>=y):
            print(y)
            print(x)
            print(z)
        elif(y>=x):
            print(x)
            print(y)
            print(z)

    pass


if __name__=='__main__':
    main()
