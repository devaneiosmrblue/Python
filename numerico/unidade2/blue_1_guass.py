#DISCENTES - Ingryd Medeiros

def Eliminação_Guass(A,b,V = True):
    
    # Importa a biblioteca de calculo do python
    import numpy as np
    # Importa a biblioteca de tempo do python
    import time
 
    print('')
    print("Método de Eliminação de Gauss","\n")
    
    # Método de Eliminação de Guass
    def metodogauss(A, b, Visualizar = V):
        
        try:    
            # Define o comprimento do vetor b
            n = len(b) 
            # Cria um vetor x com n de elementos iguais a (0) para armazenar o resultado de x
            x = np.zeros(n) 
            
            # Gera um loop para percorrer cada coluna abaixo da diagonal principal
            for k in range(n-1):
                # Gera um loop para percorrer cada linha abaixo da linha k
                for i in range(k+1,n,1):
                    # Verifica se o elemento A[i,k] é diferente de zero
                    if A[i,k] != 0:
                        # Calcula o pivô
                        pivo = A[k,k] / A[i,k]
                        # Atualiza os elementos de A abaixo da linha k e coluna k
                        for j in range(k, n):
                            A[i,j] = A[k,j] - A[i,j] * pivo
                        # Atualiza os elementos de b abaixo da linha k
                        b[i] = b[k] - b[i] * pivo
                    
                    #Imprime a matriz A e o vetor b para cada iteração
                    if Visualizar == True:
                        print(f"Iteração {k+1} - Matriz A:\n{A}")
                        print('')
                        print(f"Iteração {k+1} - Vetor b: [{', '.join(str(b) for b in b)}]")
                        print('')
                        
            #Imprime a quatindade de itrações que o metodou realizou para chegar ao resultado
            print(f"O método realizou {k+1} iteração para chegar ao resultado.")
            # Retorna a matriz A e o vetor b
            return A,b
        except:
            if Visualizar == True:
                print("O sistema linear não convergiu")
            
    # Imprime a matriz escalonada calculada por meio do metodo de gauss
    def metodosub(A, b):

        # Define o comprimento do vetor b
        n = len(b) 
        # Cria um vetor x com n de elementos iguais a (0) para armazenar o resultado de x
        x = np.zeros(n) 
        
        # Gera um loop que itera os índices da matriz A de baixo para cima, com inicio na última linha
        for i in range(n-1,-1,-1):
            # Inicia a soma = 0 para armazenar o resultado da multiplicação
            soma = 0 
            # Gera um loop que percorre as colunas da matriz A a partir da coluna i+1 até a primeira coluna
            for j in range(i+1,n-1,1):
                # Calcula o produto de A e x e soma com o resultado anterior, depois armazena a soma
                soma = soma + A[i][j]*x[j] 
            # Calcula o valor (x) por meio do valor de b[i] - soma anterior, e então divide o resultado pelo valor de A na diagonal principal da linha i
            x[i] = (b[i]-soma)/(A[i][i]) 
        # Retorna o vetor solução x
        return x 

    # Registra o tempo de início dos dois método
    inicio = time.time()

    # Chama a função eliminação de gauss e seus parametros
    A,b = metodogauss(A,b)
    # Chama a função retrosubstituição e seus parametros
    x = metodosub(A, b)

    # Registra o tempo de término do dois método
    fim = time.time()

    # Imprime a solução com 5 casas decimais utilizando a função round (arredondar) do python
    print("\n"f"A solução aproximada do sistema é:", [round(valorx, 5) for valorx in x],"\n")
    #Imprime o tempo que os métodos levou para chegar ao resultado com 4 casas decimais
    print(f"Tempo total de execução: {fim-inicio:.4f} segundos", "\n")
