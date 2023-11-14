#DISCENTES - Ingryd Medeiros

#Importa a biblioteca de gráficos do python
import matplotlib.pyplot as plt
#Importa a biblioteca de calculo do python
import numpy as np

#Do arquivo blue 0 será importado a Retrosubstituição 
from blue_0_retrosub import Retrosubstituição

#Do arquivo blue 1 será importado a função Eliminação de Gauss
from blue_1_guass import Eliminação_Guass 

#Do arquivo blue 2 será importado a função Fatoração LU sem pivô
from blue_2_lu import LU 

#Do arquivo blue 3 será importado a função Fatoração LU com pivô
from blue_3_lupivo import LUpivo

#Do arquivo blue 4 será importado a função Gauss-Jacobi
from blue_4_jacobi import Jacobi 

#Do arquivo blue 5 será importado a função Gauss-Seidel
from blue_5_seidel import Seidel

#Do arquivo blue 6 será importado a função Interpolação Polinomial
from blue_6_interpolação import Interpolação_polinomail

#Do arquivo blue 7 será importado a função Interpolação Lagrange
from blue_7_lagrange import Lagrange

#Do arquivo blue 8 será importado a função Diferenças dividias (Newton)
from blue_8_newton import Newton


# Matrizes para testes

# Matrizes e vetor 8x8
A_8x8 = np.array([[15,  2,   3,  1,  0.7, 0.5, 3,   1],
    [1, 11,  -3,  4,  0.8, 0.6, 0.9, 2],
    [-6,  4, -17,  2,  1,   3,   2,   4],
    [3, -8,   3, 30,  8,   5,   7,   6],
    [1,  4,   2,  3, 55,  17,  12,   5],
    [1.5, 2, 0.7, 0.8, 3,  17,  1,  0.9],
    [0.5, 1, 1.8,  6,  2,   5,  27,   1],
    [8,  3,   2,  2, 0.3,  1,   5,  35]]) 
    
b_8x8 = np.array([3, 2, 5, -7, 10, 2, -7, 9])

# Matrizes e vetor 20x20
A_20x20 = np.array([[25.9912,  3.5970,  9.8469,  4.2332, 34.7726, 27.3573, 42.4294, 23.7293, 32.5902,  5.2457, 15.5347, 30.4976, 23.8243,  2.6875,  3.1043,  8.2600, 22.7991, 28.6107,  1.9863, 22.3779],
    [27.5150, 11.6134, 21.8972,  3.9585, 47.0922, 14.4264, 13.8740, 20.5405,  5.8629,  9.4681, 39.0348, 16.5360, 11.3016, 40.0497,  3.8644, 24.1319, 23.7222, 43.7957,  0.9373, 13.2087],
    [24.0127, 12.7567, 38.8971, 27.4739, 24.1394, 24.6710, 21.4854, 31.2840, 44.3081, 48.4670, 23.1294, 45.4513, 15.0620, 43.9511, 35.4743, 44.6662, 45.4353, 20.8848,  6.9530, 39.5928],
    [17.2247, 24.1012, 39.3125, 40.5014, 23.8175, 28.1473, 19.4170, 34.4578, 13.5618, 26.2925, 20.0502, 25.9280, 30.4854,  2.6948, 44.9628, 11.1522, 32.9802,  2.6331, 31.4438,  7.3993],
    [38.3010,  2.5536,  5.3225, 11.5662,  3.8627, 45.2881, 38.9639, 41.9614,  7.9155,  1.6839, 24.1143, 49.5188,  2.2456, 41.3303, 41.1228,  0.8342,  2.3390, 40.4997,  3.2865, 28.6288],
    [29.4035, 18.7453, 14.1898, 14.5555, 14.8429,  6.2584, 40.2102, 15.0716,  8.5625, 16.0001, 32.6796, 25.9817,  3.1318,  4.4688, 28.8178, 28.2966, 21.9404, 46.9778,  6.0105, 44.2187],
    [47.4318, 27.8799,  4.1246, 35.6247, 29.6943, 17.3475, 49.8659, 17.7255, 48.7461, 35.9461,  0.4752,  3.0264, 33.6818, 27.0865, 29.9132, 49.8034, 12.0512, 17.8282, 44.7058,  0.8590],
    [26.0571, 42.3460, 26.8624, 31.3020, 23.3236, 38.2144,  3.7498, 17.4426, 43.6287, 47.8138, 13.9971, 20.8457, 29.8216, 37.2478, 27.5096, 31.5582, 27.0015, 19.1845, 26.2130, 24.6012],
    [35.5450, 33.7343, 30.1752,  7.1046,  5.7773, 16.5032, 49.2501, 34.6238, 47.7127, 34.9745, 16.0034, 31.7337, 45.7497, 37.9706, 46.8178, 47.4970, 19.1735, 14.9837, 27.3104,  7.9055],
    [36.4029, 40.7650, 27.4499, 43.7357, 20.4064, 24.8010, 24.0493,  4.8495,  6.6130, 39.5465,  7.0996, 16.5272,  2.2924, 19.8485,  4.6905,  8.5942, 44.1106, 32.1502,  3.4548, 28.9755],
    [20.5734, 28.5464,  7.9724,  9.7784,  2.3351, 32.5191, 25.6488,  8.9284, 11.9055, 45.8057,  5.6992, 17.4950, 12.6232, 20.0658, 30.9219, 37.0543, 42.1311, 17.5571, 47.2811,  4.5041],
    [16.9235,  2.4880, 16.7162,  3.2648, 20.8257, 19.8963, 37.5233,  0.8241, 20.3117,  8.3805, 16.4194, 23.7695, 13.9425, 42.4739, 37.1793, 17.9694, 18.9548, 40.3722,  5.2048, 26.7414],
    [24.9236, 35.0730, 19.7356, 41.2959, 18.8251, 13.0565, 38.1969,  9.8102,  6.6108, 35.7143, 32.8824, 43.8445, 44.2042, 43.6896, 49.2848, 23.3128, 27.3690, 27.7620, 38.2494, 25.0142],
    [8.1347, 49.8483, 37.7969, 14.2606, 32.7716, 39.9544, 14.6147,  3.6723, 31.1751, 27.1158, 25.5338, 10.0340, 46.4516, 39.6304,  1.1259, 46.6044, 44.7934, 31.5724, 32.7060,  7.3429],
    [27.5424,  3.3831,  9.4710, 36.8023, 43.4264, 41.4315, 18.1645, 20.4520,  4.3419, 46.0158, 14.6602,  5.6187, 33.4496,  8.1363, 40.1052, 12.5039, 17.3538,  4.2424, 11.4864,  3.9262],
    [28.0826, 19.5612,  6.9330, 41.8091, 20.4940, 14.9644, 33.6951, 32.0018, 41.4910, 48.9065,  5.8430,  8.6043, 38.8255,  5.4775, 29.7620, 12.8112,  9.7328, 40.4439,  2.2981, 48.1627],
    [32.6374,  6.9866, 22.8888, 11.7580,  5.1230, 22.8841, 43.3391, 21.9157, 30.3355, 20.7260,  0.7067, 37.3610, 25.7343, 32.7891, 42.9858,  7.2287, 23.7361, 49.7010, 31.2349, 44.4439],
    [17.9171, 36.9246, 13.3357,  9.2840, 11.7589,  7.9458, 41.5403, 13.6596, 22.3272, 27.6684,  1.1278, 33.5705, 26.3999, 40.1055, 21.5612, 13.2327, 22.7153, 40.5347, 22.6012,  2.7225],
    [6.1820, 29.2679, 32.4382,  4.7003, 14.1065,  0.4651, 37.9867, 40.4509,  9.3526, 32.5984, 47.7834,  0.1777, 46.9684, 47.6789,  0.9149, 40.5299, 39.0676,  9.2677, 42.9246, 28.1954],
    [49.0218, 44.2264, 49.3287, 28.8533, 49.3146,  2.9371, 46.4750, 42.7840, 35.5059, 10.5379, 39.8764, 21.7893, 33.5127, 44.3185, 27.8742, 29.3751,  0.9935, 33.8722, 38.0926, 19.1896]])

b_20x20 = np.array([40.4554, 10.1067, 48.7878, 30.4491, 49.0677, 43.4887, 43.3943, 30.3153, 33.6710, 26.7800, 40.7279, 17.5335, 33.5339, 17.1401, 0.9459, 32.7490, 5.8962, 34.1086, 36.2167, 28.7823])

# Listas que contem as matrizes e vetores testes
lista_matriz = [A_8x8 , A_20x20]
lista_vetor = [b_8x8, b_20x20]

# Listas testes
listax=[0.0, 0.2, 0.4, 0.6, 0.8, 1]
listay=[1.0, 1.24, 1.57, 2.03, 2.69, 3.71]

# Loop do menu de seleção
while True:
    
    print("")
    print("As equações testes são:")
    print("1. Matriz A e Vetor b (8x8)")
    print("2. Matriz A e Vetor b (20x20)")
    print("3. Listas de interpolação")
    print("4. Sair")
    print("")

    equação = int(input("Escolha a equação desejada: "))
    
    # Verifica a escolha do usuário para a equação desejada e seleciona as matrizes, vetores ou listas
    
    if equação == 1:
        matriz = lista_matriz[0] # seleciona a matriz A e vetor b 8x8
        vetor = lista_vetor[0]
        print("\n""Matriz A", matriz, "\n")
        print("\n""Vetor b:", vetor, "\n")
    elif equação == 2:
        matriz = lista_matriz[1] # seleciona a matriz A e vetor b 20x20
        vetor = lista_vetor[1]
        print("\n""Matriz A", matriz, "\n")
        print("\n""Vetor b:", vetor, "\n")
    elif equação == 3:
        print("\n""Lista x:", listax, "\n")
        print("\n""Lista y:", listay, "\n")
    elif equação == 4:
        print("Você escolheu sair do menu")
        break
    else:
        print("Opção inválida. Digite um número de 1 a 4 para selecionar uma opção válida ou 5 para sair.")
        continue

    # Exibe as opções do menu refrente aos metodos diponiveis para uso
    print("")
    print("Os métodos são:")
    print("0. Retrosubstituição")
    print("1. Eliminação de Gauss")
    print("2. Fatoração LU sem pivô")
    print("3. Fatoração LU com pivô")
    print("4. Gauss-Jacobi")
    print("5. Gauss-Seidel")
    print("6. Interpolação Polinomial")
    print("7. Interpolação Lagrange")
    print("8. Interpolação de Diferenças dividias (Newton)")
    print("9. Sair")
    print("")
    
    # Recebe a escolha do usuário
    método = int(input("Digite o número do método desejado: "))
    
    # Verifica a escolha do usuário e chama o método coorespondente 
    
    if método == 0:
        print("\n""Deseja vizualizar os calculos? ","\n")
        print("{s} = Sim, {n} = Não","\n")
        variavel = input()
        if variavel == "s":
            Retrosubstituição(matriz, vetor, V = True)
        elif variavel == "n":
            Retrosubstituição(matriz, vetor, V = False)
        else:
            print("Opção invalida")
            
    elif método == 1:
        print("\n""Deseja vizualizar os calculos? ","\n")
        print("{s} = Sim, {n} = Não","\n")
        variavel = input()
        if variavel == "s":
            Eliminação_Guass(matriz, vetor, V = True)
        elif variavel == "n":
            Eliminação_Guass(matriz, vetor, V = False)
        else:
            print("Opção invalida")  
            
    elif método == 2:
        print("\n""Deseja vizualizar os calculos? ","\n")
        print("{s} = Sim, {n} = Não","\n")
        variavel = input()
        if variavel == "s":
            LU(matriz, vetor, V = True)
        elif variavel == "n":
            LU(matriz, vetor, V = False)
        else:
            print("Opção invalida")  
            
    elif método == 3:
        print("\n""Deseja vizualizar os calculos? ","\n")
        print("{s} = Sim, {n} = Não","\n")
        variavel = input()
        if variavel == "s":
            LUpivo(matriz, vetor, V = True)
        elif variavel == "n":
            LUpivo(matriz, vetor, V = False)
        else:
            print("Opção invalida")  
                
    elif método == 4:
        print("\n""Deseja vizualizar os calculos? ","\n")
        print("{s} = Sim, {n} = Não","\n")
        variavel = input()
        if variavel == "s":
            Jacobi(matriz, vetor, V = True)
        elif variavel == "n":
            Jacobi(matriz, vetor, V = False)
        else:
            print("Opção invalida")  
        
    elif método == 5:
        print("\n""Deseja vizualizar os calculos? ","\n")
        print("{s} = Sim, {n} = Não","\n")
        variavel = input()
        if variavel == "s":
            Seidel(matriz, vetor, V = True)
        elif variavel == "n":
            Seidel(matriz, vetor, V = False)
        else:
            print("Opção invalida") 
        
    elif método == 6:
        print("\n""Deseja vizualizar os calculos? ","\n")
        print("{s} = Sim, {n} = Não","\n")
        variavel = input()
        if variavel == "s":
            Interpolação_polinomail(listax, listay, V = True)
        elif variavel == "n":
            Interpolação_polinomail(listax, listay, V = False)
        else:
            print("Opção invalida") 
        
    elif método == 7:
        print("\n""Deseja vizualizar os calculos? ","\n")
        print("{s} = Sim, {n} = Não","\n")
        variavel = input()
        if variavel == "s":
            Lagrange(listax, listay, V = True)
        elif variavel == "n":
            Lagrange(listax, listay, V = False)
        else:
            print("Opção invalida")
            
    elif método == 8:
        print("\n""Deseja vizualizar os calculos? ","\n")
        print("{s} = Sim, {n} = Não","\n")
        variavel = input()
        if variavel == "s":
            Newton(listax, listay, V = True)
        elif variavel == "n":
            Newton(listax, listay, V = False)
        else:
            print("Opção invalida")
            
    elif método == 9:
        print("Você escolheu sair do menu","\n")
        break
    else:
        print("Opção inválida. Digite um número de 0 a 8 para selecionar uma opção válida ou 9 para sair.") 
        