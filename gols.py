jogador_um = input("Digite o nome do jogador/a 1: ")
jogador_dois = input("Digite o nome do jogador/a 2: ")
print("Olá, ", jogador_um, "e ", jogador_dois, "Sejam bem vindos!")

resultado_um = int(input("Digite a quantidade de gols do primeiro/a jogador/a: "))
resultado_dois = int(input("Digite a quantidade de gols do segundo/a jogador/a: "))

if resultado_um > resultado_dois:
    print("O jogador vencedor é: ", jogador_um)
elif resultado_dois > resultado_um:
    print("O jogador vencedor é: ", jogador_dois)
else: print ("Empate!!")