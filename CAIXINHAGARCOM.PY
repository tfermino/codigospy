ValorRest = float(input("Qual o valor da conta? ")) 
QtdeAmigos=int(input("Quantidade de pessoas que irao dividir a conta? "))

Caixinha = ValorRest * 0.1

ValorTotal = ValorRest + Caixinha

Dividido = ValorTotal / QtdeAmigos

print (f"O valor para cada amigo pagar sera de R$ {Dividido:.2f}") 
#usei para que o resultado apareça com duas casas decimais, por se tratar e valor em reais