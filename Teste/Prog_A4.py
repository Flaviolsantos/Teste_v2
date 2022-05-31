if __name__ == '__main__':
    arquipelagos = ['Açores', 'Madeira']
    empresas = ['SATA', 'TAP', 'Ryanair']
    dados = [
        [0, 0],
        [0, 0],
        [0, 0]
    ]

    dados[0][0] = input("insira os valores para os Açores na SATA ")
    dados[1][0] = input("insira os valores para os Açores na TAP ")
    dados[2][0] = input("insira os valores para os Açores na Ryanair ")
    dados[0][1] = input("insira os valores para a Madeira na SATA ")
    dados[1][1] = input("insira os valores para a Madeira na TAP ")
    dados[2][1] = input("insira os valores para a Madeira na Ryanair ")

    print(dados)

    for linha in range(0, 3):
        totallinha = 0
        for coluna in range(0, 2):
            totallinha += int(dados[linha - 1][coluna - 1])
        print(f'{totallinha}')

    for coluna in range(0, 2):
        totalcoluna = 0
        for linha in range(0, 3):
            totalcoluna += int(dados[linha - 1][coluna - 1])
        print(f'{totalcoluna}')





