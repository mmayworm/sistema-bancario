import os

# Módulo depositar
def depositar(valor):
    if valor>0:
        extrato = f'Depósito {valor}\n'        
        return valor, extrato
    else: 
        print("Valor deve ser maior que 0")

# Módulo sacar
def sacar(valor):
    if(valor<1):
        print('valor deve ser maior que zero')   
    elif(saldo<valor):
        print(f'Saldo insuficiente! {saldo}')        
    elif(valor>500):
        print('Limite de saque é de R$500.00')
    elif(quantidade_saque>=2):    
        print('Limite de saque é de 3x por dia')
    else:
        extrato = f'Saque: {valor}\n'  
        return valor, extrato          

limite_saque = 0
saldo = 0
extrato = ''
quantidade_saque = 0

# menu de opções

opcao_menu = ''

while (opcao_menu!='4'):
    print('''
        MENU:
        [1] - Depositar
        [2] - Sacar
        [3] - Extrato
        [4] - Sair  
    ''')
    opcao_menu = input('Digite a opção desejada: ')
    #opção de depósito
    if(opcao_menu =='1'):
        valor = float(input('Valor para Depósito: '))
        operacao = depositar(valor)        

        #atualização do saldo e extrato
        if(operacao!=None):
            saldo+= operacao[0]
            print(f'Valor depositado: {valor}\n')
            extrato = extrato + operacao[1]
            

    #opção de saque
    elif(opcao_menu=='2'):
        valor = float(input('Valor do Saque: '))
        if(quantidade_saque>=2):
            print('Quantidade de saque diário ultrapassado')
        else:    
            operacao = sacar(valor)

        #atualização do saldo
        if(operacao!=None and quantidade_saque<=2):
            saldo-= operacao[0]
            quantidade_saque+=1
            print(f'Valor sacado: {valor}')
            print(f'saldo final = {saldo}')
            extrato = extrato + operacao[1]

    #opção de extrato
    elif(opcao_menu=='3'):
        print(f'{extrato}Saldo do dia: {saldo}')        
            
    elif(opcao_menu=='4'):
        print('Fim das operações!')
        input('Pressione uma tecla para sair...')
        os.system('cls')

    else: print('opção inválida')