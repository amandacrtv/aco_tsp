import sys
from ACO import ACO
from Graph import generate_graph


ANTS_N = 100 #mumero de formigas
GEN_N = 100 #numero de geracoes
ALPHA = 10 #peso do feromonio
BETA = 20 #peso da desirability
RHO = 0.5 #taxa de evaporacao
INT_FE = 10 #constante usada na atualizacao


def main():
    if len(sys.argv) != 2:
        print('Uso: main.py dataset.txt')
        sys.exit()
    input_path = sys.argv[1]
    graph = generate_graph(input_path)
    aco = ACO(ANTS_N, GEN_N, ALPHA, BETA, RHO, INT_FE)
    sum_weight = 0
    for _ in range(10):
        aco = ACO(ANTS_N, GEN_N, ALPHA, BETA, RHO, INT_FE)
        path, cost = aco.solve(graph)
        sum_weight += cost
    print(ANTS_N, GEN_N, ALPHA, BETA, RHO, INT_FE)
    print("weight: {0}".format(sum_weight/10))
    

if __name__== "__main__":
  main()
