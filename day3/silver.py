

def solve(data):

    # square
    x = 1
    while x ** 2 <= data:
        x += 2

    l_left = (x ** 2) - x + 1
    u_left = l_left - x + 1
    u_right = u_left - x + 1
    l_right = u_right - x - 1

    if l_left <= data <= x ** 2:
        i = (x - 1) // 2
        delta_y = data - l_left
        size = (x - 1) // 2
        j = abs(delta_y - size)
    elif u_left <= data <= l_left:
        j = (x - 1) // 2
        delta_x = data - u_left
        size = (x - 1) // 2
        i = abs(delta_x - size)
    elif u_right <= data <= u_left:
        i = (x - 1) // 2
        delta_y = data - u_right
        size = (x - 1) // 2
        j = abs(delta_y - size)
    elif l_right <= data <= u_right:
        j = (x - 1) // 2
        delta_x = data - l_right
        size = (x - 1) // 2
        i = abs(delta_x - size)
    else:
        assert False

    return i + j


def main():

    with open('input') as in_f:
        data = int(in_f.readline().strip())

    solution = solve(data)

    print(solution)


if __name__ == "__main__":

    main()
