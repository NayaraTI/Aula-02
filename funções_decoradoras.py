### As funções decoradoras potencializam
# ou substituem a lógica de funcionamento de outra função 
# ou método

##  Criando uma função decoradora

def master(msg):
    def imprime():
        print("Essa é a função Pai ou decoradora")
        msg() ## A Função que vai ser empoderada
        return imprime

### Segunda Função que irá executar junto com a função decoradora

@master                                 # função decorada!!!
def segunda_funcao():
    print("Está chamando a segunda Função")
       
    
    
    ## Executar as funções
    
    segunda_funcao()
    
    ## Decoração tipo phyton 2
    #chama_funcao = master(segunda_funcao)
    
    def decoradora(valor):
        def imprime(*args):
            print("Multiplicação Executada")
            return valor(*args)
        return imprime
    
    @decoradora
    def multiplica(a,b):
        return a*b
    
    print(multiplica(2,3))
