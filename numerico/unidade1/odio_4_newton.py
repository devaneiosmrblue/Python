#DISCENTES - Ingryd Medeiros

def newtonraphson(f):

    #Importação a biblioteca de gráficos do python
    import matplotlib.pyplot as plt
    # Importação a biblioteca de calculo do python
    import numpy as np
    # Importar o arquivo isolamento de raiz, apelidado de (iso)
    import biblioteca_isolamento_raiz as iso
    #importação para numeros matematicos mais complexos
    import math

    print('')
    print("O método usado é Newton-Raphson")
    print('')

    #definir os intervalos de inicio e fim mais o passo
    i=float(input("Insira o limite inical do intervalo de busca para achar uma raiz: "))
    j=float(input("Insira o limite final do intervalo de busca para achar uma raiz: "))
    h=float(input("Insira o passo desejado: "))
    print('')

    def dev(f, x):
        h = 1e-10
        return (f(x+h) - f(x)) / h

    #Definir a função newtonraphson e quais parametros ela recebe
    def metodonewtonraphson(f, dev, x0, e, imax):
        try:
            repeticao = 0
            x1 = x0
            while repeticao <= imax:
                # Imprime as informações desejadas da iteração x e f(x)
                print(f"Iteração {repeticao}: x{repeticao} = {x1:.10f}, f(x) = {f(x1):.10f}")
                if abs(f(x1)) < e:
                    print(f"A raiz aproximada é: {x1:.10f} com {repeticao} iterações")
                    break
                elif repeticao == imax:
                # Imprime a raiz encontrada e o número de iterações
                    print("A função não convergiu")
                x1 = x1 - f(x1)/dev(f,x1)
                repeticao = repeticao+1
            return x1
        except:
            print("A função não convergiu")

    #Chamar a função isalamento de raiz e seus parametros
    iso.isolamento_de_raiz(f,i,j,h)
    print('')

    #Definir os parametros desejados
    x0=float(input("Digite o chute inical x0, com base no intervalo de raiz existente: "))
    e=float(input("Digite a precisão desejada: "))
    imax = float(input("Digite a iteração máxima (∈ = Z): "))

    #Chama a função do método do newtonraphson para encontrar a raiz
    x1 = metodonewtonraphson(f, dev, x0, e, imax)

    # Definir o intervalo e os pontos da função
    x = np.linspace(i, j)
    y = f(x)
    dy = dev(f,x)
    fig, ax = plt.subplots()
    ax.plot(x, y, label='f(x)')
    #Cria um gráfico com x no eixo horizontal e f(x) no eixo vertical, onde f(x) é uma função dada.
    ax.plot(x, dy, label='dev(x)')
    #Cria um segundo gráfico com x no eixo horizontal e dy(x) no eixo vertical, onde dy(x) é outra função relacionada à f(x)
    ax.axhline(y=0, color='black', linestyle='-')
    ax.axvline(x=x1, color='purple', linestyle='-', label='Raiz')
    plt.title('Gráfico de f(x) e dev (x)')
    plt.xlabel('Eixo X')
    plt.ylabel('Eixo Y')
    ax.set_ylim(-35, 35)
    ax.legend()
    plt.grid()
    plt.show()


