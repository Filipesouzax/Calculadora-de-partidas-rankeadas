## Código feito para o desafio proposto no bootcamp Potência Tech iFood - Programação do Zero onde a proposta é uma calculadora de partidas rankeadas

##introdução
print("Bem vindo a calculadora de partidas rankeadas\n")
print("----- Calculadora de Partidas Rankeadas -----\n")
print("")


## Estrutura de repetição para reiniciar o programa
while True:
    input("        PRESSIONE ENTER PARA COMEÇAR\n")

    def ranking(vitorias, derrotas):
        saldo = vitorias - derrotas
        return saldo

## Variáveis de entrada
    vitorias = int(input("Digite o número de vitórias: "))
    derrotas = int(input("Digite o número de derrotas: "))
  
## Estrutura de condição parametrizando os rankings
    saldo = ranking(vitorias, derrotas)
    
    if saldo < 10:
        print("Ferro")
    elif saldo >= 11 and saldo < 20:
        print("O herói tem saldo de", saldo, "e está no nível: Bronze")
    elif saldo >= 21 and saldo < 50:
        print("O herói tem saldo de", saldo, "e está no nível: Prata")
    elif saldo >= 51 and saldo <= 80:
        print("O herói tem saldo de", saldo, "e está no nível de: Ouro")
    elif saldo >= 81 and saldo <= 90:
        print("O herói tem saldo de", saldo, "e está no nível de: Diamante")
    elif saldo >= 91 and saldo <= 100:
        print("O herói tem saldo de", saldo, "e está no nível de: Lendário")
    elif saldo >= 101:
        print("O herói tem saldo de", saldo, "e está no nível de: Imortal")

## Fim da estrutura de repetição
    reiniciar = input("\nDeseja reiniciar o programa? (s/n): ")
    if reiniciar.lower() != 's':
        break

## Fim do programa

## coded by Filipesouzac