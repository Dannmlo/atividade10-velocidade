# Exercício Python 10: faça um algoritimo que receba a velocidade em Km/h de um veiculo e:
# se maior que 60km/h aplicar multa de 7 vezes a da velocidade permitida

km=int(input("Insira a velocidade em km/h percorrida:"))
multa = (km-60)*7

print(f'''Sua velociade foi de {km}km/h''')

if (km > 60):
    print(f"Você recebeu uma multa de: R${multa}")
else :
    print(f"Você não recebeu multa")