"""
set b 99
set c b
jnz a 2
jnz 1 5
mul b 100
sub b -100000
set c b
sub c -17000
set f 1
set d 2
set e 2
set g d
mul g e
sub g b
jnz g 2
set f 0
sub e -1
set g e
sub g b
jnz g -8
sub d -1
set g d
sub g b
jnz g -13
jnz f 2
sub h -1
set g b
sub g c
jnz g 2
jnz 1 3
sub b -17
jnz 1 -23
"""


"""
b = 99
c = b
jnz a [L1]
jnz 1 [L2]
[L1]:
mul b 100
sub b -100000
set c b
sub c -17000
[L2], [L8]: 
set f 1
set d 2
[L5]:
set e 2
[L4]:
set g d
mul g e
sub g b
jnz g [L3]
set f 0
[L3]:
sub e -1
set g e
sub g b
jnz g [L4]
sub d -1
set g d
sub g b
jnz g [L5]
jnz f [L6]
sub h -1
[L6]:
set g b
sub g c
jnz g [L7]
jnz 1 [END]
[L7]:
sub b -17
jnz 1 [L8]
"""


"""
b = (99 * 100) + 100000
c = b + 17000

[L8]: 
f = 1
d = 2

while g != 0:
    e = 2
    
    while g != 0:
        g = d
        g *=e
        g -= b
        if g == 0:
            f = 0
        e += 1
        g = e
        g -= b
    
    d += 1
    g = d
    g -= b

if f == 0:
    h += 1

g = b
g -= c
if g == 0:
    return h
b += 17
jnz 1 [L8]
"""

"""
b = (99 * 100) + 100000
c = b + 17000

while True:
    f = False
    d = 2
    
    while (d - b) != 0:
        e = 2
    
        while g != 0 and not f:
            g = d
            g *=e
            g -= b
            if g == 0:
                f = True
            e += 1
            g = e
            g -= b
    
        d += 1
    
    if f == True:
        h += 1
    if b == c:
        return h
    b += 17
"""

"""
b = 109900
c = 126900

while True:
    f = False
    d = 2

    while d != b:
        e = 2

        while e != b and not f:
            if (e*d) == b:
                f = True
            e += 1
            
        d += 1

    if f == True:
        h += 1
    if b == c:
        return h
    b += 17
"""

"""
b = 109900
c = 126900

while True:
    f = False
    d = 2

    while d != b and not f:      
        if b % d == 0:
            f = True
        d += 1

    if f == True:
        h += 1
    if b == c:
        return h
    b += 17
"""

"""
b = 109900
c = 126900
h = 0

for b in range(b, c + 1, 17):
    f = False
    d = 2

    while d != b and not f:      
        if b % d == 0:
            f = True
        d += 1

    h += 1 if f else 0

return h

"""

# this is fast enough...


def solve(program):

    b = 109900
    c = 126900
    h = 0

    for b in range(b, c + 1, 17):
        f = False
        d = 2

        while d != b and not f:
            if b % d == 0:
                f = True
            d += 1

        h += 1 if f else 0

    return h


def main():

    data = []
    with open('input') as in_f:
        for row in in_f:
            ins = row.strip().split()
            data.append(ins)

    solution = solve(data)

    print(solution)


if __name__ == "__main__":

    main()
