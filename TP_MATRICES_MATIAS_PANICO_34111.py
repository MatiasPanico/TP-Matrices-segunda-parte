# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 23:40:28 2023

@author: matia
"""
#jrr
class MyArray1:
    
    """ MyArray1 es un objeto capaz de operar con matrices. Puede crearlas,
    modificarlas y operar con ellas, además de resaltar un elemento, columna
    o fila específica"""
    
    def __init__(self, filas, columnas, elementos, by_row = bool):
        """
        La función "__init__" crea las instancias de la clase. En este caso,
        delimita el numero de filas, columnas, elementos y modo de lectura de la 
        matriz. A su vez, contiene un condicional que chequea si la cantidad de
        elementos coincide con las dimenciones de la matriz. En caso contrario, 
        se para la lectura del código imprimiendo un mensaje de error.

        """
        #if len(elementos) != (filas * columnas):
        #    print("La cantidad de elementos debe coincidir con la cantidad de filas por cantidad de columnas.")
        #else:
        self.elems = elementos
        self.r = filas
        self.c = columnas
        self.by_row = by_row

    def get_pos(self, j, k):
        """
        Esta función determina matemáticamente en qué posición (índice de la lista)
        está dicho elemento según sus coordenadas j y k, con el condicional de que
        si estos parámetros no se encuentran dentro de 0 y self.c y self.r, se para
        la lectura del código.

        """
        if 0 < k <= self.c and 0 < j <= self.r: 
            if self.by_row == True:
                p = k + (j-1)*self.c
            if self.by_row == False:
                p = j + (k-1)*self.r
            #Se le resta 1 a p para poder obtener el índice 0. De esta manera, una coordenada (4, 4), si bien es el elemento numero 16 de la matriz, se marca su índice como 15. 
            return p-1
        else:
            print('ERROR: El numero introducido no se encuentra dentro de la lista')
        
    def get_coords(self, p):
        """
        Por el contrario a "get_pos", "get_coords" devuelve las coordenadas de un 
        elemento segun su posición u índice a través de un cálculo matemático. Luego
        suma 1 a los parámetros j y k para que el código no devuelva coordenadas (0, 0).
        Así, una matriz 3*3 , en lugar de ir desde el (0, 0) hasta el (2, 2), va del
        (1, 1), hasta el (3, 3), como se acostumbra escribir matemáticamente.

        """
        if 0 <= p < self.r*self.c:
            if self.by_row == True:
                j = (p // self.c)
                k = (p - j*self.c)
                j += 1
                k += 1
            if self.by_row == False:
                k = (p // self.r)
                j = (p - k*self.r)
                k += 1
                j += 1
            return j, k
        else:
            print('ERROR: El numero introducido no se encuentra dentro de la lista')

    def switch(self):
        """
       La funcion switch cambia el modo de leer la matriz. Por default se lee a la 
       matriz por filas, pero cada vez que switch sea usada se cambiara a por columna 
       o fila, según corresponda. Esto sirve para futuras funciones cuando el parámetro
       "by_row sea falso."

        """
        matriz_cambiada = []
        if self.by_row == True:
            for i in range(self.c):
                matriz_cambiada.extend(self.elems[j*self.c+i] for j in range(self.r))
        elif self.by_row == False:
            for i in range(self.r):
                matriz_cambiada.extend(self.elems[j*self.r+i] for j in range(self.c))
        return (MyArray1(self.r, self.c, matriz_cambiada, not self.by_row))  
    
    def a_by_row(self):
        """by_row sirve para que, sea cual sea la matriz que se introduzca, esta pueda ser leida
        por fila. Necesita ser llamada desde otro metodo y sirve para facilitar el indexado de la matriz
        cuando convenga indexarla por filas. Devuelve la matriz leida por filas"""
        if self.by_row == True:
            matriz = self.elems
        elif self.by_row == False:
            matriz = self.switch().elems
        return matriz
        
    def a_by_col(self):
        """by_column sirve para que, sea cual sea la matriz que se introduzca, esta pueda ser leida
        por columna. Necesita ser llamada desde otro metodo y sirve para facilitar el indexado de la matriz
        cuando convenga indexarla por columnas. Devuelve la matriz leida por columnas"""
        if self.by_row == False:
            matriz = self.elems
        elif self.by_row == True:
            matriz = self.switch().elems
        return matriz
    
    def identidad(self, n):
        """eye es una funcion usada para crear matrices idendidad de NxN. El unico parametro es N e indica el 
        numero de columnas y filas de la matriz identidad (ya que debe ser cuadrada)"""
        elems, flat = [[0] * i + [1] + [0] * (n - i - 1) for i in range(n)], []
        for i in elems:
            flat.extend(i)
        return MyArray1(n, n, flat, True)
    
    def get_row(self, j):
        """
       Esta función devuelve una nueva lista en donde estaría compuesta la fila numero
       x de la matriz. Para ello, se crea una lista vacía a la que se le agregan 
       elementos de la matriz original con la función .append(). Estos elementos
       estan delimitados por 2 variables, que sería el primer elemento de la fila
       y el último elelemto de la fila, los cuales se obtienen a través de un cálculo
       matemático.

        """
        matriz = self.a_by_row()
        if 0 < j <= self.r:
            pedlf = self.c * (j-1)
            uedlf = pedlf + self.c
            row = []
            row.append(matriz[pedlf: uedlf])
        else:
            print("error")
        return row
    
    def get_col(self, k):
        """
        Esta función devuelve una lista con la columna de la matriz señalada por el
        parámetro k a través de un for loop de la cantidad de elementos sumando la i
        cada self.c cantidad de columnas, para luego ir agregando los elementos con su  
        apropiado índice a una lista vacía

        """
        matriz = self.a_by_col()
        if 0 < k <= self.c:
            pedlc = self.r * (k-1)
            uedlc = pedlc + self.r
            col = []
            col.append(matriz[pedlc: uedlc])
            return col
   
    def get_elem(self, j, k):
        """
        La función "get_elem" devuelve el valor del número que se encuentra en las
        coordenadas marcadas por los parámetros j y k. Entonces, la función repite
        la metodología de "get_pos", pero en lugar de devolver la posición, devuelve
        el valor del elemento que se encuentra en el índice de la posición dentro de
        la lista en la que está contenida la matriz inicial.

        """
        matriz = self.a_by_row()
        if 0 < k <= self.c and 0 < j <= self.r: 
            p = k + (j-1)*self.c
            return matriz[p-1]
  
    def del_row(self, j):
        """
        "del_row" utiliza las mismas cuentas de "get_row" para saber desde qué 
        elemento hasta qué elemento tiene que eliminar, y en lugar de agregarlos
        a una lista vacía, se agregan todos los demás elementos de la lista inicial
        para generar la nueva matriz sin esa fila. La función devuelve un objeto.

        """
        matriz = self.a_by_row()
        if 0 < j <= self.r:
            pedlf = self.c * (j-1)
            uedlf = pedlf + self.c
            nueva_matriz = matriz[0: pedlf] + matriz[uedlf:]
            return MyArray1(self.r, self.c, nueva_matriz, self.by_row)
    
    def del_row_id(self, j):
        matriz = self.a_by_row()
        aux = MyArray1(self.r, self.c, matriz, True)
        identidad = self.identidad(self.r)
        fila_borrada = identidad.del_row(j)
        identidad_final =  fila_borrada @ aux
        return identidad_final 
  
    def del_col(self, k):  
        """
        A diferencia de "del_row", esta función utiliza un for loop para identificar
        a los elementos de una columna de parámetro k, y los saca, con el .pop(), de la nueva lista
        generada. Al igual que la función anterior, ésta también devuelve un objeto.

        """
        matriz = self.a_by_col()
        if 0 < k <= self.c:
            pedlc = self.r * (k-1)
            uedlc = pedlc + self.r
            nueva_matriz = matriz[0: pedlc] + matriz[uedlc:]
            return MyArray1(self.r, self.c, nueva_matriz, self.by_row) 
    
#    def del_col_id(self, j):
#        matriz = self.a_by_row()
#        aux = MyArray1(self.r, self.c, matriz, True)
#        identidad = self.identidad(self.c)
#        columna_borrada = identidad.del_col(j)
#        identidad_final =  aux @ columna_borrada
#        return identidad_final

    def swap_rows(self, j, k): 
        """
        "swap_rows" devuelve un objeto en donde esta contenida la matriz de manera
        que las filas indicadas en los parámetros j y k intecrambien su posición.
        La función utiliza "get_row" para conseguir una lista de cada fila, y con 
        el .extend() agrega los elementos a una nueva matriz, y con el for loop
        detecta si a la lista vacía (variable "matriz") le debe agregar los elementos
        de qué fila, teniendo en cuenta también las filas que no se desean intercambiar, 
        a través de if, elif y else.

        """
        matriz = self.a_by_row()
        if 0 < j <= self.r or 0 < k <= self.r:
            fila = 1
            for i in range(1, self.r+1):
                if fila == j:
                    fj = self.get_row(i)
                if fila == k:
                    fk = self.get_row(i)
                fila += 1
            nueva_matriz = []
            fila2 = 1
            for i in range(0, len(matriz), self.c):
                if fila2 == j:
                    for e in fk:
                        nueva_matriz.extend(e)
                elif fila2 == k:
                    for e in fj:
                       nueva_matriz.extend(e)
                else:
                    for e in matriz[i: i+self.c]:
                        nueva_matriz.append(e)
                fila2 += 1
            return MyArray1(self.r, self.c, nueva_matriz, self.by_row)
    
#    def swap_rows_id(self, j, k):
#        matriz = self.a_by_row()
#        aux = MyArray1(self.r, self.c, matriz, True)
#        identity = self.identidad(self.r)
#        counter = 1
#        rowj, rowk = identity.get_row(j), identity.get_row(k)
#        for i in range(0, len(identity.elems), identity.r):
#            if counter == j:
#                identity.elems[i: i+identity.r] = rowk
#            elif counter == k:
#                identity.elems[i: i+identity.r] = rowj
#            counter += 1
#        matfinal = identity @ aux
#        return matfinal

    def swap_cols(self, l, m):
        """
        Esta función sigue la misma metodología y cumple la misma función que la
        anteriór, con la diferencia de que en lugar de intercambiar filas, se 
        intercambian columnas. Se llama a la función "get_col" para obtener las
        columnas, y la función devuelve un objeto.

        """
        matriz = self.a_by_col()
        if 0 < l <= self.c or 0 < m <= self.c:
            columna = 1
            for i in range(1, self.c+1):
                if columna == l:
                    cl = self.get_col(i)
                if columna == m:
                    cm = self.get_col(i)
                columna += 1
            nueva_matriz = []
            columna2 = 1
            for i in range(0, len(matriz), self.r):
                if columna2 == m:
                    for e in cl:
                        nueva_matriz.extend(e)
                elif columna2 == l:
                    for e in cm:
                        nueva_matriz.extend(e)
                else:
                    for e in matriz[i: i+self.r]:
                        nueva_matriz.append(e)
                columna2 += 1
            return MyArray1(self.r, self.c, nueva_matriz, self.by_row)
    
#    def swap_cols_id(self, j, k):
#        matriz = self.a_by_row()
#        aux = MyArray1(self.r, self.c, matriz, True)
#        identity = self.identidad(self.c)
#        counter = 1
#        rowj, rowk = identity.get_row(j), identity.get_row(k)
#        for i in range(0, len(identity.elems), identity.r):
#            if counter == j:
#                identity.elems[i: i+identity.r] = rowk
#            elif counter == k:
#                identity.elems[i: i+identity.r] = rowj
#            counter += 1
#        mat_final = aux @ identity
#        return mat_final
#    
    def scale_row(self, j, x):
        """
        Esta función utiliza las mismas cuentas que "get_row" para obtener el primer
        y último elemento de la fila que se desea escalar, y devuelve un objeto con
        la misma matriz, pero la fila j es multiplicada por el número x.

        """
        matriz = self.a_by_row()
        if 0 < j <= self.r:
            pedlf = self.c * (j-1)
            uedlf = pedlf + self.c
            fila = matriz[pedlf:uedlf]
            fila_escalada = []
            for i in fila:
                fila_escalada.append(i*x)
            nueva_matriz = matriz[:pedlf] + fila_escalada + matriz[uedlf:]
        else:
            nueva_matriz = print("error")
        return MyArray1(self.r, self.c, nueva_matriz, self.by_row)
                
    def scale_col(self, k, y):
        """
        Esta función utiliza las mismas cuentas que "get_col" para obtener el primer
        y último elemento de la columna que se desea escalar, y devuelve un objeto con
        la misma matriz, pero la columna k es multiplicada por el número y.

        """
        matriz = self.a_by_col()
        if 0 < k <= self.c:
            pedlc = self.r * (k-1)
            uedlc = pedlc + self.r
            columna = matriz[pedlc:uedlc]
            columna_escalada = []
            for i in columna:
                columna_escalada.append(i*y)
            nueva_matriz = matriz[:pedlc] + columna_escalada + matriz[uedlc:]
        else:
            nueva_matriz = print("error")
        return MyArray1(self.r, self.c, nueva_matriz, self.by_row)
        
    def transpose(self):
        """
       La función "transpose" utiliza "switch", pero no sólo cambia la lectura de
       la matriz, sino que modifica su instancia cambiando la lista de elementos
       e intercambiando el numero de filas por columnas.

        """
        self.elems = self.switch().elems
        rows, columns = self.r , self.c
        self.r, self.c = columns, rows
        actualizacion = print("Ahora la matriz es", self.elems, "de dimension", self.r, "x", self.c)
        return actualizacion

    def flip_rows(self):
        """
       La función "flip_rows" invierte las filas de una matrix x*x. Por ejemplo, si
       una matriz tiene 4 filas, la primera se intercambia con la cuarta, y la
       segunda con la tercera. En caso de tener filas impares, la del medio no se
       mantinene en su lugar. Para esto la función usa un for loop que agarra 
       de a filas y llama a la función "swap_rows" para que las intercambie, y 
       repite el proceso la cantidad de veces que sea necesario según la cantidad
       de filas.

        """
        #Creo una instancia copiando los datos del __init__ para usar como parámetro en el for loop
        new_i = MyArray1(self.r, self.c, self.elems.copy(), self.by_row)
        for i in range(1, (new_i.r//2)+1):
            #Llamo a la función swap_rows con parámetros de la primera y última fila dentro de self.elems.copy() para que se intercambien
            new_i.elems = new_i.swap_rows(i, new_i.r-i+1).elems
        return new_i
    
    def flip_cols(self):
        """
        La función "flip_cols" usa la misma metodología que "flip_rows", pero llama 
        a "swap_cols", y en lugar de tomar como parámetro la cantidad de filas de 
        la clase, toma la cantidad de columnas.

        """
        new_i = MyArray1(self.r, self.c, self.elems.copy(), self.by_row)
        for i in range(1, (new_i.c//2)+1):
            new_i.elems = new_i.swap_cols(i, new_i.c-i+1).elems
        return new_i              
            
    def det(self, matrix_input = None, rows = None, columns = None):
        if matrix_input == None:
            matrix, rows, columns = MyArray1(self.r, self.c, self.elems, self.by_row), self.r, self.c
        if matrix_input != None:
            matrix = MyArray1(rows, columns, matrix_input, self.by_row)
        if self.r != self.c:
            print("error")
        if self.r == 2 and self.c == 2:
            matriz_end = matrix.elems
            return matriz_end[0]*matriz_end[3] + matriz_end[1]*matriz_end[2]
        else:
            fila1 = matrix.get_row(1)
            det = 0
            contador_col = 0
            for i in range(0, columns):
                elems = fila1[i]
                new_elems = []
                for i in range(2, rows+1):
                    fila = matrix.get_row(i)
                    if len(fila) > 1:
                        fila.pop(contador_col)
                        new_elems.extend(fila)           
                    elif len(fila) <= 1:
                        break
            contador_col += 1
            det += elems*((-1)**(1+contador_col))*self.det(matrix_input, rows, columns)
        return det
    
    def __add__(self, x):
        if isinstance(x, int) or isinstance(x, float):
            aux = [element + x for element in self.elems]   
        if isinstance(x, type(self)):
            matriz1, matriz2 = self.a_by_row(), x.a_by_row()
            junta = list(zip(matriz1, matriz2))
            aux = [sum(tupla) for tupla in junta]
        return aux
    
    def __radd__(self, x):
        if isinstance(x, int) or isinstance(x, float):
            return self + x
    
    def __sub__(self, x):
        if isinstance(x, int) or isinstance(x, float):
            aux = [element - x for element in self.elems]
        if isinstance(x, type(self)):
            matriz1, matriz2 = self.a_by_row(), x.a_by_row()
            junta = list(zip(matriz1, matriz2))
            aux = [tupla[0] - tupla[1] for tupla in junta]
        return aux
    
    def __rsub__(self, x):
        if isinstance(x, int) or isinstance(x, float):
            return self - x

    def __mul__(self, x):
        if isinstance(x, int) or isinstance(x, float):
             aux = [element * x for element in self.elems]
        if isinstance(x, type(self)):
            matriz1, matriz2 = self.a_by_row(), x.a_by_row()
            junta = list(zip(matriz1, matriz2))
            aux = [tupla[0] * tupla[1] for tupla in junta]
        return aux
        
    def __rmul__(self, x):
        if isinstance(x, int) or isinstance(x, float):
            return self * x
    
    def __matmul__(self, mat):
        if isinstance(mat, type(self)):
            if self.c == mat.r:
                matriz1, matriz2 = self.a_by_row(), mat.a_by_col()
                matmul1 = []
                for i in range(0, len(matriz1), self.c):
                    mult_row = matriz1[i:i+self.c] * mat.c
                    matmul1.append(mult_row)
                matmul2 = [matriz2]*mat.c
                counter = 0
                matricesjuntas = []
                for i in matmul1:
                    ziprow = list(zip(i, matmul2[counter]))
                    for a in range(0, len(matriz2), self.c):
                        matricesjuntas.append(ziprow[a: a+mat.r])
                    counter += 1
                aux1 = []       
                for element in matricesjuntas:
                    aux1.append(list(map(lambda x: x[0]*x[1],element)))
                aux2 = list((sum(elements) for elements in aux1))
            else:
                print('La cantidad de columnas de la primera matriz no coincide con la cantidad de filas de la segundo')
                aux2 = None
            return aux2
       
    def __pow__(self, x):
        if isinstance(x, int):
            matriz = self.a_by_row()
            aux_instance = MyArray1(self.r, self.c, matriz, True)
            changing_aux_instance = MyArray1(self.r, self.c, matriz, True)
            for i in range(x-1):
                matriz = changing_aux_instance @ aux_instance
                changing_aux_instance = MyArray1(self.r, self.c, matriz, True)
            aux = changing_aux_instance.elems
            return aux



if __name__ == "__main__":
       matriz1 = MyArray1(3,3,[1, 2, 3, 4, 5, 6, 7, 8, 9], True)
       matriz2 = MyArray1(3,3,[1, 2, 3, 4, 5, 6, 7, 8, 9], True)
       
       #print(matriz1.get_pos(1, 1))
       #print(matriz2.get_pos(1, 3))
       
       #print(matriz1.get_coords(11))
       #print(matriz2.get_coords(10))
       
       #print(matriz1.switch().elems)
       #print(matriz2.switch().elems)

       
       #print(matriz1.get_row(2))
       #print(matriz2.get_row(2))
       
       #print(matriz1.get_col(2))
       #print(matriz2.get_col(2))
       
       #print(matriz1.get_elem(3, 3))
       #print(matriz2.get_elem(3, 1))
       
       #print(matriz1.del_row(2).elems)
       #print(matriz2.del_row(2).elems)
       
       #print(matriz1.del_col(2).elems)
       #print(matriz2.del_col(2).elems)

       #print(matriz1.swap_rows(2, 3).elems)
       #print(matriz2.swap_rows(3, 3).elems)

       #print(matriz1.swap_cols(2, 3).elems)
       #print(matriz2.swap_cols(2, 3).elems)
       
       #print(matriz1.scale_row(3, 3).elems)
       #print(matriz2.scale_row(3, 3).elems)
       
       #print(matriz1.scale_col(2, 3).elems)
       #print(matriz2.scale_col(2, 3).elems)

       #matriz1.transpose()
       #matriz2.transpose()
       
       #print(matriz1.flip_rows().elems)
       #print(matriz2.flip_rows().elems)
       
       #print(matriz1.flip_cols().elems)
       #print(matriz2.flip_cols().elems)
       
       ###print(matriz1.det())
       ###print(matriz2.det())

       #sumapruebamatriz = matriz1 + matriz2
       #sumapruebanumero = matriz1 + 10
       #rsumapruebanumero = 10 + matriz1
       #print(sumapruebamatriz, sumapruebanumero, rsumapruebanumero)    

       #restapruebamatriz = matriz1 - matriz2
       #restapruebanumero = matriz1 - 10
       #rrestapruebanumero = 10 - matriz1
       #print(restapruebamatriz, restapruebanumero, rrestapruebanumero)    

       #multpruebamatriz = matriz1 * matriz2
       #multpruebanumero = matriz1 * 10
       #rmultpruebanumero = 10 * matriz1
       #print(multpruebamatriz, multpruebanumero, rmultpruebanumero)    

       #matmulprueba = matriz1 @ matriz2
       #print(matmulprueba)

       #powprueba = matriz1 ** 2
       #print(powprueba)

       #print(matriz1.identidad(3).elems)
       #pruebarowsidentidad = matriz1.swap_rows_id(1, 3)
       #pruebacolsidentidad = matriz1.swap_cols_id(1, 3)
       #print(pruebarowsidentidad)
       #print(pruebacolsidentidad)

       #deleterowidentidad = matriz1.del_row_id(1)
       #print(deleterowidentidad)
       ###deletecolidentidad = matriz1.del_col_id(1)
       ###print(deletecolidentidad)
       

 