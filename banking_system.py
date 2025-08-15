#módulo depositar
def depositar(valor):
    if valor>0:
        
        return valor
    else: 
        print("Valor deve ser maior que 0")

saldo = 1000

# menu de opções

opcao_menu = ''
while (opcao_menu!=4):
    print('#### Menu ####')1
    opcao_menu = int(input('Digite a opção desejada: '))
    if(opcao_menu ==1):
        valor = float(input('depósito: '))
        depositar(valor)    

        #atualização do saldo
        saldo+= depositar(valor)
        print(f'Valor depositado: {valor}')
        print(f'saldo final = {saldo}')
    elif(opcao_menu==4):
        print('Fim das operações!')

    else: print('opção inválida')