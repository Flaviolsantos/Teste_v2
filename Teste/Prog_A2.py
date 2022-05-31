
if __name__ == '__main__':
    x = float(input('Insira  altura em metros'))
    cm = print(f'Altura em cm = {x * 100}')

    y = input('repetir')
    while  y in ('yes', 'y','sim','s'):
        outro = float(input('Insira  altura em metros'))
        cm = print(f'Altura em cm = {outro * 100}')
        y = input('repetir')
        if y != ('yes', 'y','sim','s'):
            break


