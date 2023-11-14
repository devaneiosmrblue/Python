#DISCENTES - Ingryd Medeiros

def pontofixo(f, phi):

    #Importação a biblioteca de gráficos do python
    import matplotlib.pyplot as plt
    # Importação a biblioteca de calculo do python
    import numpy as np
    # Importar o arquivo isolamento de raiz, apelidado de (iso)
    import biblioteca_isolamento_raiz as iso
    #importação para numeros matematicos mais complexos
    import math


    print('')
    print("O método usado é ponto fixo")
    print('')

    #definir os intervalos de inicio e fim mais o passo
    i=float(input("Insira o limite inical do intervalo de busca para achar uma raiz: "))
    j=float(input("Insira o limite final do intervalo de busca para achar uma raiz: "))
    h=float(input("Insira o passo desejado: "))
    print('')
    
    #Definir a função pontofixo e quais parametros ela recebe 
    def metodopontofixo(f, phi, x0, e, imax):
        try: 
            repetição = 0  
            x1 = x0   
            while repetição <= imax:
                x1 = phi(x1) 
            # Imprime as informações desejadas da iteração x e f(x)
                print(f"Iteração {repetição}: x{repetição} = {x1:.10f}, f(x) = {f(x1):.10f}") 
                repetição = repetição + 1 
                if abs(f(x1)) < e:
            # Imprime a raiz encontrada e o número de iterações
                    print(f"A raiz aproximada é: {x1:.10f} com {repetição} iterações")
                    break
            #Se no elif ele não achar a raiz, ele faz uma nova compração até a repetição chegar ao imax
                elif repetição == imax: 
                    print("A função não convergiu")
            return x1
        #Se não achar a raiz, ele imprime:
        except:
            print("A função não convergiu")

    #Chamar a função isalamento de raiz e seus parametros
    iso.isolamento_de_raiz(f,i,j,h)
    print('') 

    #Definir os parametros desejados
    x0=float(input("Digite o chute inical x0, com base no intervalo de raiz existente: "))
    e=float(input("Digite a precisão desejada: "))
    imax = float(input("Digite a iteração máxima (∈ = Z): "))
    print('') 

    #Chama a função do método do ponto fixo para encontrar a raiz
    x1 = metodopontofixo(f, phi, x0, e, imax)

    #Definir a função grafico e seus parametros
    x = np.linspace(i, j, 1000)
    fig, ax = plt.subplots()
    ax.plot(x, f(x), label='f(x)') 
    #Cria um gráfico com x no eixo horizontal e f(x) no eixo vertical, onde f(x) é uma função dada.
    ax.plot(x, phi(x), label='phi(x)')
    #Cria um segundo gráfico com x no eixo horizontal e phi(x) no eixo vertical, onde phi(x) é outra função relacionada à f(x)
    ax.axhline(y=0, color='black', linestyle='-')
    #Cria uma linha horizontal ao gráfico na posição y=0
    ax.axvline(x=x1, color='purple', linestyle='-', label='Raiz')
    #Cria uma linha vertical ao gráfico na posição x=x1
    plt.title('Grafico de f(x) e phi(x)')
    plt.xlabel('Eixo X')
    plt.ylabel('Eixo Y')
    ax.set_ylim(-35,35)
    ax.legend()
    plt.grid()
    plt.show()