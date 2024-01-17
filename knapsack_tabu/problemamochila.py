import numpy as np
import random

class ProblemaMochilaMod:
    def __init__(self, ítems, utilidades, pesos, límite):
        self.ítems = ítems
        self.utilidades = np.array([list(utilidades.values())[i] for i in range(len(utilidades))])
        self.pesos = np.array([list(pesos.values())[i] for i in range(len(pesos))])
        self.límite = límite
        self.num_items = len(self.ítems)

    def vector_ítems(self, vector):
        """
        Genera una lista de ítems seleccionados basándose en un vector binario.

        Parámetros:
        - vector (list): Un vector binario donde cada elemento indica la decisión de incluir (1) o no incluir (0) un ítem.

        Retorno:
        - list: Una lista de ítems asociados a las posiciones donde el valor en el vector es igual a 1.
        """
        return [self.ítems[i] for i in range(len(vector)) if vector[i] == 1]


    def generar_solucion_aleatoria(self):
        """
        Genera una solución aleatoria para el problema de la mochila.

        Retorna:
        - np.array: Un array NumPy que representa una solución aleatoria, donde cada elemento indica la decisión de incluir (1) o no incluir (0) un ítem en la mochila.
        """
        return np.array([random.randint(0, 1) for _ in range(self.num_items)])


    def mejor_cambio(self, indices, v_actual):
        """
        Determina el mejor índice de cambio en función de la relación utilidad/peso.

        Parámetros:
        - indices (list): Lista de índices disponibles para el cambio.
        - v_actual (list): Vector binario actual que representa la solución actual.

        Retorna:
        - int: El índice del mejor cambio en la lista de índices.
        """
        # Inicializar el índice y la utilidad del mejor cambio con el primer índice del conjunto.
        i_best = indices[0]
        u_best = (self.utilidades[i_best] / self.pesos[i_best]) * ((-1) ** (v_actual[i_best]))

        # Iterar sobre los índices restantes y actualizar el índice del mejor cambio si se encuentra una utilidad mejor.
        for i in indices:
            # Calcular la utilidad para el índice actual.
            u_i = (self.utilidades[i] / self.pesos[i]) * ((-1) ** (v_actual[i]))

            # Verificar si la utilidad actual es mayor o igual a la utilidad del mejor cambio.
            if u_i >= u_best:
                i_best = i

        # Retornar el índice del mejor cambio.
        return i_best


    def utilidad(self, vector):
        """
        Calcula la utilidad total asociada a un vector binario dado.

        Parámetros:
        - vector (list): Un vector binario donde cada elemento indica la decisión de incluir (1) o no incluir (0) un ítem.

        Retorna:
        - float: La utilidad total calculada multiplicando el vector binario por el vector de utilidades y sumando los productos resultantes.
        """
        return self.utilidades.dot(vector)


    def num_solucion(self, vector):
        """
        Convierte un vector binario en un número entero.

        Parámetros:
        - vector (list): Un vector binario donde cada elemento indica la decisión de incluir (1) o no incluir (0) un ítem.

        Retorna:
        - int: El número entero resultante de la conversión del vector binario.
        """
        # Inicializar una cadena vacía para almacenar la representación binaria del número.
        n_bin = ""

        # Iterar sobre cada elemento del vector binario.
        for bin_value in vector:
            # Concatenar la representación en cadena de cada elemento al final de n_bin.
            n_bin = n_bin + str(bin_value)

        # Convertir la cadena binaria a un número entero en base 2.
        return int(n_bin, 2)


    def tabu_search(self, max_iter=20, L=8):
        """
        Implementa el algoritmo de búsqueda tabú para resolver el problema de la mochila.

        Parámetros:
        - max_iter (int): Número máximo de iteraciones del algoritmo (default: 20).
        - L (int): Longitud máxima de la lista tabú (default: 8).

        Retorna:
        - tuple: Una tupla que contiene la mejor solución encontrada, el número asociado a la solución, el peso total y la utilidad total.
        """

        # Inicialización de variables
        tabu_list = []  # Lista tabú para almacenar índices prohibidos temporalmente
        c = 1  # Contador de iteraciones
        X = self.generar_solucion_aleatoria()  # Generar solución aleatoria inicial
        X_best = X.copy()  # Mejor solución actual
        Curl_W = X_best.dot(self.pesos)  # Peso total de la mejor solución actual

        # Bucle principal de la búsqueda tabú
        while c <= max_iter:
            N = {i for i in range(self.num_items)}  # Conjunto de todos los índices disponibles

            # Excluir índices en la lista tabú del conjunto de índices disponibles
            if len(tabu_list) != 0:
                for i in tabu_list:
                    N.remove(i)

            aux = set()  # Conjunto auxiliar para almacenar índices que deben ser excluidos
            for i in N:
                # Verificar si se puede incluir el ítem i sin exceder el límite de peso
                if (X[i] == 0) and (Curl_W + self.pesos[i] > self.límite):
                    aux.add(i)

            N = N - aux  # Actualizar conjunto de índices disponibles

            if len(N) != 0:
                # Determinar el mejor índice de cambio utilizando la función mejor_cambio
                i_posible = self.mejor_cambio(list(N), X)

                # Actualizar la lista tabú
                if len(tabu_list) < L:
                    tabu_list.append(i_posible)
                else:
                    tabu_list.pop(0)
                    tabu_list.append(i_posible)

                # Realizar el cambio en la solución actual
                X[i_posible] = 1 - X[i_posible]

                # Actualizar el peso total de la solución actual
                if X[i_posible] == 1:
                    Curl_W = Curl_W + self.pesos[i_posible]
                else:
                    Curl_W = Curl_W - self.pesos[i_posible]

                # Actualizar la mejor solución si la nueva solución es mejor
                if self.utilidad(X) > self.utilidad(X_best):
                    X_best = X.copy()

            c += 1

    # Retornar la mejor solución encontrada junto con información adicional
        return X_best, self.utilidad(X_best), self.num_solucion(X_best), Curl_W

    def ejecutar_con_varios_L(self, max_iter=20, max_L=8):
        resultados = PrettyTable(['L', 'Mejor Solución Binaria', 'Mejor Solución Traducida', 'Utilidad'])
        for L in range(1, max_L + 1):
            mejor_solucion_binaria, utilidad = self.tabu_search(max_iter=max_iter, L=L)[:2]

            # Obtener nombres de ítems para la mejor solución binaria
            nombres_mejor_solucion = self.vector_ítems(mejor_solucion_binaria.tolist())

            # Obtener utilidades de la mejor solución binaria
            utilidades_mejor_solucion = self.utilidades[mejor_solucion_binaria.astype(bool)].tolist()

            resultados.add_row([L, mejor_solucion_binaria.tolist(), nombres_mejor_solucion, utilidad])

            # Ajustes manuales de ancho de columnas
            resultados._max_width = {"Mejor Solución Binaria": 20, "Mejor Solución Traducida": 30, "Utilidades": 20, "Utilidad Total": 15}
        return resultados
