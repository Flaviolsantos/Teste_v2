if __name__ == '__main__':
    lista = []
    npar = []
    nimpar = []
    nprimo = []
    maximo = []
    minimo = []


    x = input('Insira um numero ')
    lista.append(x)
    maximo.append(x)
    minimo.append(x)
    par = int(x) % 2

    
    if par == 0:
        print(f'{x} é par')
        npar.append(lista[0])
    if par != 0:
        print(f'{lista[0]} é impar')
        nimpar.append(x)

    y = 0
    for count in range(2, int(x)):
        if (int(x) % count == 0):
            y += 1

    if (y == 0):
        print(f'{x} é primo')
        nprimo.append(x)
    else:
        print(f'{x} não é primo')

        if x > max(lista):
            maximo.append(x)
            print(f'{max(x)} é o maior numero até agora')
        elif x < min(lista):
            minimo.append(x)
            print(f'{min(x)} é o menor numero até agora')
        else:
            print(f' {x}é um numero normal')

    y = input(" repetir? ")


    while y == 'yes':
        outro = input('Insira outro numero ')
        par = int(outro) % 2

        if outro in lista:
            print(f'O número {outro} já foi inserido. Insira outro número.')
            continue


        lista.append(outro)
        if par == 0:
            print(f'{outro} é par')
            npar.append(outro)
        if par != 0:
            print(f'{outro} é impar')
            nimpar.append(outro)


        y = 0
        for count in range(2, int(outro)):
            if (int(outro) % count == 0):
                y += 1

        if (y == 0):
            print(f'{outro} é primo')
            nprimo.append(outro)
        else:
            print(f'{outro} não é primo')



        if outro > max(lista):
            maximo.append(outro)
            print(f'{max(outro)} é o maior numero até agora')
        elif outro < min(lista):
            minimo.append(outro)
            print(f'{min(outro)} é o menor numero até agora')
        else:
            print(f' {outro}é um numero normal')
        y = input(" repetir? ")



    if y == 'no':
            print(f' total inseridos = {len(lista)} / Numeros Inseridos {lista}')
            print(f'total de numeros pares = {len(npar)} / Numeros Pares {npar} ')
            print(f'total de numeros impares = {len(nimpar)} / Numeros Impares {nimpar}')
            print(f'total de numreos pares = {len(nprimo)} /Numeros Primos {nprimo}')
            print(f' Maior Numero {maximo} / Menor Nuemro {minimo} ' )
