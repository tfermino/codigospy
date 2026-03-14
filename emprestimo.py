Salario = float(input("Digite seu salario: "))
Parcela = float(input("Digite o valor da parcela do emprestimo: ")) 
Negativado = input ("Você é negativado?(sim ou nao)")
Avalista = float (input("Digite o salario do seu avalista: "))

if (Parcela <= Salario * 0.3 and Negativado == "não") or (Negativado == "sim" and Avalista >= 5000):
    print("Emprestimo aprovado.")
else: 
    print ("Emprestimo negado.")