import re
""" 
iniciar feromonio com mesmo valor para todas as arestas
"""

class Graph:
    def __init__(self, matrix, m_len):
        self.matrix = matrix
        self.m_len = m_len
        pow_len = m_len ** 2
        self.pheromone = [[1 / (pow_len) for j in range(len(matrix[i]))] for i in range(m_len)]

""" 
matriz de grafos
sendo que a linha representa o primeiro ponto 
e a coluna eh uma lista com o segundo do vertice e o peso
obs: ponto subtrai 1 para economizar espaco na matriz
ex: vertice 1, x = matriz[0]
"""

def generate_graph(path):
    first_points = []
    second_points = []
    weights = []
    with open(path, 'r') as reader:
        for line in reader:
            line_vars = list(filter(None, re.sub(r"\s+", '  ', line).split('  ')))
            first_points.append(int(line_vars[0]))
            second_points.append(int(line_vars[1]))
            weights.append(int(line_vars[2]))
    graph_size = max(max(first_points), max(second_points))
    graph = [[] for _ in range(graph_size)] 
    for i in range(len(weights)):
        graph[first_points[i]-1].append([second_points[i]-1, weights[i]])
    g_obj = Graph(graph, graph_size)
    return g_obj