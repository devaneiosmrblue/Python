#DISCENTES - Ingryd Medeiros

def Interpolação_polinomail(x,y,V = True):
    
    # Importa a biblioteca de calculo do python
    import numpy as np
    # Importa a biblioteca de tempo do python
    import time
    # Importa a biblioteca de gráfico do python
    import matplotlib.pyplot as plt
    
    print('')
    print("Interpolação Polinomial","\n")
    
    # Método de Interpolação polinomial
    def metodointerpolação(x, y, Visualizar = V):
        
        # Verifica se as listas x e y têm o mesmo tamanho
        if len(x) != len(y):
                print ("As listas x e y devem ter o mesmo tamanho","\n")
        try:
            
            # Define o comprimento da lista x
            n = len(x)
            # Cria uma matriz A com tamanho n x n de elementos iguais a (0)
            A = np.zeros((n, n))
            # Cria uma vator b com tamanho n de elementos iguais a (0)
            b = np.zeros((n))
            # Inicia a iteração em 0 
            interacao = 0

            # Gera um loop que precorre as linha da matriz A o vetor b
            for i in range(0,n,1):
                # Gera uma matriz A com valores iguais a 1 na primeira coluna
                A[i,0] = 1
                # Gera um loop que itera sobre as colunas da matriz A, exceto pela última coluna
                for j in range(0,n-1,1):
                # Calcula o produto da coluna atual j na matriz A, depois armazena o produto na próxima coluna j+1 na mesma linha da matriz A.                    A[i,j+1] = A[i,j] * x[i]
                    A[i,j+1] = A[i,j] * x[i]
                # Gera um vetor b com os valores de y
                b[i] = y[i]   
                
            if Visualizar == True:
                # Imprime a matriz A e o vetor b e suas iterações
                print(f"Iteração {interacao+1}:", "\n")
                np.set_printoptions(precision=3, suppress=True)
                print(f"Matriz A:", "\n", A, "\n")
                print(f"Vetor b:", b, "\n")
                    
            if Visualizar == True:
                # Imprime a matriz A e o vetor b final
                np.set_printoptions(precision=3, suppress=True)
                print(f"Matriz final A:", "\n", A, "\n")
                print(f"Vetor final b:", b, "\n")

            #Imprime a quatindade de itrações que o metodou realizou para chegar ao resultado
            print(f"O método realizou {interacao+1} iteração para chegar ao resultado.","\n")
            
            # Retorna a matriz A e o vetor b
            return A, b
        except:
            if Visualizar == True:
                print("Erro de interpolação")
                
    # Registra o tempo de início dos dois método
    inicio = time.time()

    # Chama a função interpolação seus parametros
    A, b = metodointerpolação(x, y)

    # Resolve o sistema linear Ax=b para encontrar os coeficientes da interpolação usando a biblioteca numpy
    fatorx = np.linalg.solve(A, b)

    # Imprime a solução com 5 casas decimais utilizando a função round (arredondar) do python
    print("Os coefientes da interpolação polinomial são:", [round(valorx, 5) for valorx in fatorx],"\n") 
    
    # Imprime o texto inical sobre os valores de P(X)
    print("Os valores de P(x) são:", "\n")

    # Cria uma lista para armazenar os valores de P(x)
    lista_x = []

    # Iterando o valor de x em x
    for valor_x in x:
        
        # Cria variáveis com os valores dos coeficeinetes da interpolação
        a0, a1, a2 = round(fatorx[0], 5), round(fatorx[1], 5), round(fatorx[2], 5)
        # Gera uma equação de interpolação polinomial para P(x)
        equaçãopoli = (f"P(x) = {a0} + {a1}({valor_x}) + {a2}({valor_x})^2")
        # Calcula o valor de P(x) para o valor atual de x e armazenando o resultado
        Px = fatorx[0] + fatorx[1]*valor_x + fatorx[2]*valor_x**2
            
        # Imprime o valor de P(x) para o valor atual de x, junto com a equação polinomial correspondente
        print(f"Para x = {valor_x}: {equaçãopoli} = {Px:.2f}", "\n")
            
        # Armazena o valor de P(x) na lista valores_x
        lista_x.append(Px)
    
    # Registra o tempo de término do método
    fim = time.time()

    #Imprime o tempo que o método levou para chegar ao resultado com 4 casas decimais
    print(f"Tempo total de execução: {round(fim-inicio, 4)} segundos", "\n")

    #Define a função gráfico e seus parâmetros
    def grafico(x, y, fatorx):
        
        # Cria um array com valores de x 
        x_grafico = np.linspace(min(x), max(x))
        # Cria uma lista para armazenar os valores interpolados
        y_grafico = []
        # Gera um loop que itera px em cada valor de x_grafico
        for px in x_grafico:
            y_grafico.append(fatorx[0] + fatorx[1]*px + fatorx[2]*px**2)
            
        # Plota o gráfico
        plt.figure() 
        plt.plot(x_grafico, y_grafico, color="Plum", label="Curva de interpolação")
        plt.scatter(x, y, color="black", label="Valores de (x)", s=50)
        plt.title("Interpolação Polinomial")
        plt.xlabel("Eixo x")
        plt.ylabel("Eixo y")
        plt.xticks()
        plt.yticks()
        plt.xlim()
        plt.ylim()
        plt.legend(loc="center left", bbox_to_anchor=(0.8, 0.6))
        plt.grid()
        plt.gca().spines['right'].set_visible(False) # Remove a borda da direita
        plt.gca().spines['top'].set_visible(False) # Remove a borda superior
        plt.show()
        
    #Chama a função gráfico e seus parametros
    grafico(x, y, fatorx)
