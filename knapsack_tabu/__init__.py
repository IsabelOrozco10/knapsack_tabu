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



#-----------------------------
import random

def generar_solucion_inicial(mochila):
    return [random.choice([0, 1]) for i in range(len(mochila))]

def evaluar_solucion(solucion, mochila, capacidad_maxima):
    # La función zip combina elementos de las listas mochila y solucion en tuplas
    peso_total = sum(peso * incluido for peso, incluido in zip(mochila, solucion))
    valor_total = sum(valor * incluido for valor, incluido in zip(mochila, solucion))
    
    if peso_total > capacidad_maxima:
        return 0  # Penalizar soluciones que exceden la capacidad
    else:
        return valor_total

def generar_vecindario(solucion_actual):
    vecindario = []
    for i in range(len(solucion_actual)):
        vecino = list(solucion_actual)
        vecino[i] = 1 - vecino[i]  # Cambiar el estado del objeto
        vecindario.append(vecino)
    return vecindario

def encontrar_mejor_vecino(vecindario, lista_tabu):
    mejores_vecinos = [(vecino, evaluar_solucion(vecino, mochila, capacidad_maxima)) for vecino in vecindario if vecino not in lista_tabu]
    if mejores_vecinos:
        return max(mejores_vecinos, key=lambda x: x[1])[0]
    else:
        return random.choice(vecindario)

def busqueda_tabu(mochila, capacidad_maxima, iteraciones, longitud_maxima_lista_tabu):
    mejor_solucion = generar_solucion_inicial(mochila)
    mejor_valor = evaluar_solucion(mejor_solucion, mochila, capacidad_maxima)
    lista_tabu = []

    for _ in range(iteraciones):
        vecindario = generar_vecindario(mejor_solucion)
        mejor_vecino = encontrar_mejor_vecino(vecindario, lista_tabu)

        valor_vecino = evaluar_solucion(mejor_vecino, mochila, capacidad_maxima)

        if valor_vecino > mejor_valor:
            mejor_solucion = mejor_vecino
            mejor_valor = valor_vecino

        lista_tabu.append(mejor_vecino)
        if len(lista_tabu) > longitud_maxima_lista_tabu:
            lista_tabu.pop(0)

    return mejor_solucion, mejor_valor

# Ejemplo de uso
mochila = [5, 10, 8, 5]
capacidad_maxima = 20
iteraciones = 100
longitud_maxima_lista_tabu = 5

mejor_solucion, mejor_valor = busqueda_tabu(mochila, capacidad_maxima, iteraciones, longitud_maxima_lista_tabu)
print("Mejor solución encontrada:", mejor_solucion)
print("Mejor valor:", mejor_valor)
