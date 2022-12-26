from collections import defaultdict


def solve(data):

    velocity = {par[0]: par[2] for par in data}
    acceleration = {par[0]: par[3] for par in data}
    position = {par[0]: par[1] for par in data}
    alive = {p for p in position}

    for tick in range(1000):
        # move particles
        for pid in alive:
            vel = (velocity[pid][0] + acceleration[pid][0],
                   velocity[pid][1] + acceleration[pid][1],
                   velocity[pid][2] + acceleration[pid][2])
            velocity[pid] = vel

            pos = (velocity[pid][0] + position[pid][0],
                   velocity[pid][1] + position[pid][1],
                   velocity[pid][2] + position[pid][2])
            position[pid] = pos

        # collision check
        space = defaultdict(list)

        for idx, pos in position.items():
            space[pos].append(idx)

        alive = set()
        for pos, particles in space.items():
            if len(particles) == 1:
                alive.add(particles[0])

    solution = len(alive)

    return solution


def main():

    data = []
    with open('input') as in_f:
        for idx, row in enumerate(in_f):
            p, v, a = row.strip().split(', ')
            p = tuple(map(int, p.split('<')[-1].split('>')[0].split(',')))
            v = tuple(map(int, v.split('<')[-1].split('>')[0].split(',')))
            a = tuple(map(int, a.split('<')[-1].split('>')[0].split(',')))

            particle = (idx, p, v, a)
            data.append(particle)

    solution = solve(data)

    print(solution)


if __name__ == "__main__":

    main()
