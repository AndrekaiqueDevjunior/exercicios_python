#====== BIBLIOTECA ======

#Não pode cadastrar dois livros com o mesmo id.
#Só pode emprestar um livro se "disponivel" for True.
##Quando emprestar, você deve mudar "disponivel" para False.
#Não pode emprestar novamente um livro que já está emprestado.
#Na devolução, altere "disponivel" novamente para True.
#Não pode devolver um livro que já está disponível.
#Na opção 6, mostre quantos livros estão disponíveis naquele momento.




#1 - Listar livros
#2 - Cadastrar livro
#3 - Emprestar livro
#4 - Devolver livro
#5 - Buscar livro pelo título
#6 - Mostrar quantidade de livros disponíveis
#0 - Sair
livros = [
    {
    "id": 1,
    "titulo": "Python para Iniciantes",
    "autor": "Carlos Silva",
    "disponivel": True
    }
]

while True:
        print("#1 - Listar Livros")
        print("#2 - Cadastrar Livros")
        print("#3 - Emprestar Livros")
        print("#4 - Devolver  Livros")
        print("#5 - Buscar  Livros Pelo Titulo")
        print("#6 - Mostrar Quantidade de Livros Disponíveis")
        opcao = int(input("Selecione uma opção: "))

        


        if opcao == 1:


            def listar_livros(livros):
                for livro in livros:
                    print(livro)
                    return livro
                return None
            #Porque você apenas criou a função, mas provavelmente ainda não chamou ela.  
            listar_livros(livros)

        if opcao == 2:

            novo_id = len(livros) + 1
            # len = contar o total de livros
            novo_titulo = input("Insira o TITULO do Livro: ")
            novo_autor = input("Insira o autor do livro: ")
           
            def cadastrar_livros(livros, novo_id, novo_titulo,novo_autor,disponivel):


                         
                novo_livro = {
                    "id": novo_id,
                    "titulo": novo_titulo,
                    "autor": novo_autor,
                    "disponivel": True

                        }
                    
                livros.append(novo_livro)
                return livros

            cadastrar_livros(livros, novo_id, novo_titulo,novo_autor,disponivel)
        for livro in livros:
            print(livro)


        if opcao == 3:
            pesquisar_livro = input("Insira o nome do livro: ")

            def emprestar_livros(livros,pesquisar_livro):

                for livro in livros:
                    if livro["titulo"] == pesquisar_livro:
                        livro["disponivel"] = False
                        return livro
                return None

            resultado = emprestar_livros(livros, pesquisar_livro)
            print(resultado)
            
        if opcao == 4:

            titulo_devolver = input("INsira o nome do livro que deseja Devolver: ")

            def devolver_livro(livros, titulo_devolver):
                for livro in livros:
                    if livro["titulo"] == titulo_devolver:
                        livro["disponivel"] = True
                        return livro
                    else:
                        print("#Não pode devolver um livro que já está disponível.")

                return None
                    
               # if livro["titulo"] == True:
                    #print("#Não pode devolver um livro que já está disponível.")

            resultado = devolver_livro(livros, titulo_devolver)
            print(resultado)

        if opcao == 5:

            pesquisar_titulo = input("Insira o Nome do Livro ou Titulo: ")

            def pesquisar_livro(livros, pesquisar_titulo):
                for livro in livros:
                    if livro["titulo"] == pesquisar_titulo:
                        return livro
                    return None

            resultado = pesquisar_livro(livros, pesquisar_titulo)
            print(resultado)

        if opcao == 6:

            for livro in livros:
                if livro["disponivel"] == True:
                    print(livro["disponivel"])
                else:
                    print(f"Nenhum Livro Disponível")