def escrever(output, line, control):
    with open(output, control, encoding='utf-8') as file:
        file.write(line)

def ler(ficheiro):

    with open(ficheiro) as file:
        for num, line in enumerate(file, 1):
            print(line.rstrip().split(','))
            if num == 1:
                titulos = (line.rstrip().split(','))
                escrever('resultado.txt', line, 'w')


            else:
                dados = (line.rstrip().split(','))

    for linha in range(1, 12):
        totallinha = 0
        for coluna in range(1, 5):
            totallinha = str(totallinha) + str(dados[linha - 1][coluna - 1])
        print(f'{totallinha}')
        escrever('resultado.txt', line, 'a')

    for coluna in range(1, 5):
        totalcoluna = 0
        for linha in range(1, 13):
            totalcoluna += str(totalcoluna) + str(dados[linha - 1][coluna - 1])
        print(f'{totalcoluna}')
        escrever('resultado.txt', line, 'a')



if __name__ == '__main__':
    ler("passageiros.csv")