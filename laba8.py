import numpy as np
import random as rd

from collections import deque


def bfs_1(matrix, start):
    n = len(matrix)          
    visited = set()
    queue = deque([start])   
    result = []             
    
    visited.add(start)
    
    while queue:
        vertex = queue.popleft()
        result.append(vertex)
        
        # Проверяем всех соседей текущей вершины
        for neighbor in range(n):
            # Если есть ребро и вершина не посещена
            if matrix[vertex][neighbor] == 1 and neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return result


def bfs_2(adj_list, start):
    n = len(adj_list)
    visited = set()
    queue = deque([start])
    result = []

    visited.add(start)

    while(queue):
        vertex = queue.popleft()
        result.append(vertex)

        for neighbor in range(n):
            if neighbor not in visited:

                visited.add(neighbor)
                queue.append(neighbor)

    return result



def generator_smezh(razm):
    matr_sm = np.matrix(np.array([abs(rd.randint(-1000, 1000))%2 for _ in range(razm) for _ in range(razm)]).reshape(razm, razm))

    for i in range(razm):
        matr_sm[i, i] = 0
        for j in range(razm):
            if i<=j:
                matr_sm[i,j] = matr_sm[j, i]

    print(matr_sm)
    return matr_sm.tolist()


def matrix_to_adj_list(matrix):
    """Функциональный стиль преобразования"""
    return [
        [j for j in range(len(matrix)) if matrix[i][j] != 0]
        for i in range(len(matrix))
    ]



def main():
    G = generator_smezh(int(input("Введите количество вершин в графе: ")))
    print(f"для матричного представления:\t{bfs_1(G, int(input("Введите вершину с которой хотите начать:\t")))}\n")


    G = matrix_to_adj_list(G)
    print(f"для спискового представления:\t{bfs_2(G, int(input("Введите вершину с которой хотите начать:\t")))}\n")


if __name__ == "__main__":
    main()