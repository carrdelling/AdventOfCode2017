

def solve(data):

    distances = []
    for par in data:
        idx = par[0]

        pos = list(par[1])
        vel = list(par[2])
        acc = list(par[3])
        for tick in range(1000):

            vel = (vel[0] + acc[0], vel[1] + acc[1], vel[2] + acc[2])
            pos = (vel[0] + pos[0], vel[1] + pos[1], vel[2] + pos[2])

        dist = sum(abs(p) for p in pos)
        distances.append((dist, idx))

    distances.sort(key= lambda x: x[0])

    solution = distances[0][1]

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
