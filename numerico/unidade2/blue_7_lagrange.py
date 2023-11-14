#DISCENTES - Ingryd Medeiros

def Lagrange(x,y,V = True):
    
    # Importa a biblioteca de calculo do python
    import numpy as np
    # Importa a biblioteca de tempo do python
    import time
    # Importa a biblioteca de gráfico do python
    import matplotlib.pyplot as plt

    print("")
    print("Método de Lagrange","\n")

    # Solicita ao usuario o x0 que será utilizado para encontar o valor do y correspondente
    x0 = float(input("Insira o valor de x0 para achar o valor de y: "))
    
    # Método de interpolação pelo método de Lagrange
    def metodolagrange(x, y, x0, Visualizar = V):
        
        # Verifica se as listas x e y têm o mesmo tamanho
        if len(x) != len(y):
                print ("As listas x e y devem ter o mesmo tamanho","\n")
                
        try:
            
            # Define o comprimento da lista x
            n = len(x)
            # Inicia y0 (valor que queremos obter) em 0 
            y0 = 0
            # Inicia a iteração em 0 
            iteração = 0
                       
            # Verifica se x0 está dentro do intervalo de x
            if x0 < min(x) or x0 > max(x):
                return ("x0 deve estar dentro do intervalo de x.")
                
            # Gera um loop que precorre as linhas da lista x
            for i in range(0,n,1):
            # Inica o multiplicador para calcular o L(x) para cada linha i
                mult = 1
                iteração = i + 1
                if Visualizar == True:
                    print(f"Os valores de L são:")
                # Gera um loop que itera todas as linhas da lista x para calcular o valor do multiplicador
                for j in range(0,n,1):
                    # Verifica se os valores das colunas e linhas são diferentes
                    if j != i:
                        mult = mult * ((x0-x[j])/(x[i]-x[j])) #equação L(x)
                    if Visualizar == True:
                        # Imprime cada iteração de L(x) com seu valor correspondente
                        print("L{0}({1},{2}) = {3:.5f}".format(iteração, j+1, iteração, mult))
                
                # Calcula o valor de P(x) para o ponto x0
                y0 = y0 + y[i] * mult
                
                if Visualizar == True:
                    print('')
                    print("P({0}) = {1:.5f} + {2:.5f} * {3:.5f} = {4:.5f}\n".format(iteração, y0 + y[i] * mult, y[i], mult, y0))    
                    #Imprime a quatindade de itrações que o metodou realizou para chegar ao resultado
                    print(f"O método realizou {i+1} iteração para chegar ao resultado.","\n")
            
            # Retorna o valor de y0 para o x0
            return y0
        except:
            if Visualizar == True:
                print("Erro de interpolação")
                
    # Registra o tempo de início dos dois método
    inicio = time.time()

    # Ponto x0 para interpolação
    y0 = metodolagrange(x, y, x0)

    # Registra o tempo de término do método
    fim = time.time()

    print("Para interpolação de x = {:.5f}, y = {:.5f}".format(x0, y0),"\n")

    #Imprime o tempo que o método levou para chegar ao resultado com 4 casas decimais
    print(f"Tempo total de execução: {round(fim-inicio, 4)} segundos", "\n")

    #Define a função gráfico e seus parâmetros
    def grafico(x, y, x0):
        
        # Cria um array com valores de x 
        x_grafico = np.linspace(min(x), max(x))
        # Cria uma lista para armazenar os valores interpolados
        y_grafico = []
        # Gera um loop que itera px em cada valor de x_grafico
        for px in x_grafico:
            y_grafico.append(metodolagrange(x, y, px, Visualizar = False))

        # Plota o gráfico
        plt.figure() 
        plt.plot(x_grafico, y_grafico, color="Plum", label="Curva de interpolação")
        plt.scatter(x, y, color="black", label="Valores de (x)")
        plt.scatter(x0, metodolagrange(x, y, x0, Visualizar = False), color="red", label="Valor interpolado")
        plt.title("Interpolação Polinomial - Lagrange")
        plt.xlabel("Eixo x")
        plt.ylabel("Eixo y")
        plt.xticks(x)
        plt.yticks()
        plt.legend(loc="center left", bbox_to_anchor=(0.8, 0.6))
        plt.grid()
        plt.gca().spines['right'].set_visible(False) # Remove a borda da direita
        plt.gca().spines['top'].set_visible(False) # Remove a borda superior
        plt.show()
    
    #Chama a função gráfico e seus parametros
    grafico (x, y, x0)