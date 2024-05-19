def menu():
    print(f"""
 \t\t ____  _ _       __  __              
 \t\t|  _ \(_) |     |  \/  |             
 \t\t| |_) |_| |_ ___| \  / | __ _ _ __   
 \t\t|  _ <| | __/ _ \ |\/| |/ _` | '_ \  
 \t\t| |_) | | ||  __/ |  | | (_| | |_) | 
 \t\t|____/|_|\__\___|_|  |_|\__,_| .__/  
 \t\t                              | |     
 \t\t                              |_|     

\t[1] - Cadastrar Receita\t\t[2] - Visualizar Receita
\t[3] - Atualizar Receita\t\t[4] - Apagar Receita
\t[5] - Procurar Receita por País\t[6] - Ver Receitas Favoritas
\t[7] - Avaliar Receita\t\t[8] - Ver Receita Aleatória
\t\t\t[0] - Sair do Programa                    
""")
    
def listar_receitas():
    try:
        with open("receitas.txt", "r", encoding="utf-8") as file:
            receitas = file.read().strip().split("===================================")
        
        receitas = [receita for receita in receitas if receita.strip()]  # Remove entradas vazias
        
        if not receitas:
            print("\nNão há receitas cadastradas.")
            return
        
        for i, receita in enumerate(receitas):
            print(f"\n== RECEITA {i + 1} ==\n")
            linhas = receita.strip().split("\n")
            for linha in linhas:
                print(linha)
    
    except FileNotFoundError:
        print("O arquivo de receitas não foi encontrado. Por favor, cadastre uma receita primeiro.")
    except Exception as e:
        print(f"Ocorreu um erro ao tentar ler o arquivo: {e}")

def cadastrar_receita():
    nome_receita = input("\nDigite o nome da receita que deseja cadastrar: ").capitalize()
    padrao = f"Nome Receita: {nome_receita}\n"
    
    try:
        with open("receitas.txt", "r", encoding="utf-8") as file:
            receitas_existentes = file.readlines()

        for linha in receitas_existentes:
            if padrao in linha:
                print(f"A receita '{nome_receita}' já está cadastrada. Não é possível adicionar novamente.")
                return

    except FileNotFoundError:
        print("\n\t\t\t!!! AVISO !!!\n\nArquivo 'receitas.txt' não existe. Um novo arquivo será criado.\n")
    
    pais = input(f"Insira o país da receita {nome_receita}: ").capitalize()
    ingredientes = input(f"Insira os ingredientes usados em {nome_receita}: ").capitalize()
    preparo = input(f"Explique o método de preparo: ").capitalize() 
    favorita = input(f"A receita {nome_receita} é uma das suas favoritas? ").capitalize()
    
    while True:
        if favorita in {"Não", "Sim"}:
            break
        else:
            print("\nParece que você inseriu um valor inválido. Você só pode inserir os valores [Não] ou [Sim].")
            favorita = input(f"A receita {nome_receita} é uma das suas favoritas? ").capitalize()

    try:
        with open("receitas.txt", "a", encoding="utf-8") as file:
            file.write("===================================\n")
            file.write(f"Nome Receita: {nome_receita}\n")
            file.write(f"País Receita: {pais}\n")
            file.write(f"Ingredientes: {ingredientes}\n")
            file.write(f"Método de Preparo:\n - {preparo}\n")
            file.write(f"Avaliação: Sem Avaliação\n")
            file.write(f"Favorita: {favorita}\n")
            file.write("\n")
        print("Receita cadastrada com sucesso!")
    except Exception as e:
        print(f"Erro na gravação: {e}")



def atualizar_receita():
    receita_a_ser_alterada = input("Digite o nome da Receita a ser alterada: ").capitalize()
    
    try:
        with open("receitas.txt", "r", encoding="utf-8") as file:
            receitas = file.readlines()
        
        receita_encontrada = False
        aux2 = []
        
        i = 0
        while i < len(receitas):
            linha = receitas[i]
            if linha.startswith("Nome Receita:") and receita_a_ser_alterada in linha:
                receita_encontrada = True
                # Ignorar linhas até o próximo separador
                while i < len(receitas) and receitas[i].strip() != "===================================":
                    i += 1
                i += 1  # Ignorar o separador também
            else:
                aux2.append(linha)
                i += 1

        if not receita_encontrada:
            print(f"\nReceita '{receita_a_ser_alterada}' não encontrada.")
            return
        nome_receita = input("Insira o novo nome da receita: ").capitalize()
        # Verificar se o novo nome já existe
        for linha in receitas:
            if linha.startswith("Nome Receita:") and nome_receita in linha:
                print(f"\nJá existe uma receita com o nome '{nome_receita}'. Por favor, escolha outro nome.")
                return
        pais_receita = input("Insira o novo país da receita: ").capitalize()
        ingredientes_receita = input("Insira os novos ingredientes da receita: ").capitalize()
        preparo = input(f"Explique o método de preparo: ").capitalize()
        favorita = input(f"A receita {nome_receita} é uma das suas favoritas? ").capitalize()
        while favorita not in {"Não", "Sim"}:
            print("\nParece que você inseriu um valor inválido. Você só pode inserir os valores [Não] ou [Sim].")
            favorita = input(f"A receita {nome_receita} é uma das suas favoritas? ").capitalize()
        
        nova_receita = (
            f"Nome Receita: {nome_receita}\n"
            f"País Receita: {pais_receita}\n"
            f"Ingredientes: {ingredientes_receita}\n"
            f"Método de Preparo:\n - {preparo}\n"
            "Avaliação: Sem Avaliação\n"
            f"Favorita: {favorita}\n"
        )

        with open("receitas.txt", "w", encoding="utf-8") as file:
            for linha in aux2:
                file.write(linha)
            file.write(nova_receita)
        
        print("Receita atualizada com sucesso!")
    except FileNotFoundError:
        print("\nO arquivo de receitas não foi encontrado. Por favor, cadastre uma receita primeiro.")
    except Exception as e:
        print(f"\nOcorreu um erro ao tentar atualizar a receita: {e}")


    
def apagar_receita():
    try:
        with open("receitas.txt", "r", encoding="utf-8") as file:
            receitas = file.read().split("===================================")
        if len(receitas) == 1:
            print("\nNão há receitas cadastradas.")
            return
        else:
            print("\nReceita(s) Cadastrada(s) antes de deletar:")
            for receita in receitas:
                print(receita.strip())
            
    except FileNotFoundError:
        print("O arquivo de receitas não foi encontrado. Por favor, cadastre uma receita primeiro.")
        return
    except Exception as e:
        print(f"Ocorreu um erro ao tentar ler as receitas: {e}")
        return

    nome_receita_a_ser_deletada = input("\nDigite o nome da receita que deseja deletar: ").strip().lower()
    padrao = f"Nome Receita: {nome_receita_a_ser_deletada}\n"
    receita_encontrada = False
    receitas_atualizadas = []

    for receita in receitas:
        if padrao.lower() not in receita.lower():
            receitas_atualizadas.append(receita.strip())
        else:
            receita_encontrada = True

    if not receita_encontrada:
        print("\nReceita não encontrada.")
        return

    try:
        with open("receitas.txt", "w", encoding="utf-8") as file:
             for receita in receitas_atualizadas:
                 file.write(receita.strip() + "\n===================================\n")

        print("\nReceita deletada com sucesso!")
        
    except Exception as e:
        print(f"Ocorreu um erro ao tentar salvar as receitas: {e}")

def procurar_receita_por_pais():
    try:
        with open("receitas.txt", "r", encoding="utf-8") as file:
            receitas = file.read()

        if "Nome Receita:" not in receitas:
            print("Não há receitas cadastradas.")
            return

        pais_desejado = input("\nInsira o país para procurar receitas: ").capitalize()
        receitas_list = receitas.split("===================================\n")
        receitas_encontradas = [receita for receita in receitas_list if f"País Receita: {pais_desejado}" in receita]

        if receitas_encontradas:
            print(f"\n== RECEITAS DE {pais_desejado.upper()} ==\n")
            for receita in receitas_encontradas:
                print(receita.strip())
                print()
        else:
            print(f"\nNão foram encontradas receitas do país '{pais_desejado}'.")

    except FileNotFoundError:
        print("O arquivo de receitas não foi encontrado. Por favor, cadastre uma receita primeiro.")
    except Exception as e:
        print(f"Ocorreu um erro ao tentar ler o arquivo: {e}")

def ver_receitas_favoritas():
    try:
        with open("receitas.txt", "r", encoding="utf-8") as file:
            receitas = file.read()

        if "Nome Receita:" not in receitas:
            print("Não há receitas cadastradas.")
            return

        receitas_list = receitas.split("===================================\n")
        favoritas = [receita for receita in receitas_list if "Favorita: Sim" in receita]

        if favoritas:
            print("\n== RECEITAS FAVORITAS ==\n")
            for receita in favoritas:
                print(receita.strip())
                print()
        else:
            print("\nVocê não tem receitas marcadas como favoritas.")

    except FileNotFoundError:
        print("\nO arquivo de receitas não foi encontrado. Por favor, cadastre uma receita primeiro.")
    except Exception as e:
        print(f"\nOcorreu um erro ao tentar ler o arquivo: {e}")

def avaliar_receita():
    try:
        with open("receitas.txt", "r", encoding="utf-8") as file:
            receitas = file.read()

        if "Nome Receita:" not in receitas:
            print("Não há receitas cadastradas.")
            return

        print("\n== RECEITAS CADASTRADAS ==\n")
        receitas_list = receitas.split("===================================\n")
        for receita in receitas_list:
            if receita.strip():
                print(receita.split("\n")[0].strip())

        nome_receita = input("\nInsira o nome da receita que deseja avaliar: ").capitalize()
        nova_lista_receitas = []
        receita_encontrada = False

        for receita in receitas_list:
            if f"Nome Receita: {nome_receita}" in receita:
                receita_encontrada = True
                avaliacao = input("Forneça sua avaliação para esta receita (de 1 a 5 estrelas): ")
                while True:
                    if avaliacao.isdigit() and 1 <= int(avaliacao) <= 5:
                        break
                    else:
                        avaliacao = input("Por favor, insira uma avaliação válida (de 1 a 5 estrelas): ")

                nova_receita = receita.replace("Avaliação: Sem Avaliação", f"Avaliação: {avaliacao} estrela(s)")
                nova_lista_receitas.append(nova_receita.strip())
            else:
                nova_lista_receitas.append(receita.strip())

        if receita_encontrada:
            with open("receitas.txt", "w", encoding="utf-8") as file:
                for receita in nova_lista_receitas:
                    if receita.strip():
                        file.write("===================================\n")
                        file.write(receita.strip() + "\n")

            print(f"\nA receita '{nome_receita}' foi avaliada com sucesso.")
        else:
            print("\nA receita não foi encontrada.")

    except FileNotFoundError:
        print("\nO arquivo de receitas não foi encontrado. Por favor, cadastre uma receita primeiro.")
    except Exception as e:
        print(f"\nOcorreu um erro ao tentar ler o arquivo: {e}")

def obter_indice_aleatorio(receitas, entrada_usuario):
    tamanho_receitas = len(receitas)
    hash_entrada = hash(entrada_usuario)
    indice_aleatorio = hash_entrada % tamanho_receitas
    return indice_aleatorio

def ver_receita_aleatoria():
    try:
        with open("receitas.txt", "r", encoding="utf-8") as file:
            receitas = file.read().split("===================================\n")

            if receitas:
                entrada_usuario = input("\nDigite algo rapidamente para gerar uma receita aleatória: ")
                indice_aleatorio = obter_indice_aleatorio(receitas, entrada_usuario)
                print("\nReceita Aleatória:\n")
                print(receitas[indice_aleatorio])
            else:
                print("Não há receitas cadastradas.")

    except FileNotFoundError:
        print("\nO arquivo de receitas não foi encontrado. Por favor, cadastre uma receita primeiro.")
    except Exception as e:
        print(f"\nOcorreu um erro ao tentar ler o arquivo: {e}")


def main():
    menu()
    while True:
        opcao = input("\nEscolha uma das opções do menu: ")
        if opcao == '1':
            cadastrar_receita()
        elif opcao == '2':
            listar_receitas()
        elif opcao == '3':
            listar_receitas()
            print("")
            atualizar_receita()
        elif opcao == '4':
            apagar_receita()
        elif opcao == '5':
            procurar_receita_por_pais()
        elif opcao == '6':
            ver_receitas_favoritas()
        elif opcao == '7':
            avaliar_receita()
        elif opcao == '8':
            ver_receita_aleatoria()
        elif opcao == '0':
            print('Encerrando o programa. Até mais!')
            break
        else:
            print('Opção inválida. Tente novamente.')

main()