""" Clase principal para el problema de la mochila """

class ProblemaMochila:
    def __init__(self, ítems, utilidades, pesos, límite):
        self.ítems = ítems
        self.utilidades = np.array([list(utilidades.values())[i] for i in range(len(utilidades))])
        self.pesos = np.array([list(pesos.values())[i] for i in range(len(pesos))])
        self.límite = límite
        self.num_items = len(items)

    def vector_ítems(self, vector):
        return {self.ítems[i] for i in range(len(vector)) if vector[i] == 1}

    def vector_utilidades(self):
        return np.array([list(self.utilidades.values())[i] for i in range(len(self.utilidades))])

    def vector_pesos(self):
        return np.array([list(self.pesos.values())[i] for i in range(len(self.pesos))])

    def generar_solucion_aleatoria(num_items):
        return np.array([random.randint(0, 1) for _ in range(num_items)])

    def encuentra_mejor_cambio(self, vector_actual, indices):
        i_best = indice[0]
        for i in indices:
            

    def tabu_search(self.pesos, self.utilidades, capacidad_mochila, max_iter=200, Life=8):
        tabu_list = []
        c = 1
        X_best = generar_solucion_aleatoria(self.num_items)
        Curl_W = X_best.dot(pesos)
        X = X_best
        while c<=max_iter:
            N = [i for i in range(num_items)]
            start = max([0, c-Life])
            for i in range(start, c)
                N = N.remove(tabu_list[j])
            for i in N:
                if (X[i] == 0) and (Cur_W + pesos[i] > capacidad_mochila):
                    N = N.remove(i)
            if N != null:
                

    
