from collections import Counter


def solve(data):

    # get w
    weights = {parent: w for parent, w, childs in data if len(childs) < 1}
    orig_w = {parent: w for parent, w, childs in data}
    solution = None

    while solution is None:

        for parent, w, childs in data:

            if parent in weights:
                continue

            if all(c in weights for c in childs):
                uniweights = [weights[c] for c in childs]
                if len(set(uniweights)) == 1:
                    weights[parent] = w + sum(uniweights)
                else:
                    # we found the imbalance
                    counts = Counter(uniweights)
                    diff, same = sorted(counts.items(), key=lambda x: x[1])
                    change = same[0] - diff[0]

                    for c in childs:
                        if weights[c] == diff[0]:
                            real_w = orig_w[c]
                            solution = real_w + change

    return solution


def main():

    data = []
    with open('input') as in_f:
        for row in in_f:
            chunks = row.strip().split(' -> ')

            childs = chunks[1].split(', ') if len(chunks) > 1 else []
            parent, w = chunks[0][:-1].split(' (')
            w = int(w)

            data.append((parent, w, childs))

    solution = solve(data)

    print(solution)


if __name__ == "__main__":

    main()