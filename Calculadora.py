#Aqui Pedimos para o usuário escolher uma das opções de operação, que estão representadas por números de 1 à 4
#Enquanto o usuário não escolher um número de 1 a 4 ele repetira o loop com a pergunta pedindo que selecione o tipo de operação desejada
while True:
    while True:
        #Criamos um input junto de uma váriavel para captar o que o usuário digitar, junto a uma estrutura de IF para identificar se o usuário digitou uma opção valida
        entrada = (input("\nSelecione o tipo de operação que deseja realizar ( 1-Soma, 2-Subtração, 3-Multiplicação, 4-Divisão) :" )).strip()
        #Aqui ele está tentando executar esse código, como em todos os try utilizados no código abaixo
        try:
            escolha_operacao = int(entrada)
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
        except:
            ValueError
            print(f"Escolha uma opção valida sem espaços vazios, enter, ou números invalidos")
        #Foi colocado uma mensagem confirmando para o usuário a opção escolhida
    print(f" Legal vou escolheu realizar {operacao}!")
    #Criamos mais um loop pois, não podemos deixar que a pessoa divida um número por 0 impedindo um erro da matematica e do VsCode
    while True:
        #criamos um input para os 2 números desejados para realizar a operação de forma basica, junto com um try que está convertendo o input de string para float
        entradafirstnumero = (input(f"Digite o primeiro número da {operacao} :")).strip()
        entradasecondnumero = (input(f"Digite o segundo número da {operacao} :")).strip()
        #conversão de string para float
        try:
            firstnumero= float(entradafirstnumero)
            secondnumero= float(entradasecondnumero)
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
                if secondnumero == 0:
                    print(f"Não é possivel realizar divisão por 0")
                else:
                    resultado= firstnumero / secondnumero
                    print(f"Esse é o resultado {resultado}")
                    break
        except:
            ValueError
            print(f"Escolha uma opção valida sem espaços vazios, enter")

#TESTE TESTE
