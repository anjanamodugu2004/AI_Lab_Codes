import random

cap = 50

w = [10, 20, 30, 40, 50]
v = [60, 100, 120, 150, 200]

ps = 50
gen = 100
mr = 0.1

def gen_ch():
    return [random.choice([0, 1]) for _ in range(len(w))]

def init_pop():
    return [gen_ch() for _ in range(ps)]

def fit(ch):
    tw = sum(ci * wi for ci, wi in zip(ch, w))
    tv = sum(ci * vi for ci, vi in zip(ch, v))
    return tv if tw <= cap else 0

def select(pop):
    scores = [fit(ch) for ch in pop]
    return [random.choices(pop, weights=scores, k=1)[0] for _ in range(ps)]

def cross(p1, p2):
    pt = random.randint(1, len(p1) - 1)
    return p1[:pt] + p2[pt:], p2[:pt] + p1[pt:]

def mutate(ch):
    pt = random.randint(0, len(ch) - 1)
    ch[pt] = 1 - ch[pt]

def apply_mut(pop):
    for ch in pop:
        if random.random() < mr:
            mutate(ch)

def ga():
    pop = init_pop()

    for _ in range(gen):
        parents = select(pop)
        off = []

        for i in range(0, len(parents), 2):
            if i + 1 < len(parents):
                c1, c2 = cross(parents[i], parents[i + 1])
                off.extend([c1, c2])

        apply_mut(off)
        pop = off

    best = max(pop, key=fit)
    return best, fit(best)

sol, max_v = ga()

print("Best Sol:", sol)
print("Max Value:", max_v)
