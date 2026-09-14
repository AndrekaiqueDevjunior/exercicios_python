usuarios_site = {"André", "João", "Maria", "Carlos"}

usuarios_app = {"Maria", "Carlos", "Pedro", "Lucas"}




#unificado = usuarios_site & usuarios_app 
#diferenca = usuarios_site - usuarios_app #Próximo desafio — diferença entre conjuntos # Quem está no usuarios_site e não está no usuarios_app?

#Quais usuários estão no aplicativo, mas NÃO estão no site?
#diferenca = usuarios_app - usuarios_site

uniao = usuarios_app | usuarios_site
#O | representa a união.


#$print(unificado)
#print(diferenca)
print(uniao)














#emails = [
 #   "andre@email.com",
  #  "joao@email.com",
   #3# "andre@email.com",
    #"maria@email.com",
    #"joao@email.com"
#]


#print(f" esses sao os emails : ' nao repetindo a lista ' {set(emails)}")
#print(f" total de emails nao repetindo: {len(set(emails))}")



#A importância do set está principalmente em trabalhar com valores únicos e fazer algumas operações de conjunto de forma muito eficiente.
#Existe um operador de set para fazer interseção:             """"" &  """""