#DISCENTES - Ingryd Medeiros

def Jacobi(A,b,V = True):
    
    # Importa a biblioteca de calculo do python
    import numpy as np
    # Importa a biblioteca de tempo do python
    import time

    print('')
    print("Método Gauss-Jacobi","\n")

    e = float(input("Digite a presição desejada: "))
    imax = float(input("Digite o número de iterações desejada: "))
    print('')

    # Método de Guass Jacobi
    def metodojacobi(A, b, e, imax, Visualizar = V):
        
        try:
            
            # Define o comprimento do vetor b
            n = len(b)
            # Define a variável de iteração com valor zero 
            interacao = 0
            # Cria um vetor xk com tamanho n de elementos iguais a (0), o vetor xk irá armazenar a solução aproximada da iteração atual
            xk = np.zeros(n) 

            # Define o vetor inicial xk
            for i in range(n):
                # Calcula a aproximação inicial do valor da solução do sistema e armazena o resultado no elemento i do vetor xk
                xk[i] = b[i] / A[i][i]
            
            if Visualizar == True:
                # Imprime o valor inicial de xk para a iteração 0    
                print(f"x{interacao}: ({', '.join(str(x) for x in xk)})")
                # join(str()) é uma função embutido do pyhton que transforma o elementos de xk é uma string e os separa por virgula
                print('')

            # Gera um loop que itera xk enquanto ele for menor que o valor máximo de iterações digitado pelo usuario
            while interacao < imax:
                # Incrementa a contagem de iterações
                interacao = interacao + 1
                # Cria uma cópia do vetor xk para armazenar a solução da iteração anterior
                x0 = xk.copy() 
                
                # Gera um loop que itera os índices da matriz A e do vator b para atualizar o vetor xk com novas estimativas da solução
                for i in range(0,n,1):
                    # Inicia a soma = 0 para armazenar o resultado da soma anterior + a multiplicação da matriz A e do vetor Xk
                    soma = 0
                    # Gera um loop que itera todos os índices de coluna da matriz A e do vetor xk, exceto a coluna i, que é a coluna atual do for de i
                    for j in range(0,n,1):
                    # Verifica se i é diferente de j para calcular a multiplicação entre a matriz A e o vetor x0 
                        if i != j:
                            # Calcula o produto de A e x0 e soma com o resultado anterior, depois armazena a soma
                            soma = soma + A[i][j] * x0[j]
                    # Calcula o novo valor do elemento i do vetor xk utilizando o método de Gauss-Jacobi
                    xk[i] = (1 / A[i][i]) * (b[i] - soma)
            
                if Visualizar == True:
                    # Imprime os valores de xk para a iteração atual
                    print(f"x{interacao}:", xk)
                
            # Calcula a distância entre os valores de xk atual e anterior (valores em modulo)
                dist = (abs(xk - x0))
                # Calcula o distância relativa usando a distancia anterior e o valor máximo atual de xk (valores em modulo)
                dist_rel = (dist/ max(abs(xk)))
                # Calcula o valor máximo da distancia relativa
                dist_max = max(dist_rel)
                
                if Visualizar == True:
                    # Imprime a soluçao da distancia relativa máxima com 10 casas decimais utilizando a função round (arredondar) do python
                    print(f"Distância máxima aproximada {interacao}: {round(dist_max, 10)}")
                    print('')
                    
                # Verifica se valor máximo da distancia relativa é menor que a precisão
                if dist_max < e:
                    # Interrompe o loop while e retorna o vetor xk que representa a solução aproximada do sistema
                    break
                # Verifica se o número máximo de iterações foi alcançado e exibe a mensagem de erro
                elif interacao == imax:
                    if Visualizar == True:
                        print("Número máximo de iterações alcançado, sistema não convergiu")
                # Verifica se nenhuma das condições anteriores foi atendida e continua para a próxima iteração
                else:
                    continue
                
            #Imprime a quatindade de itrações que o metodou realizou para chegar ao resultado
            print(f"O método realizou {interacao+1} iteração para chegar ao resultado.")
            # Retorna o vetor solução xk
            return xk
        except:
            if Visualizar == True:
                print("O sistema linear não convergiu")

    # Registra o tempo de início do método
    inicio = time.time()   
        
    # Chama a função Gauss Seidel seus parametros
    x = metodojacobi(A, b, e, imax)
    
    # Registra o tempo de término do método
    fim = time.time()
    
    # Imprime a solução com 5 casas decimais utilizando a função round (arredondar) do python
    print("\n"f"A solução aproximada do sistema é:", [round(valorx, 10) for valorx in x],"\n")
    #Imprime o tempo que o método levou para chegar ao resultado com 4 casas decimais
    print(f"Tempo total de execução: {fim-inicio:.4f} segundos")

