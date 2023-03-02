# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 10:17:46 2023

@author: Rodrigo
"""
import numpy as np
import random
import sys

# Open a file for writing
with open("proyecto_final.txt", "w") as file:
    # Set sys.stdout to redirect print output to the file
    sys.stdout = file


    
    def generate_stochastic_matrix(num_groups):
        matrix = np.random.rand(num_groups, num_groups)
        row_sums = matrix.sum(axis=1)
        matrix = np.around(matrix / row_sums[:, np.newaxis], decimals=3)
        return matrix 
    def generate_stochastic_matrix2(num_groups):
        matrix = []
        for i in range(num_groups):
            row = []
            row_sum = 0
            for j in range(num_groups):
                if i == j:
                    row.append(0)
                else:
                    prob = round(random.random(), 3)
                    row.append(prob)
                    row_sum += prob
            for j in range(num_groups):
                row[j] /= row_sum
                row[j] = round(row[j], 3)
            matrix.append(row)
        return matrix
    
    def fun_general04(N):
        R = np.random.rand(N)
        x = np.zeros(N)
        for i in range(0, N):
            if 0 < R[i] < 0.005:
                x[i] = np.sqrt(2*R[i])- 1/10
                #print(f'Encontrado: {R[i]}, x = {x[i]}')
            else:
                x[i] = -10*np.log(201/200 - R[i])
    
        return x
    def determine_affected_group(num_groups, matrix):
        row = matrix[num_groups-1]
        group = np.argmax(row)
        return group
    
    
    
    def remove_row_column(matrix, row_number):
        new_matrix = np.delete(matrix, row_number, axis=0)
        new_matrix = np.delete(new_matrix, row_number, axis=1)
        return new_matrix

    print('Hace mucho tiempo en un reino lejano, los cuatro ejércitos más poderosos de la tierra se encontraban en un estado constante de tensión y rivalidad. El Ejército del Norte (1), conocido por su poderoso arsenal de armas de fuego y su habilidad de combate en la nieve. El Ejército del Sur (2), reconocido por sus tácticas astutas y su inteligencia superior. El Ejército del Este (3), con fama de ser el más disciplinado y letal en el combate cuerpo a cuerpo. Y por último, el Ejército del Oeste (4), dueño de la tecnología más avanzada y una impresionante flota de aeronaves.')
    num_groups = int(input('Cuantos de los 4 ejercitos quieres que peleen?'))
    print('Cuantos de los 4 ejercitos quieres que peleen?')
    print(num_groups)
    if (num_groups == 2):
        print('Cuantos soldados hay en cada ejército?\n')
        vidas = int(input('Cuantos soldados hay en cada ejército?\n'))
        print(vidas)
        matrix = generate_stochastic_matrix2(num_groups)
        
        N = 200000;
        n_lives1 = vidas
        n_lives2= vidas

        print('La matríz inicial es')
        for m in matrix:
            print(m)
        while (n_lives1>0 and n_lives2>0):
                            ataca = fun_general04(N)
                            atacante = int(np.trunc(sum(ataca)/N)/random.randint(2, 6))

                            group = determine_affected_group(atacante-2, matrix)

                            if (group == 0):
                                n_lives1 = n_lives1-1
                                print('El Ejército del Norte tiene',n_lives1,'soldados')
                                if (n_lives1 == 0):
                                    print('El Ejército del Norte ha muerto')
                                    print('\nEl ejercito vencedor es el 2')
                            if (group == 1):
                                n_lives2 = n_lives2-1
                                print('El Ejército del Sur tiene',n_lives2,'soldados')
                                if (n_lives2 == 0):
                                    print('El Ejército del Sur ha muerto')
                                    print('\nEl ejercito vencedor es el 1')
            
        print("Game over")
    elif (num_groups == 3):
        print('Cuantos soldados hay en cada ejército?\n')
        vidas = int(input('Cuantos soldados hay en cada ejército?\n'))
        print(vidas)
        matrix = generate_stochastic_matrix2(num_groups)
        
        N = 200000;
        n_lives1 = vidas
        n_lives2= vidas
        n_lives3 = vidas
        print('La matríz inicial es')
        for m in matrix:
            print(m)
        while (n_lives1>0 and n_lives2>0 and n_lives3>0):
                ataca = fun_general04(N)
                atacante = int(np.trunc(sum(ataca)/N)/random.randint(2, 6))

                group = determine_affected_group(atacante-1, matrix)

                if (group == 0):
                    n_lives1 = n_lives1-1
                    print('El Ejército del Norte tiene',n_lives1,'soldados')
                    if (n_lives1 == 0):
                        print('El Ejército del Norte ha muerto')
                        row_number = 0
                        new_matrix = remove_row_column(matrix, row_number)
                        print(new_matrix)
                        while (n_lives2>0 and n_lives3>0):
                            ataca = fun_general04(N)
                            atacante = int(np.trunc(sum(ataca)/N)/random.randint(2, 6))

                            group = determine_affected_group(atacante-2, new_matrix)

                            if (group == 0):
                                n_lives2 = n_lives2-1
                                print('El Ejército del Sur tiene',n_lives2,'soldados')
                                if (n_lives2 == 0):
                                    print('El Ejército del Sur ha muerto')
                                    row_number = 0
                                    print('\nEl ejercito vencedor es el 3')
                            if (group == 1):
                                n_lives3 = n_lives3-1
                                print('El Ejército del Este tiene',n_lives3,'soldados')
                                if (n_lives3 == 0):
                                    print('El Ejército del Este ha muerto')
                                    row_number = 1
                                    print('\nEl ejercito vencedor es el 2')

                if (group == 1):
                    n_lives2 = n_lives2-1
                    print('El Ejército del Sur tiene',n_lives2,'soldados')
                    if (n_lives2 == 0):
                        print('El Ejército del Sur ha muerto')
                        row_number = 1
                        new_matrix = remove_row_column(new_matrix, row_number)
                        print(new_matrix)
                        while (n_lives1>0 and n_lives3>0):
                            ataca = fun_general04(N)
                            atacante = int(np.trunc(sum(ataca)/N)/random.randint(2, 6))

                            group = determine_affected_group(atacante-2, new_matrix)

                            if (group == 0):
                                n_lives1 = n_lives1-1
                                print('El Ejército del Norte tiene',n_lives1,'soldados')
                                if (n_lives1 == 0):
                                    print('El Ejército del Norte ha muerto')
                                    row_number = 0
                                    print('\nEl ejercito vencedor es el 3')
                            if (group == 1):
                                n_lives3 = n_lives3-1
                                print('El Ejército del Este tiene',n_lives3,'soldados')
                                if (n_lives3 == 0):
                                    print('El Ejército del Este ha muerto')
                                    row_number = 1
                                    print('\nEl ejercito vencedor es el 1')

                if (group == 2):
                    n_lives3 = n_lives3-1
                    print('El Ejército del Este tiene',n_lives3,'soldados')
                    if (n_lives3 == 0):
                        print('El Ejército del Este ha muerto')
                        row_number = 2
                        new_matrix = remove_row_column(new_matrix, row_number)
                        print(new_matrix)
                        while (n_lives1>0 and n_lives2>0):
                            ataca = fun_general04(N)
                            atacante = int(np.trunc(sum(ataca)/N)/random.randint(2, 6))

                            group = determine_affected_group(atacante-2, new_matrix)

                            if (group == 0):
                                n_lives1 = n_lives1-1
                                print('El Ejército del Norte tiene',n_lives1,'soldados')
                                if (n_lives1 == 0):
                                    print('El Ejército del Norte ha muerto')
                                    row_number = 0
                                    print('\nEl ejercito vencedor es el 2')
                            if (group == 1):
                                n_lives2 = n_lives2-1
                                print('El Ejército del Sur tiene',n_lives2,'soldados')
                                if (n_lives2 == 0):
                                    print('El Ejército del Sur ha muerto')
                                    row_number = 1
                                    print('\nEl ejercito vencedor es el 1')
            
        print("Game over")
    else:
        print('Cuantos soldados hay en cada ejército?\n')
        vidas = int(input('Cuantos soldados hay en cada ejército?\n'))
        print(vidas)
        matrix = generate_stochastic_matrix2(num_groups)
        
        N = 200000;
        n_lives1 = vidas
        n_lives2= vidas
        n_lives3 = vidas
        n_lives4 = vidas
        print('La matríz inicial es')
        for m in matrix:
            print(m)
        
        while (n_lives1>0 and n_lives2>0 and n_lives3>0 and n_lives4>0):
            ataca = fun_general04(N)
            atacante = int(np.trunc(sum(ataca)/N)/random.randint(2, 6))
            print('\nEl ejercito que ataca es: ',atacante)
        
            group = determine_affected_group(atacante, matrix)
            print("El ejercito atacado: ", group+1)
        
            if (group == 0):
                n_lives1 = n_lives1-1
                print('El Ejército del Norte tiene',n_lives1,'soldados')
                if (n_lives1 == 0):
                    print('El Ejército del Norte ha muerto')
                    row_number = 0
                    new_matrix = remove_row_column(matrix, row_number)
                    print(new_matrix)
        
                    while (n_lives2>0 and n_lives3>0 and n_lives4>0):
                        ataca = fun_general04(N)
                        atacante = int(np.trunc(sum(ataca)/N)/random.randint(2, 6))
                        
        
                        group = determine_affected_group(atacante-1, new_matrix)
        
                        if (group == 0):
                            n_lives2 = n_lives2-1
                            print('El Ejército del Sur tiene',n_lives2,'soldados')
                            if (n_lives2 == 0):
                                print('El Ejército del Sur ha muerto')
                                row_number = 0
                                new_matrix = remove_row_column(new_matrix, row_number)
                                print(new_matrix)
                                while (n_lives3>0 and n_lives4>0):
                                    ataca = fun_general04(N)
                                    atacante = int(np.trunc(sum(ataca)/N)/random.randint(2, 6))
                                    
        
                                    group = determine_affected_group(atacante-2, new_matrix)
        
                                    if (group == 0):
                                        n_lives3 = n_lives3-1
                                        print('El Ejército del Este tiene',n_lives3,'soldados')
                                        if (n_lives3 == 0):
                                            print('El Ejército del Este ha muerto')
                                            row_number = 0
                                            print('El ejercito vencedor es el 4')
                                    if (group == 1):
                                        n_lives4 = n_lives4-1
                                        print('El Ejército del Oeste tiene',n_lives4,'soldados')
                                        if (n_lives4 == 0):
                                            print('El Ejército del Oeste ha muerto')
                                            row_number = 1
                                            print('El ejercito vencedor es el 3')
        
                        if (group == 1):
                            n_lives3 = n_lives3-1
                            print('El Ejército del Este tiene',n_lives3,'soldados')
                            if (n_lives3 == 0):
                                print('El Ejército del Este ha muerto')
                                row_number = 1
                                new_matrix = remove_row_column(new_matrix, row_number)
                                print(new_matrix)
                                while (n_lives2>0 and n_lives4>0):
                                    ataca = fun_general04(N)
                                    atacante = int(np.trunc(sum(ataca)/N)/random.randint(2, 6))
                                    
        
                                    group = determine_affected_group(atacante-2, new_matrix)
        
                                    if (group == 0):
                                        n_lives2 = n_lives2-1
                                        print('El Ejército del Sur tiene',n_lives2,'soldados')
                                        if (n_lives2 == 0):
                                            print('El Ejército del Sur ha muerto')
                                            row_number = 0
                                            print('El ejercito vencedor es el 4')
                                    if (group == 1):
                                        n_lives4 = n_lives4-1
                                        print('El Ejército del Oeste tiene',n_lives4,'soldados')
                                        if (n_lives4 == 0):
                                            print('El Ejército del Oeste ha muerto')
                                            row_number = 1
                                            print('El ejercito vencedor es el 2')
        
                        if (group == 2):
                            n_lives4 = n_lives4-1
                            print('El Ejército del Oeste tiene',n_lives4,'soldados')
                            if (n_lives4 == 0):
                                print('El Ejército del Oeste ha muerto')
                                row_number = 2
                                new_matrix = remove_row_column(new_matrix, row_number)
                                print(new_matrix)
                                while (n_lives3>0 and n_lives2>0):
                                    ataca = fun_general04(N)
                                    atacante = int(np.trunc(sum(ataca)/N)/random.randint(2, 6))
                                    
        
                                    group = determine_affected_group(atacante-2, new_matrix)
        
                                    if (group == 0):
                                        n_lives2 = n_lives2-1
                                        print('El Ejército del Sur tiene',n_lives2,'soldados')
                                        if (n_lives2 == 0):
                                            print('El Ejército del Sur ha muerto')
                                            row_number = 0
                                            print('El ejercito vencedor es el 3')
                                    if (group == 1):
                                        n_lives3 = n_lives3-1
                                        print('El Ejército del Este tiene',n_lives3,'soldados')
                                        if (n_lives3 == 0):
                                            print('El Ejército del Este ha muerto')
                                            row_number = 1
                                            print('El ejercito vencedor es el 2')
        
            if (group == 1):
                n_lives2 = n_lives2-1
                print('El Ejército del Sur tiene',n_lives2,'soldados')
                if (n_lives2 == 0):
                    print('El Ejército del Sur ha muerto')
                    row_number = 1
                    new_matrix = remove_row_column(matrix, row_number)
                    print(new_matrix)
        
                    while (n_lives1>0 and n_lives3>0 and n_lives4>0):
                        ataca = fun_general04(N)
                        atacante = int(np.trunc(sum(ataca)/N)/random.randint(2, 6))
                        
        
                        group = determine_affected_group(atacante-1, new_matrix)
        
                        if (group == 0):
                            n_lives1 = n_lives1-1
                            print('El Ejército del Norte tiene',n_lives1,'soldados')
                            if (n_lives1 == 0):
                                print('El Ejército del Norte ha muerto')
                                row_number = 0
                                while (n_lives3>0 and n_lives4>0):
                                    ataca = fun_general04(N)
                                    atacante = int(np.trunc(sum(ataca)/N)/random.randint(2, 6))
                                    
        
                                    group = determine_affected_group(atacante-2, new_matrix)
        
                                    if (group == 0):
                                        n_lives3 = n_lives3-1
                                        print('El Ejército del Este tiene',n_lives3,'soldados')
                                        if (n_lives3 == 0):
                                            print('El Ejército del Este ha muerto')
                                            row_number = 0
                                            print('El ejercito vencedor es el 4')
                                    if (group == 1):
                                        n_lives4 = n_lives4-1
                                        print('El Ejército del Oeste tiene',n_lives4,'soldados')
                                        if (n_lives4 == 0):
                                            print('El Ejército del Oeste ha muerto')
                                            row_number = 1
                                            print('El ejercito vencedor es el 3')
        
                        if (group == 1):
                            n_lives3 = n_lives3-1
                            print('El Ejército del Este tiene',n_lives3,'soldados')
                            if (n_lives3 == 0):
                                print('El Ejército del Este ha muerto')
                                row_number = 1
                                new_matrix = remove_row_column(new_matrix, row_number)
                                print(new_matrix)
                                while (n_lives1>0 and n_lives4>0):
                                    ataca = fun_general04(N)
                                    atacante = int(np.trunc(sum(ataca)/N)/random.randint(2, 6))
                                    
        
                                    group = determine_affected_group(atacante-2, new_matrix)
        
                                    if (group == 0):
                                        n_lives1 = n_lives1-1
                                        print('El Ejército del Norte tiene',n_lives1,'soldados')
                                        if (n_lives1 == 0):
                                            print('El Ejército del Norte ha muerto')
                                            row_number = 0
                                            print('El ejercito vencedor es el 4')
                                    if (group == 1):
                                        n_lives4 = n_lives4-1
                                        print('El Ejército del Oeste tiene',n_lives4,'soldados')
                                        if (n_lives4 == 0):
                                            print('El Ejército del Oeste ha muerto')
                                            row_number = 1
                                            print('El ejercito vencedor es el 1')
        
                        if (group == 2):
                            n_lives4 = n_lives4-1
                            print('El Ejército del Oeste tiene',n_lives4,'soldados')
                            if (n_lives4 == 0):
                                print('El Ejército del Oeste ha muerto')
                                row_number = 2
                                new_matrix = remove_row_column(new_matrix, row_number)
                                print(new_matrix)
                                while (n_lives1>0 and n_lives3>0):
                                    ataca = fun_general04(N)
                                    atacante = int(np.trunc(sum(ataca)/N)/random.randint(2, 6))
                                    
        
                                    group = determine_affected_group(atacante-2, new_matrix)
        
                                    if (group == 0):
                                        n_lives1 = n_lives1-1
                                        print('El Ejército del Norte tiene',n_lives1,'soldados')
                                        if (n_lives1 == 0):
                                            print('El Ejército del Norte ha muerto')
                                            row_number = 0
                                            print('El ejercito vencedor es el 3')
                                    if (group == 1):
                                        n_lives3 = n_lives3-1
                                        print('El Ejército del Este tiene',n_lives4,'soldados')
                                        if (n_lives4 == 0):
                                            print('El Ejército del Este ha muerto')
                                            row_number = 1
                                            print('El ejercito vencedor es el 1')
        
        
            if (group == 2):
                n_lives3 = n_lives3-1
                print('El Ejército del Este tiene',n_lives3,'soldados')
                if (n_lives3 == 0):
                    print('El Ejército del Este ha muerto')
                    row_number = 2
                    new_matrix = remove_row_column(matrix, row_number)
                    print(new_matrix)
        
                    while (n_lives1>0 and n_lives2>0 and n_lives4>0):
                        ataca = fun_general04(N)
                        atacante = int(np.trunc(sum(ataca)/N)/random.randint(2, 6))
                        
        
                        group = determine_affected_group(atacante-1, new_matrix)
        
                        if (group == 0):
                            n_lives1 = n_lives1-1
                            print('El Ejército del Norte tiene',n_lives1,'soldados')
                            if (n_lives1 == 0):
                                print('El Ejército del Norte ha muerto')
                                row_number = 0
                                new_matrix = remove_row_column(new_matrix, row_number)
                                print(new_matrix)
                                while (n_lives2>0 and n_lives4>0):
                                    ataca = fun_general04(N)
                                    atacante = int(np.trunc(sum(ataca)/N)/random.randint(2, 6))
                                    
        
                                    group = determine_affected_group(atacante-2, new_matrix)
        
                                    if (group == 0):
                                        n_lives2 = n_lives2-1
                                        print('El Ejército del Sur tiene',n_lives2,'soldados')
                                        if (n_lives2 == 0):
                                            print('El Ejército del Sur ha muerto')
                                            row_number = 0
                                            print('El ejercito vencedor es el 4')
                                    if (group == 1):
                                        n_lives4 = n_lives4-1
                                        print('El Ejército del Oeste tiene',n_lives4,'soldados')
                                        if (n_lives4 == 0):
                                            print('El Ejército del Oeste ha muerto')
                                            row_number = 1
                                            print('El ejercito vencedor es el 2')
        
                        if (group == 1):
                            n_lives2 = n_lives2-1
                            print('El Ejército del Sur tiene',n_lives2,'soldados')
                            if (n_lives2 == 0):
                                print('El Ejército del Sur ha muerto')
                                row_number = 1
                                new_matrix = remove_row_column(new_matrix, row_number)
                                print(new_matrix)
                                while (n_lives1>0 and n_lives4>0):
                                    ataca = fun_general04(N)
                                    atacante = int(np.trunc(sum(ataca)/N)/random.randint(2, 6))
                                    
        
                                    group = determine_affected_group(atacante-2, new_matrix)
        
                                    if (group == 0):
                                        n_lives1 = n_lives1-1
                                        print('El Ejército del Norte tiene',n_lives1,'soldados')
                                        if (n_lives1 == 0):
                                            print('El Ejército del Norte ha muerto')
                                            row_number = 0
                                            print('El ejercito vencedor es el 4')
                                    if (group == 1):
                                        n_lives4 = n_lives4-1
                                        print('El Ejército del Oeste tiene',n_lives4,'soldados')
                                        if (n_lives4 == 0):
                                            print('El Ejército del Oeste ha muerto')
                                            row_number = 1
                                            print('El ejercito vencedor es el 1')
        
                        if (group == 2):
                            n_lives4 = n_lives4-1
                            print('El Ejército del Oeste tiene',n_lives4,'soldados')
                            if (n_lives4 == 0):
                                print('El Ejército del Oeste ha muerto')
                                row_number = 2
                                new_matrix = remove_row_column(new_matrix, row_number)
                                print(new_matrix)
                                while (n_lives1>0 and n_lives2>0):
                                    ataca = fun_general04(N)
                                    atacante = int(np.trunc(sum(ataca)/N)/random.randint(2, 6))
                                    
        
                                    group = determine_affected_group(atacante-2, new_matrix)
        
                                    if (group == 0):
                                        n_lives1 = n_lives1-1
                                        print('El Ejército del Norte tiene',n_lives1,'soldados')
                                        if (n_lives1 == 0):
                                            print('El Ejército del Norte ha muerto')
                                            row_number = 0
                                            print('El ejercito vencedor es el 2')
                                    if (group == 1):
                                        n_lives2 = n_lives2-1
                                        print('El Ejército del Sur tiene',n_lives2,'soldados')
                                        if (n_lives2 == 0):
                                            print('El Ejército del Sur ha muerto')
                                            row_number = 1
                                            print('El ejercito vencedor es el 1')
        
            if (group == 3):
                n_lives4 = n_lives4-1
                print('El Ejército del Oeste tiene',n_lives4,'soldados')
                if (n_lives4 == 0):
                    print('El Ejército del Oeste ha muerto')
                    row_number = 3
                    new_matrix = remove_row_column(matrix, row_number)
                    print(new_matrix)
        
                    while (n_lives1>0 and n_lives2>0 and n_lives3>0):
                        ataca = fun_general04(N)
                        atacante = int(np.trunc(sum(ataca)/N)/random.randint(2, 6))
        
                        group = determine_affected_group(atacante-1, new_matrix)
        
                        if (group == 0):
                            n_lives1 = n_lives1-1
                            print('El Ejército del Norte tiene',n_lives1,'soldados')
                            if (n_lives1 == 0):
                                print('El Ejército del Norte ha muerto')
                                row_number = 0
                                new_matrix = remove_row_column(new_matrix, row_number)
                                print(new_matrix)
                                while (n_lives2>0 and n_lives3>0):
                                    ataca = fun_general04(N)
                                    atacante = int(np.trunc(sum(ataca)/N)/random.randint(2, 6))
        
                                    group = determine_affected_group(atacante-2, new_matrix)
        
                                    if (group == 0):
                                        n_lives2 = n_lives2-1
                                        print('El Ejército del Sur tiene',n_lives2,'soldados')
                                        if (n_lives2 == 0):
                                            print('El Ejército del Sur ha muerto')
                                            row_number = 0
                                            print('\nEl ejercito vencedor es el 3')
                                    if (group == 1):
                                        n_lives3 = n_lives3-1
                                        print('El Ejército del Este tiene',n_lives3,'soldados')
                                        if (n_lives3 == 0):
                                            print('El Ejército del Este ha muerto')
                                            row_number = 1
                                            print('\nEl ejercito vencedor es el 2')
        
                        if (group == 1):
                            n_lives2 = n_lives2-1
                            print('El Ejército del Sur tiene',n_lives2,'soldados')
                            if (n_lives2 == 0):
                                print('El Ejército del Sur ha muerto')
                                row_number = 1
                                new_matrix = remove_row_column(new_matrix, row_number)
                                print(new_matrix)
                                while (n_lives1>0 and n_lives3>0):
                                    ataca = fun_general04(N)
                                    atacante = int(np.trunc(sum(ataca)/N)/random.randint(2, 6))
        
                                    group = determine_affected_group(atacante-2, new_matrix)
        
                                    if (group == 0):
                                        n_lives1 = n_lives1-1
                                        print('El Ejército del Norte tiene',n_lives1,'soldados')
                                        if (n_lives1 == 0):
                                            print('El Ejército del Norte ha muerto')
                                            row_number = 0
                                            print('\nEl ejercito vencedor es el 3')
                                    if (group == 1):
                                        n_lives3 = n_lives3-1
                                        print('El Ejército del Este tiene',n_lives3,'soldados')
                                        if (n_lives3 == 0):
                                            print('El Ejército del Este ha muerto')
                                            row_number = 1
                                            print('\nEl ejercito vencedor es el 1')
        
                        if (group == 2):
                            n_lives3 = n_lives3-1
                            print('El Ejército del Este tiene',n_lives3,'soldados')
                            if (n_lives3 == 0):
                                print('El Ejército del Este ha muerto')
                                row_number = 2
                                new_matrix = remove_row_column(new_matrix, row_number)
                                print(new_matrix)
                                while (n_lives1>0 and n_lives2>0):
                                    ataca = fun_general04(N)
                                    atacante = int(np.trunc(sum(ataca)/N)/random.randint(2, 6))
        
                                    group = determine_affected_group(atacante-2, new_matrix)
        
                                    if (group == 0):
                                        n_lives1 = n_lives1-1
                                        print('El Ejército del Norte tiene',n_lives1,'soldados')
                                        if (n_lives1 == 0):
                                            print('El Ejército del Norte ha muerto')
                                            row_number = 0
                                            print('\nEl ejercito vencedor es el 2')
                                    if (group == 1):
                                        n_lives2 = n_lives2-1
                                        print('El Ejército del Sur tiene',n_lives2,'soldados')
                                        if (n_lives2 == 0):
                                            print('El Ejército del Sur ha muerto')
                                            row_number = 1
                                            print('\nEl ejercito vencedor es el 1')
                    
        print("Game over")

            
    sys.stdout = sys.__stdout__