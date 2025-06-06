import random

def tournament_selection(pop, fitnesses, k=3):
    selected = []
    for _ in range(len(pop)):
        contenders = random.sample(list(zip(pop, fitnesses)), k)
        winner = max(contenders, key=lambda x: x[1])
        selected.append(winner[0])
    return selected

def order_crossover(p1, p2):
    size = len(p1)
    a, b = sorted(random.sample(range(size), 2))
    child = [None] * size
    child[a:b] = p1[a:b]
    pos = b
    for g in p2[b:] + p2[:b]:
        if g not in child:
            if pos >= size:
                pos = 0
            child[pos] = g
            pos += 1
    return child

def swap_mutation(ind):
    i, j = random.sample(range(len(ind)), 2)
    ind[i], ind[j] = ind[j], ind[i]
    return ind

def local_search(ind, simulate_fn):
    """尝试交换两个基因，若更优则接受"""
    i, j = random.sample(range(len(ind)), 2)
    new_ind = ind[:]
    new_ind[i], new_ind[j] = new_ind[j], new_ind[i]
    return new_ind if simulate_fn(new_ind) > simulate_fn(ind) else ind

def ga_semi_improved(simulate_fn, N, pop_size=30, generations=50, mutation_rate=0.2, cx_prob=0.9,
                     elite_ratio=0.1, immigrant_ratio=0.1):
    population = [random.sample(range(N), N) for _ in range(pop_size)]
    elite_count = max(1, int(pop_size * elite_ratio))
    immigrant_count = max(1, int(pop_size * immigrant_ratio))

    best_ind = None
    best_fit = float('-inf')
    history = []

    for gen in range(generations):
        fitnesses = [simulate_fn(ind) for ind in population]
        gen_best_idx = max(range(len(fitnesses)), key=lambda i: fitnesses[i])
        gen_best_fit = fitnesses[gen_best_idx]
        history.append(gen_best_fit)

        if gen_best_fit > best_fit:
            best_fit = gen_best_fit
            best_ind = population[gen_best_idx][:]

        # 局部搜索
        best_ind = local_search(best_ind, simulate_fn)

        # 精英保留
        elites = [x for _, x in sorted(zip(fitnesses, population), reverse=True)][:elite_count]

        # 选择、交叉、变异
        parents = tournament_selection(population, fitnesses)
        offspring = []
        while len(offspring) < pop_size - elite_count - immigrant_count:
            p1, p2 = random.sample(parents, 2)
            child = order_crossover(p1, p2) if random.random() < cx_prob else p1[:]
            if random.random() < mutation_rate:
                child = swap_mutation(child)
            offspring.append(child)

        # 引入移民（新个体）
        immigrants = [random.sample(range(N), N) for _ in range(immigrant_count)]

        # 生成下一代
        population = elites + offspring + immigrants

    return best_ind, best_fit, history
