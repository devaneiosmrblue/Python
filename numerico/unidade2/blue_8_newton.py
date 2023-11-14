#DISCENTES - Ingryd Medeiros

def Newton(x,y,V = True):
    
    # Importar a biblioteca de calculo do python
    import numpy as np
    # Importar a biblioteca de tempo do python
    import time
    # Importar a biblioteca de gráfico do python
    import matplotlib.pyplot as plt

    print("")
    print("Método das diferenças dividias (Newton)","\n")
    
    # Solicita ao usuario o x0 que será utilizado para encontar o valor do y correspondente
    x0 = float(input("Insira o valor de x0 para achar o valor correspondente de y: "))
    print('')
    
    # Método de interpolação pelo método das diferenças divididas
    def newton(x, y, x0, Visualizar = V):
    
       # Verifica se as listas x e y têm o mesmo tamanho
        if len(x) != len(y):
                print ("As listas x e y devem ter o mesmo tamanho","\n")
        try:          
            # Define o comprimento da lista x  
            n = len(x)
            # Inicia y0 (valor que queremos obter) em 0 
            y0 = 0
            # Cria uma lista vazia para armazenar os valores calculados das diferenças divididas
            dif_div = []
            
            # Gera uma lista da tabela dif_div com n elementos iguais a zero para armazenar os valores das diferenças divididas
            for tabela in range(n):
                tabela = np.zeros(n)
                dif_div.append(tabela)
                
            # Gera um loop que itera até a primeira coluna da tabela de diferenças divididas serem preenchidas com os valores de y
            for i in range(n):
                dif_div[i][0] = y[i]

            # Gera um loop itera sobre as colunas da tabela dif_div e atualiza o valor da diferença dividida 
            for j in range(1, n):
                # Gera um loop itera sobre as linhas da tabela dif_div e atualiza o valor da diferença dividida
                for i in range(n - j):
                    # Calcula as diferenças divididas da tabela de valores de x e y para obter os coeficientes do polinômio
                    dif_div[i][j] = (dif_div[i + 1][j - 1] - dif_div[i][j - 1]) / (x[i + j] - x[i])
                    if Visualizar == True:
                        # Imprime o calculo das diferenças divididas
                        print("Diferença dividida d[{}][{}] = ({} - {}) / ({:.5f} - {:.5f}) = {:.5f}".format(i, j, dif_div[i + 1][j - 1], dif_div[i][j - 1], x[i + j], x[i], dif_div[i][j]))

            # Armazenar o valor inical nas diferenças dividias da linha 0 e coluna 0 
            y0 = dif_div[0][0]
            
            # Gera um loop que itera sobre as colunas e calcula os coeficientes do polinômio interpolador através das diferenças divididas
            for j in range(1, n):
                if Visualizar == True:
                    print("\n""Iteração {}".format(j+1))
                # Armazena o resultado das colunas calculadas nas diferenças divididas 
                resultado = dif_div[0][j]
            # Gera um loop que itera sobre j e calcula a multiplicação entre o valor armazenado e a diferença entre os valores de x da tabela dif_div
                for i in range(j):
                    # Calcula a multiplicação entre do valor atual de resultado e a diferença entre x0 e x[i] das linhas
                    resultado = resultado * (x0 - x[i])
                # Armazena o valor de y0 atual + o valor de resultado anterior até finalizar o loop e chegar no y0 correspondente a x0
                y0 = y0 + resultado
                
                # Imprime cada iteração de de x0 e y0 até chegar ao y0 correspondete ao x0 que o usuario digitou
                if Visualizar == True:
                    print("Para x0 =", round(x0, 5))
                    print("Temos y0 =", round(y0, 5))
            # Retorna o valor de y0 para o x0
            return y0
        except:
            if Visualizar == True:
                print("Erro de interpolação")
    
    # Registra o tempo de início dos dois método
    inicio = time.time()

    y0 = newton(x, y, x0)

    # Registra o tempo de término do método
    fim = time.time()

    print("\n""Para interpolação de x = {:.5f}, y = {:.5f}".format(x0, y0),"\n")

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
            y_grafico.append(newton(x, y, px, Visualizar = False))

        # Plota o gráfico
        plt.figure() 
        plt.plot(x_grafico, y_grafico, color="Plum", label="Curva de interpolação")
        plt.scatter(x, y, color="black", label="Valores de (x)")
        plt.scatter(x0, newton(x, y, x0, Visualizar = False), color="red", label="Valor interpolado")
        plt.title("Interpolação Polinomial - Newton")
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
    grafico(x, y, x0)