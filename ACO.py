from Ant import Ant

class ACO:
    """  
    count: qtd de formigas
    gen_s: qtd de geracoes
    alpha: importante pro feromonio
    beta: importante para heuristica
    rho: coeficiente residual do feromonio
    q: intensidade feromonio
    """
    def __init__(self, count, gen_s, alpha, beta, rho, q):
        self.count = count
        self.gen_s = gen_s
        self.alpha = alpha
        self.beta = beta
        self.rho = rho
        self.q = q
    
    def update_phe(self, graph, ants):
        for i in range(len(graph.pheromone)):
            for j in range(len(graph.pheromone[i])):
                graph.pheromone[i][j] *= self.rho
            for ant in ants:
                graph.pheromone[i][j] += ant.pheromone_delta[i][j]
    
    def solve(self, graph):
        b_weight = 0
        b_solution = []

        for _ in range(self.gen_s):
            ants = [Ant(self, graph) for __ in range(self.count)]
            for ant in ants:
                for __ in range(graph.m_len - 1):
                    ant.select_next()
                
                for j in range(len(graph.matrix[ant.tabu[-1]])):
                    if graph.matrix[ant.tabu[-1]][j][0] == ant.tabu[0]:
                        ant.t_weight += graph.matrix[ant.tabu[-1]][j][1]
                        break
                if ant.t_weight > b_weight:
                    b_weight = ant.t_weight
                    b_solution = [] + ant.tabu
                ant.update_pheromone_delta()
            self.update_phe(graph, ants)
        b_solution = [i+1 for i in b_solution]
        return b_solution, b_weight