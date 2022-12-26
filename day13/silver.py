
def solve(data):

    end = max(data) + 1
    scanners = {ly: 0 for ly in data}
    direction = {ly: True for ly in data}

    severity = 0
    for pos in range(end):
        scan = scanners.get(pos, -1)
        if scan == 0:
            severity += (pos * data[pos])

        for ly in scanners:
            if direction[ly]:
                scanners[ly] = scanners[ly] + 1
                if scanners[ly] == (data[ly] - 1):
                    direction[ly] = False
            else:
                scanners[ly] = scanners[ly] - 1
                if scanners[ly] == 0:
                    direction[ly] = True

    return severity


def main():

    layers = {}
    with open('input') as in_f:
        for row in in_f:
            layer, dist = row.strip().split(': ')
            layers[int(layer)] = int(dist)

    solution = solve(layers)

    print(solution)


if __name__ == "__main__":

    main()
