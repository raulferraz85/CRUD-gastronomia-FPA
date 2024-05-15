

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
    
def formatar_texto(texto):
    palavras = texto.split()
    texto_formatado = ''

    for i in range(0, len(palavras), 10):
        texto_formatado += ' '.join(palavras[i:i+10]) + '\n'
    
    return texto_formatado

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
    preparo_formatado = formatar_texto(preparo)  
    favorita = input(f"A receita {nome_receita} é uma das suas favoritas? ").capitalize()
    while True:
        if favorita not in {"Não","Sim"}:
            print("\nParece Que Você Inseriu um Valor Inválido\nVocê só pode inserir os valores [Não] ou [Sim]")
            favorita = input(f"A receita {nome_receita} é uma das suas favoritas? ")
        else:
            break

    with open("receitas.txt", "a", encoding="utf-8") as file:
        file.write("===================================\n")
        file.write(f"Nome Receita: {nome_receita}\n")
        file.write(f"País Receita: {pais}\n")
        file.write(f"Ingredientes: {ingredientes}\n")
        file.write(f"Método de Preparo:\n - {preparo_formatado}\n")
        file.write(f"Avaliação: Sem Avaliação\n")
        file.write(f"Favorita: {favorita}\n")
        file.write("\n")

    print(f"\nA receita '{nome_receita}' foi cadastrada com sucesso!")
    
def visualizar_receitas():
    try:
        with open("receitas.txt", "r", encoding="utf-8") as file:
            receitas = file.readlines()
            numero_receita = 1

            for linha in receitas:
                if linha.startswith("Nome Receita:"):
                    print(f"\n== RECEITA {numero_receita}: ==\n")
                    numero_receita += 1
                print(linha, end='')
            if numero_receita == 1:
                print("\nNão há receitas cadastradas no sistema.")
            
    except FileNotFoundError:
        print("O arquivo de receitas não foi encontrado. Por favor, cadastre uma receita primeiro.")
    except Exception as e:
        print(f"Ocorreu um erro ao tentar ler o arquivo: {e}")


def atualizar_receita():
    try:
        with open("receitas.txt", "r", encoding="utf-8") as file:
            linhas = file.readlines()
            if len(linhas) == 0:
                print("Não há receitas cadastradas.") 
                return
        print("\n== RECEITAS CADASTRADAS ==\n")
        for linha in linhas:
            if linha.startswith("Nome Receita:"):
                print(linha.strip())

        receita_a_ser_atualizada = input("\nInsira o nome da receita que deseja atualizar: ").capitalize()

        if any(receita_a_ser_atualizada in linha for linha in linhas):
            print(f"\nA receita '{receita_a_ser_atualizada}' foi encontrada e pode ser atualizada.")
            
        else:
            print("\nA receita não foi encontrada.")
            return

    except FileNotFoundError:
        print("O arquivo de receitas não foi encontrado. Por favor, cadastre uma receita primeiro.")
    except Exception as e:
        print(f"Ocorreu um erro ao tentar ler o arquivo: {e}")

def apagar_receita():
    pass

def procurar_receita_por_pais():
    pass

def ver_receitas_favoritas():
    pass

def avaliar_receita():
    pass

def obter_indice_aleatorio(receitas, entrada_usuario):
    soma_caracteres = sum(len(palavra) for palavra in entrada_usuario.split())
    indice_aleatorio = soma_caracteres % len(receitas)
    return indice_aleatorio

def ver_receita_aleatoria():
    try:
        with open("receitas.txt", "r", encoding="utf-8") as file:
            receitas = file.read().split("\n===================================\n")

            if receitas:
                entrada_usuario = input("Digite algo rapidamente para gerar uma receita aleatória: ")
                indice_aleatorio = obter_indice_aleatorio(receitas, entrada_usuario)
                print(receitas[indice_aleatorio])
            else:
                print("Não há receitas cadastradas.")

    except FileNotFoundError:
        print("O arquivo de receitas não foi encontrado. Por favor, cadastre uma receita primeiro.")
    except Exception as e:
        print(f"Ocorreu um erro ao tentar ler o arquivo: {e}")


def main():
    menu()
    while True:
        opcao = input("\nEscolha uma das opções do menu: ")
        if opcao == '1':
            cadastrar_receita()
        elif opcao == '2':
            visualizar_receitas()
        elif opcao == '3':
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