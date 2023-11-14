#DISCENTES - Ingryd Medeiros  
   
def LUpivo(A,b, V = True):   
   
    # Importa a biblioteca de calculo do python
    import numpy as np
    # Importa a biblioteca de tempo do python
    import time

    print('')
    print("Método de Fatoração Lu com pivô","\n")

    def metodoLU(A, Visualizar = V):
        try:
            # Define o comprimento da matriz A
            n = len(A)
            # Cria uma matriz L que armazenar os valores da fatoração LU inferior 
            L = np.zeros((n, n))
            # Cria uma matriz U armazenar os valores da fatoração LU superior   
            U = np.zeros((n, n))
            
            # Gera um loop para percorrer cada coluna abaixo da diagonal principal
            for k in range(0,n,1):
                if Visualizar == True:   
                    # Imprime as iterações
                    print(f"Iteração {k+1}:")
                    print('')
                # Gera uma matriz L triangular inferior com valores iguais a 1 na diagonal principal
                L[k,k] = 1
                # Gera um loop para percorrer cada linha abaixo da linha k
                for i in range(k+1, n,1):
                    # Verifica se o elemento A[i,k] é diferente de zero
                    if A[i,k] != 0:
                        # Calcula o pivô
                        pivo = A[i,k]/A[k,k]
                    # Armazena o pivo na posição (i,k) da matriz L na coluna da matriz original
                    L[i,k] = pivo
                # Atualiza os elementos de A abaixo da linha k e coluna k
                    for j in range(k+1, n):
                        A[i,j] = A[i,j] - pivo*A[k,j]
                for j in range(k, n):
                    # Copia os elementos da linha k de A para a linha k de U
                    U[k,j] = A[k,j]
                    # Se k é diferente de j, atualiza os elementos de A abaixo da diagonal principal com os valores correspondentes para a matriz L
                    if k != j:
                        for i in range(k+1, n):
                            A[i,j] = A[i,j] - U[k,j]*L[i,k]

                if Visualizar == True:
                    # Função da biblioteca NumPy para imprimir os valores da matriz U com duas casas decimais (útil na impressão de valores muito pequenos ou grandes)
                    np.set_printoptions(precision=3, suppress=True)
                    # Imprime a matriz U que armazena os valores da fatoração LU
                    print("Matriz U:")
                    print(U)
                    print('')
                    # Imprime a matriz L que armazena os valores da fatoração LU
                    print("Matriz L:")
                    print(L)
                    print('')
            
            #Imprime a quatindade de itrações que o metodou realizou para chegar ao resultado
            print(f"O método realizou {i+1} iteração para chegar ao resultado.")   
            # Retorna as matrizes L e U
            return L, U                   
        except:
            if Visualizar:
                print("O sistema linear não convergiu")
    
    # Função de retrosubstituição
    def metodosub(L, U, b, Visualizar = V):
        
        if Visualizar == True: 
            print("")  
            print("Retrosubistituição de LU","\n")

        # Define o comprimento de L
        n = len(L)
        # Cria um vetor y com tamanho n de elementos iguais a (0) para armazenar o resultado de y
        y = np.zeros(n)
        # Cria um vetor x com n de elementos iguais a (0) para armazenar o resultado de x
        x = np.zeros(n)
        
        # Resolvendo o sistema Ly = b
        if Visualizar == True:
            print("A solução do sistema Ly = b é:","\n")
        # Gera um loop que percorre as linhas da matriz L e do vetor b
        for i in range(0,n,1):
            # Inicia a soma = 0 para armazenar o resultado da multiplicação dos valores de L e y
            soma = 0
            # Gera um loop que percorre as colunas da matriz L e do vetor y até a posição i-1
            for j in range(0,i,1):
            # Calcula o produto de L e y e soma com o resultado anterior, depois armazena a soma
                soma = soma + L[i,j]*y[j]
            # Calcula o valor (y) por meio do valor de b[i] - soma anterior, e então divide resultado pelo valor de L na diagonal principal da linha i            
            y[i] = b[i] - soma
            if Visualizar == True:
                #Imprime o calculo da retrosubistituição para cada iteração
                print(f"y{i} = {b[i]} - ({soma:.5f}) = {y[i]:.5f}")

        # Resolvendo o sistema Ux = y
        if Visualizar == True:
            print("A solução do sistema Ux = y é:","\n")
        # Gera um loop que itera os índices da matriz U de baixo para cima, com inicio na última linha
        for i in range(n-1, -1, -1):
            # Inicia a soma = 0 para armazenar o resultado da multiplicação dos valores de U e x
            soma = 0
            # Gera um loop que percorre as colunas da matriz U de baixo para cima, iniciando na coluna i+1 até a primeira coluna
            for j in range(i+1, n, 1): 
                # Calcula o produto de U e x e soma com o resultado anterior, depois armazena a soma
                soma = soma + U[i][j] * x[j]  
            # Calcula o valor (x) por meio do valor de y[i] - soma anterior, e então divide o resultado pelo valor de U na diagonal principal da linha i
            x[i] = (y[i] - soma) / U[i][i] 
            if Visualizar == True:
                #Imprime o calculo da retrosubistituição para cada iteração
                print(f"x{i} = ({y[i]:.5f} - ({soma:.5f})) / ({U[i,i]:.5f}) = {x[i]:.5f}")        

        # Retorna o vetor solução x
        return x
    
    # Registra o tempo de início do método
    inicio = time.time()

    # Chama a função fatoração LU e seus parametros
    L, U = metodoLU(A) 
    
    # Chama a função retrosubstituição para y e x e seus parametros
    x = metodosub(L, U, b) 
    
    # Registra o tempo de término do método
    fim = time.time()
    
    # Imprime a solução com 5 casas decimais utilizando a função round (arredondar) do python
    print("\n"f"A solução aproximada do sistema é:", [round(valorx, 5) for valorx in x],"\n")
    #Imprime o tempo que o método levou para chegar ao resultado com 4 casas decimais
    print(f"Tempo total de execução: {fim-inicio:.4f} segundos","\n")