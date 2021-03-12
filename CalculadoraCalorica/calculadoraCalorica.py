''' 66 + (13,7 * KG) + (5 * CM) - (6,8 * IDADE) = HOMENS
    665 + (9,6 x peso) + (1,8 x altura em cm) – (4,7 x idade) = MULHERES
    
    Pouco exercício: multiplicar por 1,2;
    Exercício Leve: multiplicar por 1,375;
    Exercício moderado: multiplicar por 1,55;
    Exercício pesado: multiplicar por 1,725;
    Exercício pesado diário: multiplicar por 1,9.
    
    '''
peso = int(input("insira seu peso: "))
idade = int(input("insira sua idade: "))
altura = int(input("insira sua altura em CM: "))
sexo = input("informe seu sexo. H para Homem, M para mulher: ")

if (sexo == 'H' or sexo == 'h'):
    vlBasal = 66 + ((13.7 * peso)+(5*altura))-(6.8*idade)
elif (sexo == 'M' or sexo == 'm'):
    vlBasal = 665 + ((9.6 * peso) + (1.8 * altura)) - (4.7 * idade)
else:
    print("voce não escolheu uma opção válida")
    quit()


print("Seu valor calórico basal é de "+str(vlBasal)+" KiloCalorias por dia")
