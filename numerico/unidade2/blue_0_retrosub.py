#DISCENTES - Ingryd Medeiros

def Retrosubstituição(A,b,V = True):
    
    # Importa a biblioteca de calculo do python
    import numpy as np
    # Importa a biblioteca de tempo do python
    import time

    print('')
    print("Função de Retrosubstituição")
    print('')

    # Método de retrosubstituição
    # Recebe uma matriz triangular superior A e um vetor b e retorna a solução do sistema Ax=b
    def metodosub(A, b, Visualizar = V):
        
        try:  
            # Define o comprimento do vetor b
            n = len(b) 
            # Cria um vetor x com n de elementos iguais a (0) para armazenar o resultado de x
            x = np.zeros(n) 
            # Inicia a iteração em 0 
            interacao = 0
            
            # Imprime a mensagem de início das iterações
            if Visualizar == True:
                print("As iterações são:" "\n")
            
            # Gera um loop que itera os índices da matriz A de baixo para cima, com inicio na última linha
            for i in range(n-1,-1,-1):
                # Inicia a soma = 0 para armazenar o resultado da soma anterior + a multiplicação da matriz A e do vetor Xk
                soma = 0 
                # Gera um loop que percorre as colunas da matriz A a partir da coluna i+1 até a primeira coluna
                for j in range(i+1,n,1): 
                    # Calcula o produto de A e x e soma com o resultado anterior, depois armazena a soma
                    soma = soma + A[i][j]*x[j]
                # Calcula o valor (x) por meio do valor de b[i] - soma anterior, e então divide o resultado pelo valor de A na diagonal principal da linha i
                x[i] = (b[i]-soma)/(A[i][i])
                
                # Imprime o calculo da retrosubistituição e o resultado para cada iteração com arredondamento de 5 casas decimais
                if Visualizar == True:
                    print(f"x{i}: ({b[i]}-{soma})/({A[i][i]}) = {round(x[i], 5)}")
                    print('')
                
            #Imprime a quatindade de itrações que o metodou realizou para chegar ao resultado
            print(f"O método realizou {interacao+1} iteração para chegar ao resultado.","\n")
            # Retorna o vetor solução x
            return x 
        except:
            if Visualizar == True:
                print("O sistema linear não convergiu")
                
    # Inicia o cronômetro para medir o tempo de  execução do código e salva em segundos 
    inicio = time.time()
    
    # Chama a função retrosubstituição e seus parametros
    x = metodosub(A, b)
    
    # Finaliza o cronometro e armazena o tempo final que o codigo levou para chegar em uma resolução do método implementado
    fim = time.time()
    #Imprime o tempo que o código levou para chegar ao resultado com 4 casas decimais
    print(f"Tempo total de execução: {fim-inicio:.4f} segundos", "\n")
    # Imprime a solução com 5 casas decimais utilizando a função round (arredondar) do python
    print("A solução aproximada do sistema é:", [round(valorx, 5) for valorx in x], "\n")
