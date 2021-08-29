import random 
class Ant:
    def __init__(self, aco, graph):
        self.colony = aco
        self.graph = graph
        self.t_weight = 0
        self.tabu = []
        self.pheromone_delta = []
        self.allowed = [i for i in range(graph.m_len)]
        self.eta = [[graph.matrix[i][j][1] / 100 for j in range(len(graph.matrix[i]))] for i in range(graph.m_len)]
        start = random.randint(0, graph.m_len - 1)
        self.tabu.append(start)
        self.current = start
        self.allowed.remove(start)
    
    def select_next(self):
        factor = 0
        curr_allowed_index = []
        curr_allowed_point = []
        for j, arr in enumerate(self.graph.matrix[self.current]):
            if arr[0] in self.allowed:
                curr_allowed_index.append(j)
                curr_allowed_point.append(arr[0])
        if len(curr_allowed_index) > 0:
            for i in curr_allowed_index:
                factor += self.graph.pheromone[self.current][i] ** self.colony.alpha * self.eta[self.current][i] ** self.colony.beta
            
            probs = [0 for i in range(self.graph.m_len)]

            for i in range(self.graph.m_len):
                try:
                    index_point = curr_allowed_point.index(i)
                    probs[i] = self.graph.pheromone[self.current][curr_allowed_index[index_point]] ** self.colony.alpha * self.eta[self.current][curr_allowed_index[index_point]] ** self.colony.beta / factor
                except ValueError:
                    pass 
                except ZeroDivisionError:
                    probs[i] = 0
            
            selected = 0
            rand = random.random()
            selected_index = 0

            for i, prob in enumerate(probs):
                try:
                    rand -= prob
                    selected_index = curr_allowed_point.index(i)
                    if rand <= 0:
                        selected = i
                        break
                except ValueError:
                    pass
            if selected in self.allowed:
                self.allowed.remove(selected)
                self.tabu.append(selected)
                self.t_weight += self.graph.matrix[self.current][selected_index][1]
                self.current = selected
    
    def update_pheromone_delta(self):
        self.pheromone_delta = [[0 for __ in range(self.graph.m_len)] for _ in range(self.graph.m_len)]
        for __ in range(1, len(self.tabu)):
            i = self.tabu[__ - 1]
            j = self.tabu[__]
            self.pheromone_delta[i][j] = self.colony.q * (self.t_weight / 100)