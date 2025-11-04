print("MedEco Solutions 1.0\n")

estoque_medicamentos = {"dorflex": 60, "dipirona": 95, "buscopan": 45, "paracetamol": 86, "annita": 36}
usuarios_login = {"vicentejunior.ij@hotmail.com": {"nome" : "Vicente", "senha" : "12345678", "email" : "vicentejunior.ij@hotmail.com"}}

#email = "vicentejunior.ij@hotmail.com"
#senha = "12345678"
#nome = "Vicente"
contador = 3
contador2 = 0
opcao = 5

print("Faça login na sua conta: \n")

while contador != 0 and contador2 == 0:

    email_digitado = input("Digite seu email: ")
    email_formatado = email_digitado.lower()
    senha_digitada = input("Digite sua senha: ")

    if email_digitado == usuarios_login.get(email_digitado, {}).get("email") and senha_digitada == usuarios_login.get(email_digitado, {}).get("senha"):
    #if email_formatado == email and senha_digitada == senha:
        print(f"\n\nSeja bem vindo, {usuarios_login[email_digitado]["nome"]}!\n ")
        while True:


            menu = f"""
Escolha a Opção desejada:

(1) Entrada de Medicamentos
(2) Baixa de Medicamentos
(3) Extrato de Medicamentos em estoque
(4) Adicionar Novos Medicamentos
(5) Sair

"""
            print(menu)
            opcao = int(input())

            if opcao == 1:
                print("Entrada de Medicamentos:\n")
                nome_medicamento = input("Digite o nome do medicamento: ")
                quant_medicamento = int(input("Digite a quantidade de medicamentos que entrou no estoque: "))
                estoque_medicamentos[nome_medicamento] += quant_medicamento
                print(f"\nForam adicionados {quant_medicamento} unidades de {nome_medicamento} ao estoque!\n")


            elif opcao == 2:
                print("Baixa de Medicamentos:\n")
                nome_medicamento = input("Digite o nome do medicamento: ")
                quant_medicamento = int(input("Digite a quantidade de medicamentos que saíu do estoque: "))
                estoque_medicamentos[nome_medicamento] -= quant_medicamento
                print(f"\nSairam {quant_medicamento} unidades de {nome_medicamento} do estoque!\n")

            elif opcao == 3:
                print("Extrato de Medicamentos em Estoque:\n")
                for chave in estoque_medicamentos:
                    print(f"{chave} = {estoque_medicamentos[chave]} unidades.")

            elif opcao == 4:
                print("Adicionar Novos Medicamentos:\n")
                nome_novo_medicamento = input("Digite o nome do novo medicamento: ")
                quant_novo_medicamento = int(input("Digite a quantidade de medicamentos: "))
                estoque_medicamentos[nome_novo_medicamento] = quant_novo_medicamento
                print(f"\nForam adicionados {quant_novo_medicamento} unidades de {nome_novo_medicamento} ao estoque!\n")

            elif opcao == 5:
                contador2 += 1
                break

            else:
                print("Opção inválida! Digite a opção desejada: ")


    else:
        contador -= 1
        print(f"\n\nDados inválidos! Você tem mais {contador} tentativa!")

if contador == 0:
    print("Acesso bloqueado!\n")
else:
    print("Acesso finalizado! Muito obrigado, volte sempre!")
