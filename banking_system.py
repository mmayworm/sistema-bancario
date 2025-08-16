# Módulo depositar
def depositar(valor):
    if valor>0:        
        return valor
    else: 
        print("Valor deve ser maior que 0")

# Módulo sacar
def sacar(valor):
    if(valor<1):
        print('valor deve ser maior que zero')   
    elif(saldo<valor):
        print(f'Saldo insuficiente!{saldo}')        
    elif(valor>500):
        print('Limite de saque é de R$500.00')
      
    else: 
        return valor          

limite_saque = 0
saldo = 0

# menu de opções

opcao_menu = ''
while (opcao_menu!=4):
    print('''#### Menu ####
          #### opção 1: depositar####
          #### opção 2: sacar ####
          #### opção 4: sair ####
          ''')
    opcao_menu = int(input('Digite a opção desejada: '))
    #opção de depósito
    if(opcao_menu ==1):
        valor = float(input('depósito: '))
        operacao = depositar(valor)    

        #atualização do saldo
        if(operacao!=None):
            saldo+= operacao
            print(f'Valor depositado: {valor}')
            print(f'saldo final = {saldo}')

    #opção de saque
    elif(opcao_menu==2):
        valor = float(input('sacar: '))
        operacao = sacar(valor)

        #atualização do saldo
        if(operacao!=None):
            saldo-= operacao
            print(f'Valor sacado: {valor}')
            print(f'saldo final = {saldo}')

    elif(opcao_menu==4):
        print('Fim das operações!')

    else: print('opção inválida')