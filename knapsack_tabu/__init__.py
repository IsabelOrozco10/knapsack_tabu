""" Clase principal para el problema de la mochila """

class ProblemaMochila:
    def __init__(self, ítems, utilidades, pesos, límite):
        self.ítems = ítems
        self.utilidades = np.array([list(utilidades.values())[i] for i in range(len(utilidades))])
        self.pesos = np.array([list(pesos.values())[i] for i in range(len(pesos))])
        self.límite = límite
        self.num_items = len(self.ítems)

    def vector_ítems(self, vector):
        """
        Esta método permite conocer la lista de objetos que representa un vector binario.
        
        Parametros:
            vector(array): Vector binario que representa una lista de objetos.
            
        Returns:
            list: Lista de objetos que reprenta el vector binario.
        """
        return [self.ítems[i] for i in range(len(vector)) if vector[i] == 1]

    def generar_solucion_aleatoria(self):
        """
        Genera una solución aleatoria para el problema.

        Esta función crea una solución aleatoria representada como un array de NumPy
        de 0s y 1s, donde cada elemento indica si el ítem correspondiente está incluido o no.

        Returns:
        numpy.ndarray: Un array de NumPy que representa la solución aleatoria.
        """
        return np.array([random.randint(0, 1) for _ in range(self.num_items)])

    def mejor_cambio(self, indices, v_actual):
         """
        Encuentra el índice que representa la mejor opción de cambio en función de utilidades y pesos.

        Esta función toma una lista de índices `indices` y un array `v_actual` que representa
        la configuración actual del problema. Evalúa las opciones en términos de utilidades y
        pesos, y devuelve el índice de la mejor opción de cambio.

        Args:
            -indices (list): Lista de índices disponibles para evaluar.
            -v_actual (numpy.ndarray): Array que representa la configuración actual del problema.

        Returns:
            -int: Índice de la mejor opción de cambio.
        """
        #Inicializar el índice y la utilidad del mejor cambio con el primer índice del conjunto.
        i_best = indices[0]
        u_best = (self.utilidades[i_best]/self.pesos[i_best])*((-1)**(v_actual[i_best]))
        # Iterar sobre los índices restantes y actualizar el índice del mejor cambio si se encuentra una utilidad mejor.
        for i in indices:
            # Calcular la utilidad para el índice actual.
            u_i = (self.utilidades[i]/self.pesos[i])*((-1)**(v_actual[i]))
            # Verificar si la utilidad actual es mayor o igual a la utilidad del mejor cambio.
            if u_i > u_best:
                i_best = i
        # Retornar el índice del mejor cambio.
        return i_best
    
    def utilidad(self, vector):
         """
        Calcula la utilidad total en función de un vector de selección.
        Args:
            -vector (numpy.ndarray): Vector de selección binario que indica qué ítems están incluidos.
        Returns:
            -float: La utilidad total calculada.
        """
        return self.utilidades.dot(vector)
    
    def tabu_search(self, max_iter=20, L=8):
        """
        Realiza una búsqueda tabú para encontrar una solución óptima.

        Esta función implementa un algoritmo de búsqueda tabú para encontrar una solución
        óptima para el problema, considerando restricciones de peso y utilidad.

        Args:
            -max_iter (int): Número máximo de iteraciones para el algoritmo (por defecto, 20).
            -L (int): Longitud máxima de la lista tabú (por defecto, 8).

        Returns:
            Tuple[numpy.ndarray, float, float]:
                - La mejor solución encontrada (array binario).
                - Peso total de la mejor solución.
                - Utilidad total de la mejor solución.
        """
        tabu_list = []
        c = 1
        X = self.generar_solucion_aleatoria()
        X_best = X.copy()
        Curl_W = X_best.dot(self.pesos)
        while c<=max_iter:
            N = {i for i in range(self.num_items)}
            if len(tabu_list) != 0:
                N = N-tabu_list
            aux = set()
            for i in N:
                if (X[i] == 0) and (Curl_W + self.pesos[i] > self.límite):
                    aux.add(i)
            N = N-aux
            if len(N) != 0:
                i_posible = self.mejor_cambio(list(N), X)
                if len(tabu_list) > L:
                    tabu_list.pop()
                    tabu_list.add(i_posible)
                else:
                    tabu_list.add(i_posible)
                X[i_posible] = 1-X[i_posible]
                if X[i_posible] == 1:
                    Curl_W = Curl_W + self.pesos[i_posible]
                else:
                    Curl_W = Curl_W - self.pesos[i_posible]
                if self.utilidad(X) > self.utilidad(X_best):
                    X_best = X.copy()
            c += 1
        return X_best, Curl_W, self.utilidad(X_best)
