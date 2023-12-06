""" Clase principal para el problema de la mochila """

class ProblemaMochila:
    def __init__(self, ítems, utilidades, pesos, límite):
        self.ítems = ítems
        self.utilidades = utilidades
        self.pesos = pesos
        self.límite = límite
        self.num_items = len(items)

    def vector_ítems(self, vector):
        return [self.ítems[i] for i in range(len(vector)) if vector[i] == 1]

    def vector_utilidades(self, vector):
        return np.array([list(self.utilidades.values())[i] for i in range(len(self.utilidades)) if vector[i] == 1])

    def vector_pesos(self, vector):
        return np.array([list(self.pesos.values())[i] for i in range(len(self.pesos)) if vector[i] == 1])

    def generar_solucion_aleatoria(num_items):
        return np.array([random.randint(0, 1) for _ in range(num_items)])

    def tabu_search(self.pesos, self.utilidades, capacidad_mochila, max_iter=200, Life=8):
        tabu_list = []
        c = 1
        X_best = generar_solucion_aleatoria(self.num_items)
        X_vpesos = vector_pesos(X_best)
        X_vutilidades = vector_utilidades(X_best)
        Curl_W = X_best.dot(X_vpesos)
        while c<=max_iter:
            N = {i for i in range(num_items)}
            start = max([0, c-Life])
            for j in range(start, c)
                N = N 


    
