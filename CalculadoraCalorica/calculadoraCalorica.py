''' 66 + (13,7 * KG) + (5 * CM) - (6,8 * IDADE) = HOMENS
    665 + (9,6 x peso) + (1,8 x altura em cm) – (4,7 x idade) = MULHERES

    Pouco exercício: multiplicar por 1,2;
    Exercício Leve: multiplicar por 1,375;
    Exercício moderado: multiplicar por 1,55;
    Exercício pesado: multiplicar por 1,725;
    Exercício pesado diário: multiplicar por 1,9.

    '''

'''perguntas'''
peso = float(input("insira seu peso: "))
idade = int(input("insira sua idade: "))
altura = int(input("insira sua altura em CM: "))
sexo = input("informe seu sexo. H para Homem, M para mulher: ")
exercicios = int(input(
    "Pouco exercício digite 1, Exercício Leve 2, " +
    "Exercício moderado 3, Exercício pesado 4 ou Exercício pesado diário 5"))

'''multiplicadores'''
if (exercicios < 1 or exercicios > 5):
    print("voce não escolheu uma opção de exercícios válida")
    quit()


def multiplicador(i):
    selecionador = {
        1: 1.2,
        2: 1.375,
        3: 1.55,
        4: 1.725,
        5: 1.9
    }
    return selecionador.get(i)


'''calc area'''
if (sexo == 'H' or sexo == 'h'):
    vlBasal = 66 + ((13.7 * peso)+(5*altura))-(6.8*idade)
elif (sexo == 'M' or sexo == 'm'):
    vlBasal = 665 + ((9.6 * peso) + (1.8 * altura)) - (4.7 * idade)
else:
    print("voce não escolheu uma opção válida")
    quit()


print("Seu valor calórico basal é de "+str(vlBasal *
                                           multiplicador(exercicios))+" KiloCalorias por dia")
