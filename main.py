# Atividade ETEC - Empresa TudoWeb
# Objetivo: Pesquisa de satisfação com estrutura de repetição FOR

# Variáveis para armazenar as quantidades (Contadores)
qtd_excelente = 0 
qtd_ruim = 0

# Definimos o número de entrevistados
# Para o teste solicitado, use 10. Para a versão final, mude para 50. 
total_entrevistados = 50

print ("--- Pesquisa de Satidfação TUDOWEB ---")

# Estrutura de repetição FOR para coletar as respostas dos entrevistados
for i in range(1, total_entrevistados + 1):
    print(f"\nEntrevistado nº {i}")

    # Coleta de dados 
    nome = input("Digite o seu nome: ")
    idade = input("Digite a sua idade: ") 

    print("Opinião sobre o atendimento")
    print("1: Excelente | 2: Bom | 3: Ruim")
    opiniao = input(" Sua resposta: ")

    # Estrutura de decisão para verificar a opinião do entrevistado
    if opiniao == "1":
        qtd_excelente += 1
    elif opiniao == "3":
        qtd_ruim += 1
        # Caso seja "2" (Bom), o programa apenas segue, pois não pede soma específica para essa opção

# Exibição dos resultados 
print ("\n" + "="*30)
print("RESULTADO DA PESQUISA")
print(f"Quantidade de respostas EXCELENTE: {qtd_excelente}")
print(f"Quantidade de respostas RUIM: {qtd_ruim}")
print("="*30)
