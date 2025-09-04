# 8-Puzzle A* Solver - Terminal Demo
from typing import Tuple, List, Optional
import heapq

def manhattan(state: Tuple[int, ...], goal: Tuple[int, ...]) -> int:
    pos_goal = {val: (i // 3, i % 3) for i, val in enumerate(goal)}
    soma = 0
    for i, val in enumerate(state):
        if val == 0:
            continue
        linha, col = i // 3, i % 3
        linha_goal, col_goal = pos_goal[val]
        soma += abs(linha - linha_goal) + abs(col - col_goal)
    return soma

def get_neighbors(state: Tuple[int, ...]) -> List[Tuple[int, ...]]:
    idx = state.index(0)
    linha, col = idx // 3, idx % 3
    moves = [(-1,0),(1,0),(0,-1),(0,1)]
    neighbors = []
    for dl, dc in moves:
        nl, nc = linha + dl, col + dc
        if 0 <= nl < 3 and 0 <= nc < 3:
            nidx = nl * 3 + nc
            lst = list(state)
            lst[idx], lst[nidx] = lst[nidx], lst[idx]
            neighbors.append(tuple(lst))
    return neighbors

def inversoes(state: Tuple[int, ...]) -> int:
    arr = [x for x in state if x != 0]
    inv = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                inv += 1
    return inv

def eh_solvel(start: Tuple[int, ...], goal: Tuple[int, ...]) -> bool:
    return inversoes(start) % 2 == inversoes(goal) % 2

def a_star(start: Tuple[int, ...], goal: Tuple[int, ...]) -> Optional[List[Tuple[int, ...]]]:
    hfunc = lambda s: manhattan(s, goal)
    heap = []
    heapq.heappush(heap, (hfunc(start), 0, start, [start]))
    cost_so_far = {start: 0}
    while heap:
        f, g, current, path = heapq.heappop(heap)
        if current == goal:
            return path
        for neighbor in get_neighbors(current):
            new_g = g + 1
            if neighbor not in cost_so_far or new_g < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_g
                heapq.heappush(heap, (new_g + hfunc(neighbor), new_g, neighbor, path + [neighbor]))
    return None

def print_board(state: Tuple[int, ...]):
    for i in range(3):
        print(state[i*3:(i+1)*3])
    print()

def main():
    print("Digite o estado inicial (ex: 1,2,3,4,5,6,7,8,0):")
    start = tuple(int(x) for x in input().strip().split(","))
    print("Digite o estado objetivo (ex: 1,2,3,4,5,6,7,8,0):")
    goal = tuple(int(x) for x in input().strip().split(","))
    print("Inversões inicial:", inversoes(start), "| objetivo:", inversoes(goal))
    if not eh_solvel(start, goal):
        print("Este estado não é solúvel para o objetivo!")
        return
    path = a_star(start, goal)
    if path:
        print(f"Solução encontrada em {len(path)-1} movimentos:")
        for idx, state in enumerate(path):
            print(f"Passo {idx}:")
            print_board(state)
    else:
        print("Não foi encontrada solução.")

if __name__ == "__main__":
    main()
