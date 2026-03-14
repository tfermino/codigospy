nota1 = float(input("Digite a nota1: "))
nota2 = float(input("Digite a nota2: "))
media= (nota1 + nota2)/2

print("Sua media foi", media) #saber a media e analisar se deu certo a parte do if 

if media >= 9.0:
    print ("MB")
elif media < 8.9 and media >=7.0: #usei a função and pra sinalizar que seria entre essas notas o resultado do print
    print("B")
elif media >= 5.0 and media < 6.9:
    print ("R")
else:
    print ("I")