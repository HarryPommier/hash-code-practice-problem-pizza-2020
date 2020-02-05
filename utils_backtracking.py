def open_in(dict_in, k):
  with open(dict_in[k], 'r') as f:
      lines = f.readlines()
      m, n = lines[0].split()
      parts = [int(x) for x in lines[1].split()]

  print("There are max {} slices and {} pizzas.".format(m, n))
  #print("Parts: \n", parts)
  return int(m), int(n), parts


def backtrack_full(m, n, parts, state, target):

  #print(state)

  if state[0] == target:
    return True
  
  for i in reversed(range(len(parts))):
    if i in state[1]:
      continue

    state[0] += parts[i]
    state[1].append(i)

    if backtrack_full(m, n, parts, state, target):
      return True
    else:
      k = state[1].pop(-1)
      state[0] -= parts[k]

  return False

def backtrack_heuristic(m, n, parts, state, alpha, my_max):

  #print(state)

  if (state[0] <= m and state[0] >= alpha*m) and state[0] >= my_max:
    return True
  
  for i in reversed(range(len(parts))):
    if i in state[1]:
      continue

    state[0] += parts[i]
    state[1].append(i)

    if backtrack_heuristic(m, n, parts, state, alpha, my_max):
      return True
    else:
      k = state[1].pop(-1)
      state[0] -= parts[k]

  return False


def write_solution(state, k):
  pizzas_str = " ".join([str(piz) for piz in state[1]])
  out = [str(len(state[1]))+"\n", pizzas_str]
  print(out)
  with open('out/{}_backtracking.out'.format(k), 'w') as f:
      f.writelines(out) 

  return True