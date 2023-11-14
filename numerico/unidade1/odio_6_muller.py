#DISCENTES - Ingryd Medeiros

def muller(f):

   #Importação a biblioteca de gráficos do python
    import matplotlib.pyplot as plt
    # Importação a biblioteca de calculo do python
    import numpy as np
    # Importar o arquivo isolamento de raiz, apelidado de (iso)
    import biblioteca_isolamento_raiz as iso
    #importação para numeros matematicos mais complexos
    import math

    print('') 
    print("O método usado é o Muller")
    print('') 

    #Definir os intervalos de inicio e fim mais o passo
    i=float(input("Insira o limite inical do intervalo de busca para achar uma raiz: "))
    j=float(input("Insira o limite final do intervalo de busca para achar uma raiz: "))
    h=float(input("Insira o passo desejado: "))
    print('')

    #Definir as variaveis da função muller para utilizar no metodo 
    def funcaomuller(f, x0, x1, x2): 
        p0 = f(x0)
        p1 = f(x1)
        p2 = f(x2)
        h0 = x1 - x0
        h1 = x2 - x1
        a = (h1*h1*(p0 - p1) - h0*h0*(p1 - p2)) / (h0*h1*(h0 - h1))
        b = (p1 - p0) / h0 + a*h0
        c = p0
        return a, b, c, h0, h1

    def bhaskara(a, b, c):
        return (b**2 - 4*a*c)**0.5

    #Definir a função muller e quais parametros ela recebe 
    def metodomuller(f, p0, p1, p2, e, imax):
        try:
            a, b, c, h0, h1 = funcaomuller(f, p0, p1, p2)
            d0 = (f(p1) - f(p0)) / (p1 - p0)
            d1 = (f(p2) - f(p1)) / (p2 - p1)
            a = (d1 - d0) / (p2 - p0)
            b = a * (p2 - p1) + d1
            c = f(p2)
            delta = bhaskara(a, b, c)
            
            if delta < 0:
                print("Não é possível calcular raízes complexas")
            if abs(b-delta) < abs(b+delta): 
                x3 = p2-2*c/(b+delta)
            else:
                x3 = p2-2*c/(b-delta)
            print(f"Iteração 0: x0 = {p0:.10f}, x1 = {p1:.10f}, x2 = {p2:.10f}, x3 = {x3:.10f}, f(x3) = {f(x3):.10f}")
            
            repeticao = 1 
            while repeticao <= imax:
                p0, p1, p2 = p1, p2, x3
                a, b, c, h0, h1 = funcaomuller(f, p0, p1, p2)
                d0 = (f(p1) - f(p0)) / (p1 - p0)
                d1 = (f(p2) - f(p1)) / (p2 - p1)
                a = (d1 - d0) / (p2 - p0)
                b = a * (p2 - p1) + d1
                c = f(p2)
                delta = bhaskara(a, b, c)
                if delta < 0:
                    print("Não é possível calcular raízes complexas")
                    break
                if abs(b-delta) < abs(b+delta):
                    x3 = p2-2*c/(b+delta)
                else:
                    x3 = p2-2*c/(b-delta)
                print(f"Iteração {repeticao}: x0 = {p0:.10f}, x1 = {p1:.10f}, x2 = {p2:.10f}, x3 = {x3:.10f}, f(x3) = {f(x3):.10f}")
                
                if abs(f(x3)) < e:
                    print(f"A raiz aproximada é: {x3:.10f} com {repeticao+1} iterações")
                    return x3
                elif repeticao == imax-1: 
                    print("A função não convergiu")
                repeticao += 1 
            return x3
        except:
            print("A função não convergiu")

    #Chamar a função isalamento de raiz e seus parametros
    iso.isolamento_de_raiz(f,i,j,h)
    print('') 

    #Caso queira mostrar os intervalos onde possa ter raizes basta implementar o metodo de isolamento de raizes
    p0 = float(input("Digite o ponto inical p0, com base no intervalo de raiz existente: "))
    p1 = float(input("Digite o ponto inical p1, com base no intervalo de raiz existente: "))
    p2 = float(input("Digite o ponto inical p2, com base no intervalo de raiz existente: "))
    e = float(input("Digite a precisão desejada: "))
    imax = int(input("Digite a iteração máxima (∈ = Z): "))
    print('') 

    #Chama a função do método de muller para encontrar a raiz
    x3 = metodomuller(f, p0, p1, p2, e, imax)

    x = np.linspace(i, j, 1000)
    y = f(x)
    fig, ax = plt.subplots()
    ax.plot(x, y, label='f(x)')
    ax.axhline(y=0, color='black', linestyle='-')
    #Cria um gráfico com x no eixo horizontal e f(x) no eixo vertical, onde f(x) é uma função dada.
    ax.axvline(x=x3, color='purple', linestyle='-', label='Raiz')
    #Cria um segundo gráfico com x no eixo horizontal e dy(x) no eixo vertical, onde dy(x) é outra função relacionada à f(x)
    plt.title('Gráfico de f(x)')
    plt.xlabel('Eixo X')
    plt.ylabel('Eixo Y')
    ax.set_ylim(-35, 35)
    ax.legend()
    plt.grid()
    plt.show()
