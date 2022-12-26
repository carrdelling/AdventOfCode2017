

def solve(data):

    full_available = set()
    for a, b in data:
        full_available.add((a, b))
        full_available.add((b, a))

    best_strength = 0
    states = []

    for x, y in full_available:
        if x == 0:
            chain = (x, y)
            available = full_available - {(x, y), (y, x)}
            states.append((chain, available))

    while states:

        current = states.pop()
        chain, available = current

        target = chain[-1]

        options = {(x, y) for x, y in available if x == target}

        if not options:
            strength = sum(2*v for v in chain) - chain[0] - chain[-1]

            if strength > best_strength:
                best_strength = max(best_strength, strength)
                print(chain, strength, best_strength)

        for option in options:
            new_chain = tuple(list(chain) + [option[-1]])
            new_available = available - {option, (option[1], option[0])}

            states.append((new_chain, new_available))

    solution = best_strength

    return solution


def main():
    
    data = []
    with open('input') as in_f:
        for row in in_f:
            piece = list(map(int, row.strip().split('/')))
            piece = (min(piece), max(piece))
            data.append(piece)

    solution = solve(data)

    print(solution)


if __name__ == "__main__":

    main()
