#DISCENTES - Ingryd Medeiros

def secante(f):
    
    #Importação a biblioteca de gráficos do python
    import matplotlib.pyplot as plt
    # Importação a biblioteca de calculo do python
    import numpy as np
    # Importar o arquivo isolamento de raiz, apelidado de (iso)
    import biblioteca_isolamento_raiz as iso
    #importação para numeros matematicos mais complexos
    import math

    print('') 
    print("O método usado é o secante")
    print('') 

    #definir os intervalos de inicio e fim mais o passo
    i=float(input("Insira o limite inical do intervalo de busca para achar uma raiz: "))
    j=float(input("Insira o limite final do intervalo de busca para achar uma raiz: "))
    h=float(input("Insira o passo desejado: "))
    print('')


    #Definir a função secante e quais parametros ela recebe 
    def metodosecante(f, x0, x1, e, imax):
        try:
            repetição = 0 
            while repetição <= imax:
                if repetição == 0:
            #Imprime as informações desejadas da iteração x e f(x)
                    print(f"Iteração {repetição}: x{repetição} = {x0:.10f}, f(x) = {f(x0):.10f}")
                print(f"Iteração {repetição+1}: x{repetição+1} = {x1:.10f}, f(x) = {f(x1):.10f}")
                x2 = x1 - (f(x1)*(x1 - x0))/(f(x1)-f(x0))
                x0 = x1
                x1 = x2
                if abs(f(x2)) < e:
                    print(f"Iteração {repetição+2}: x{repetição+2} = {x2:.10f}, f(x) = {f(x2):.10f}")
                    print(f'A raiz aproximada é: {x2:.10f} com {repetição+1} iterações')
            #Imprime a raiz encontrada e o número de iterações
                    break 
                elif repetição == imax:
                    print("A função não convergiu")
                    break
                repetição = repetição+1 
            return x2
        except:
            print("A função não convergiu")

    #Chamar a função isalamento de raiz e seus parametros
    iso.isolamento_de_raiz(f,i,j,h)
    print('') 

    #Caso queira mostrar os intervalos onde possa ter raizes basta implementar o metodo de isolamento de raizes
    x0=float(input("Digite o chute inical x0, com base no intervalo de raiz existente: "))
    x1=float(input("Digite o chute final x1, com base no intervalo de raiz existente: "))
    e=float(input("Digite a precisão desejada: "))
    imax = float(input("Digite a iteração máxima (∈ = Z): "))
    print('') 

    #Chama a função do método da secante para encontrar a raiz
    x2 = metodosecante(f, x0, x1, e, imax)

    # Definir o intervalo e os pontos da função
    x = np.linspace(i, j, 1000)
    y = f(x)
    fig, ax = plt.subplots()
    ax.plot(x, y, label='f(x)')
    ax.axhline(y=0, color='black', linestyle='-')
    #Cria um gráfico com x no eixo horizontal e f(x) no eixo vertical, onde f(x) é uma função dada.
    ax.axvline(x=x2, color='purple', linestyle='-', label='Raiz')
    #Cria um segundo gráfico com x no eixo horizontal e dy(x) no eixo vertical, onde dy(x) é outra função relacionada à f(x)
    plt.title('Gráfico de f(x)')
    plt.xlabel('Eixo X')
    plt.ylabel('Eixo Y')
    ax.set_ylim(-35, 35)
    ax.legend()
    plt.grid()
    plt.show()