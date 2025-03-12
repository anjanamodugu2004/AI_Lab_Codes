import random

ps = 100

genes = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890, .-;:_!\"#%&/()=?@${[]}"

target = "Ram"

def rand_gene():
    return random.choice(genes)

def gen_gnome():
    return [rand_gene() for _ in range(len(target))]

def calc_fit(ch):
    return sum(1 for g, t in zip(ch, target) if g != t)

def init_pop():
    return [[gen_gnome(), 0] for _ in range(ps)]

def select(p):
    return random.sample(p, 2)

def cross(p1, p2):
    return [g1 if (r := random.random()) < 0.45 else g2 if r < 0.9 else rand_gene()
            for g1, g2 in zip(p1[0], p2[0])]

def mutate(ch):
    return [rand_gene() if random.random() < 0.1 else g for g in ch]

def ga():
    gen, pop = 1, init_pop()

    for i in pop:
        i[1] = calc_fit(i[0])

    while True:
        pop.sort(key=lambda i: i[1])

        if pop[0][1] == 0:
            break

        new_gen = pop[:ps // 10] + [[cross(*select(pop)), 0] for _ in range(ps - ps // 10)]

        for i in new_gen:
            i[0] = mutate(i[0])
            i[1] = calc_fit(i[0])

        pop = new_gen

        print(f"Gen: {gen}\tString: {''.join(pop[0][0])}\tFitness: {pop[0][1]}")

        gen += 1

    print(f"Gen: {gen}\tString: {''.join(pop[0][0])}\tFitness: {pop[0][1]}")

ga()
