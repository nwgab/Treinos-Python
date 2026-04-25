#Aqui Pedimos para o usuário escolher uma das opções de operação, que estão representadas por números de 1 à 4
#Enquanto o usuário não escolher um número de 1 a 4 ele repetira o loop com a pergunta pedindo que selecione o tipo de operação desejada
while True:
    #Criamos um input junto de uma váriavel para captar o que o usuário digitar, junto a uma estrutura de IF para identificar se o usuário digitou uma opção valida
    escolha_operacao = int(input( "Selecione o tipo de operação que deseja realizar ( 1-Soma, 2-Subtração, 3-Multiplicação, 4-Divisão) :" ))
    if escolha_operacao == 1:
        operacao = "Soma"
        break
    elif escolha_operacao == 2:
        operacao = "Subtração"
        break
    elif escolha_operacao == 3:
        operacao = "Multiplicação"
        break
    elif escolha_operacao == 4:
        operacao = "Divisão"
        break
    else:
        print("Escolha uma opção válida ")
    #Foi colocado uma mensagem confirmando para o usuário a opção escolhida
print(f" Legal vou escolheu realizar {operacao}!")
#Criamos mais um loop pois, não podemos deixar que a pessoa divida um número por 0 impedindo um erro da matematica e do VsCode
while True:
    #criamos um input para os 2 números desejados para realizar a operação de forma basica
    firstnumero = float(input(f"Digite o primeiro número da {operacao} :"))
    secondnumero = float(input(f"Digite o segundo número da {operacao} :"))
    #colocamos as condições para realizar a soma, subtração, multiplicação, divisão
    if escolha_operacao == 1:
        resultado= firstnumero + secondnumero
        print(f"Esse é o resultado {resultado}")
        break
    elif escolha_operacao == 2:
        resultado= firstnumero - secondnumero
        print(f"Esse é o resultado {resultado}")
        break
    elif escolha_operacao == 3:
        resultado= firstnumero * secondnumero
        print(f"Esse é o resultado {resultado}")
        break
    #Essa parte é crucial para evitar que o programa realize divisões por 0
    elif escolha_operacao == 4:
        if firstnumero == 0:
            print(f"Não é possivel realizar divisão por 0")
        elif secondnumero == 0:
            print(f"Não é possivel realizar divisão por 0")
        else:
            resultado= firstnumero / secondnumero
            print(f"Esse é o resultado {resultado}")
            break
    
