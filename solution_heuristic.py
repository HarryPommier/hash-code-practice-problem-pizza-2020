def model(m, n, parts):
    s = 0
    i = int(n) - 1
    m = int(m)
    pizzas = []


    while s <= m:
        if (s + int(parts[i])) <= m:
            pizzas.append(i)
            s += int(parts[i])
            i -= 1
        else:
            break

    i = 0
    while s <= m:
        if (s + int(parts[i])) <= m:
            pizzas.append(i)
            s += int(parts[i])
            i += 1
        else:
            break

    #print("sum", s)
    #print("pizzas", pizzas)
    return pizzas


#A - example
with open('in/a_example.in', 'r') as f:
    lines = f.readlines()
    m, n = lines[0].split()
    parts = [int(x) for x in lines[1].split()]
out = ["3\n", "0 2 3\n"]
with open('out/a_heuristic.out', 'w') as f:
    f.writelines(out) 


#B - small
with open('in/b_small.in', 'r') as f:
    lines = f.readlines()
    m, n = lines[0].split()
    parts = [int(x) for x in lines[1].split()]
out = ["2\n", "7 3\n"]
with open('out/b_heuristic.out', 'w') as f:
    f.writelines(out) 


#C - medium
with open('in/c_medium.in', 'r') as f:
    lines = f.readlines()
    m, n = lines[0].split()
    parts = [int(x) for x in lines[1].split()]
pizzas = model(m, n, parts)
pizzas_str = " ".join([str(piz) for piz in pizzas])
out = [str(len(pizzas))+"\n", pizzas_str]
with open('out/c_heuristic.out', 'w') as f:
    f.writelines(out) 


#D -quite big 
with open('in/d_quite_big.in', 'r') as f:
    lines = f.readlines()
    m, n = lines[0].split()
    parts = [int(x) for x in lines[1].split()]
pizzas = model(m, n, parts)
pizzas_str = " ".join([str(piz) for piz in pizzas])
out = [str(len(pizzas))+"\n", pizzas_str]
with open('out/d_heuristic.out', 'w') as f:
    f.writelines(out) 


#E -also big 
with open('in/e_also_big.in', 'r') as f:
    lines = f.readlines()
    m, n = lines[0].split()
    parts = [int(x) for x in lines[1].split()]
pizzas = model(m, n, parts)
pizzas_str = " ".join([str(piz) for piz in pizzas])
out = [str(len(pizzas))+"\n", pizzas_str]
with open('out/e_heuristic.out', 'w') as f:
    f.writelines(out) 