from utils_backtracking import *

dict_in = {
  "a":"in/a_example.in",
  "b":"in/b_small.in",
  "c":"in/c_medium.in",
  "d":"in/d_quite_big.in",
  "e":"in/e_also_big.in",
}

#Run A
k = "a"
m, n, parts = open_in(dict_in, k)
state = [0, []]
backtrack_full(m, n, parts, state, 16)
write_solution(state, k)

#Run B
k = "b"
m, n, parts = open_in(dict_in, k)
state = [0, []]
backtrack_full(m, n, parts, state, 100)
write_solution(state, k)

#Run C
k = "c"
m, n, parts = open_in(dict_in, k)
state = [0, []]
#backtrack_heuristic(m, n, parts, state, 0.99, 4482)
backtrack_heuristic(m, n, parts, state, 0.99, 4481)
print(state[0])
write_solution(state, k)

#Run D
k = "d"
m, n, parts = open_in(dict_in, k)
state = [0, []]
backtrack_heuristic(m, n, parts, state, 0.7, -1)
print(state[0])
write_solution(state, k)