from typing import List, Tuple, Optional
import heapq
from flask import Flask, request, jsonify, render_template_string

goal = (1,2,3,4,5,6,7,8,0)

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

def misplaced(state: Tuple[int, ...], goal: Tuple[int, ...]) -> int:
  return sum(1 for i, v in enumerate(state) if v != 0 and v != goal[i])

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

def a_star(start: Tuple[int, ...], goal: Tuple[int, ...], heuristic: str) -> Optional[List[Tuple[int, ...]]]:
  if heuristic == "manhattan":
    hfunc = lambda s: manhattan(s, goal)
  else:
    hfunc = lambda s: misplaced(s, goal)
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
def distancia_manhattan(estado: Tuple[int, ...], objetivo: Tuple[int, ...]) -> int:
    pos_objetivo = {val: (i // 3, i % 3) for i, val in enumerate(objetivo)}
    soma = 0
    for i, val in enumerate(estado):
        if val == 0:
            continue
        linha, col = i // 3, i % 3
        linha_obj, col_obj = pos_objetivo[val]
        soma += abs(linha - linha_obj) + abs(col - col_obj)
    return soma

def fora_do_lugar(estado: Tuple[int, ...], objetivo: Tuple[int, ...]) -> int:
    return sum(1 for i, v in enumerate(estado) if v != 0 and v != objetivo[i])

def vizinhos(estado: Tuple[int, ...]) -> List[Tuple[int, ...]]:
    idx = estado.index(0)
    linha, col = idx // 3, idx % 3
    movimentos = [(-1,0),(1,0),(0,-1),(0,1)]
    vizinhos = []
    for dl, dc in movimentos:
        nl, nc = linha + dl, col + dc
        if 0 <= nl < 3 and 0 <= nc < 3:
            nidx = nl * 3 + nc
            lst = list(estado)
            lst[idx], lst[nidx] = lst[nidx], lst[idx]
            vizinhos.append(tuple(lst))
    return vizinhos

def a_estrela(inicial: Tuple[int, ...], objetivo: Tuple[int, ...], heuristica: str) -> Optional[List[Tuple[int, ...]]]:
    if heuristica == "manhattan":
        hfunc = lambda s: distancia_manhattan(s, objetivo)
    else:
        hfunc = lambda s: fora_do_lugar(s, objetivo)
    heap = []
    heapq.heappush(heap, (hfunc(inicial), 0, inicial, [inicial]))
    custo_ate_agora = {inicial: 0}
    while heap:
        f, g, atual, caminho = heapq.heappop(heap)
        if atual == objetivo:
            return caminho
        for vizinho in vizinhos(atual):
            novo_g = g + 1
            if vizinho not in custo_ate_agora or novo_g < custo_ate_agora[vizinho]:
                custo_ate_agora[vizinho] = novo_g
                heapq.heappush(heap, (novo_g + hfunc(vizinho), novo_g, vizinho, caminho + [vizinho]))
    return None

def inversoes(estado: Tuple[int, ...]) -> int:
    arr = [x for x in estado if x != 0]
    inv = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                inv += 1
    return inv

def eh_solucionavel(inicial: Tuple[int, ...], objetivo: Tuple[int, ...]) -> bool:
    return inversoes(inicial) % 2 == inversoes(objetivo) % 2
from flask import Flask, request, jsonify, render_template_string
import heapq
from typing import List, Tuple, Optional

goal = (1,2,3,4,5,6,7,8,0)

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

def misplaced(state: Tuple[int, ...], goal: Tuple[int, ...]) -> int:
    return sum(1 for i, v in enumerate(state) if v != 0 and v != goal[i])

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

def a_star(start: Tuple[int, ...], goal: Tuple[int, ...], heuristic: str) -> Optional[List[Tuple[int, ...]]]:
  if heuristic == "manhattan":
    hfunc = lambda s: manhattan(s, goal)
  else:
    hfunc = lambda s: misplaced(s, goal)
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

app = Flask(__name__)

HTML = '''
<!DOCTYPE html>
<html lang="pt">
<head>
<meta charset="utf-8" />
<title>8-Puzzle Go Web</title>
<style>
body { font-family: Arial, sans-serif; background: #222; color: #eee; }
.container { max-width: 700px; margin: 40px auto; }
h2 { margin-bottom: 18px; }
.row { display: flex; align-items: center; gap: 16px; margin-bottom: 12px; }
.board { display: grid; grid-template-columns: repeat(3, 60px); grid-gap: 8px; margin: 20px 0; justify-content: start; }
.tile { width: 60px; height: 60px; background: #444; display: flex; align-items: center; justify-content: center; font-size: 2em; border-radius: 8px; transition: background 0.3s, transform 0.3s; }
.tile.empty { background: #222; }
.tile.moving { background: #3b82f6; color: #fff; transform: scale(1.1); }
input, select, button { margin: 0 4px; padding: 6px; border-radius: 6px; border: none; font-size: 1em; }
button { background: #3b82f6; color: white; font-weight: bold; cursor: pointer; }
#controls { margin-bottom: 8px; }
</style>
</head>
<body>
<div class="container">
<h1>8-Puzzle Visual</h1>
<div class="instructions">
Digite o estado inicial e objetivo usando números de 0 a 8 (0 é o espaço vazio).<br>
Clique em "Resolver" para ver os movimentos passo a passo.<br>
Se quiser um desafio, clique em "Embaralhar" para gerar um estado inicial solúvel aleatório.
</div>
<h2>Resolver o 8-Puzzle</h2>
<form id="form" class="row">
  <label for="start">Estado inicial:</label>
  <input id="start" value="1,2,3,4,5,6,7,0,8" size="20" placeholder="Ex: 1,2,3,4,5,6,7,8,0">
  <label for="goal">Estado objetivo:</label>
  <input id="goal" value="1,2,3,4,5,6,7,8,0" size="20" placeholder="Ex: 1,2,3,4,5,6,7,8,0">
  <label for="heuristic">Heurística:</label>
  <select id="heuristic"><option value="manhattan">Manhattan</option><option value="misplaced">Blocos fora do lugar</option></select>
  <button type="submit">Resolver</button>
  <button type="button" id="shuffle">Embaralhar</button>
</form>
<div id="controls" class="row" style="display:none;">
  <button id="prev">Anterior</button>
  <button id="next">Próximo</button>
  <span id="stepinfo"></span>
</div>
<div id="board" class="board"></div>
</div>
<script>
function shuffleArray(arr) {
  for (let i = arr.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [arr[i], arr[j]] = [arr[j], arr[i]];
  }
  return arr;
}
function isSolvable(state, goal) {
  function inversions(arr) {
    arr = arr.filter(x => x !== 0);
    let inv = 0;
    for (let i = 0; i < arr.length; i++) {
      for (let j = i+1; j < arr.length; j++) {
        if (arr[i] > arr[j]) inv++;
      }
    }
    return inv;
  }
  return inversions(state) % 2 === inversions(goal) % 2;
}
document.getElementById('shuffle').onclick = function() {
  let arr = [1,2,3,4,5,6,7,8,0];
  let goal = document.getElementById('goal').value.split(',').map(Number);
  let tries = 0;
  let shuffled;
  do {
    shuffled = shuffleArray([...arr]);
    tries++;
  } while (!isSolvable(shuffled, goal) && tries < 1000);
  document.getElementById('start').value = shuffled.join(',');
}
let solution = [];
let step = 0;
function renderBoard(state, prevState = null) {
  const board = document.getElementById('board');
  board.innerHTML = '';
  let movingIdx = -1;
  if (prevState) {
    // Descobre qual peça se moveu
    for (let i = 0; i < 9; i++) {
      if (state[i] !== prevState[i] && state[i] !== 0 && prevState[i] !== 0) {
        movingIdx = i;
        break;
      }
    }
  }
  for (let i = 0; i < 9; i++) {
    const div = document.createElement('div');
    let classes = 'tile';
    if (state[i] === 0) classes += ' empty';
    if (i === movingIdx) classes += ' moving';
    div.className = classes;
    div.textContent = state[i] === 0 ? '' : state[i];
    board.appendChild(div);
  }
}
function updateStepInfo() {
  document.getElementById('stepinfo').textContent = 'Passo ' + (step+1) + ' de ' + solution.length;
}
document.getElementById('form').onsubmit = async function(e) {
  e.preventDefault();
  let start = document.getElementById('start').value;
  let goal = document.getElementById('goal').value;
  let heuristic = document.getElementById('heuristic').value;
  try {
    let res = await fetch('/solve', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({start, goal, heuristic})
    });
    let data = await res.json();
    if (data.path) {
      solution = data.path;
      step = 0;
      document.getElementById('controls').style.display = '';
      renderBoard(solution[step]);
      updateStepInfo();
    } else {
      solution = [];
      document.getElementById('controls').style.display = 'none';
      document.getElementById('board').innerHTML = '<b>Sem solução.</b>';
    }
  } catch (err) {
    document.getElementById('board').innerHTML = '<b>Erro na requisição!</b>';
  }
}
document.getElementById('next').onclick = function() {
  if (solution.length && step < solution.length-1) {
    let prev = solution[step];
    step++;
    renderBoard(solution[step], prev);
    updateStepInfo();
  }
}
document.getElementById('prev').onclick = function() {
  if (solution.length && step > 0) {
    let prev = solution[step];
    step--;
    renderBoard(solution[step], prev);
    updateStepInfo();
  }
}
</script>
</body>
</html>
'''

@app.route("/")
def index():
  return render_template_string(HTML)

@app.route("/solve", methods=["POST"])
def solve():
    data = request.get_json()
    print("/solve called with:", data)
    start = tuple(int(x) for x in data["start"].split(","))
    goal_ = tuple(int(x) for x in data["goal"].split(","))
    heuristic = data["heuristic"]
    path = a_star(start, goal_, heuristic)
    print("Solution path:", path)
    if path:
        return jsonify({"path": [list(p) for p in path]})
    else:
        return jsonify({"path": None})

if __name__ == "__main__":
    app.run(debug=True)
