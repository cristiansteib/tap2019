H, W = map(int, input().split())
matriz = []

for _ in range(H):
    inp = input().replace('*', '1')
    inp = inp.replace('.', '0')
    matriz.append(inp)


def potential_centers(r):
    row = (int(matriz[r], 2))
    centers = []
    for i in range(0, W):

        if (row & (0b111 << i)) == 0b111 << i:
            centers.append(i + 1)
    return centers


def get_long_croix(r, center):
    return 0


def validate_croix_bottom_boundaries(r, center, long):
    return True


def count_croixs_in_row(r, centers):
    counter = 0
    for center in centers:
        long = get_long_croix(r, center)
        if long:
            if validate_croix_bottom_boundaries(r, center, long):
                counter += 1
    return counter


# se puede acotar de w+1 a w-1
counter = 0
for r in range(1, H):
    centers = potential_centers(r)
    if centers:
        counter += count_croixs_in_row(r, centers)

print(counter)
