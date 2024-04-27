def to_z_order(x, y):
    value = 0
    n = len(x)
    for i in range(n):
        if x[i] == '1':
            value = (value << 1) | 1
        else:
            value = (value << 1) | 0
        if y[i] == '1':
            value = (value << 1) | 1
        else:
            value = (value << 1) | 0
    return value

def from_z_order(value, n):
    result = [0, 0]
    x, y = 0, 0
    for i in range(n):
        x |= (value & 1) << i
        value >>= 1
        y |= (value & 1) << i
        value >>= 1
    result[0] = x
    result[1] = y
    return result

def get_bits(value):
    bits = ""
    leading_zeros = True
    for i in range(31, -1, -1):
        if (value & (1 << i)) != 0:
            bits += "1"
            leading_zeros = False
        elif not leading_zeros:
            bits += "0"
    return bits if bits else "0"

def print_points(map):
    # Init grid to '.'
    grid = [['.' for _ in range(8)] for _ in range(8)]

    for z_order, binary in map.items():
        coordinates = from_z_order(z_order, 3)
        x, y = coordinates[0], coordinates[1]
        grid[7 - x][y] = 'o'

    for row in grid:
        print(" ".join(row))
    for z_order, binary in map.items():
        print(f"ZOrder: {binary}, Decimal: {z_order}")

def contains_value(map, value):
    return value in map.values()

# Considering 3-bit values
z_index = {}

# Adding points to the index
point1 = to_z_order("110", "010")  # (6,2)
z_index[point1] = get_bits(point1)

point2 = to_z_order("101", "001")  # (5,1)
z_index[point2] = get_bits(point2)

point3 = to_z_order("011", "111")  # (3,7)
z_index[point3] = get_bits(point3)

point4 = to_z_order("001", "100")  # (1,4)
z_index[point4] = get_bits(point4)

# int point5 = to_z_order("100", "111") # (1,4)
# z_index[point5] = get_bits(point5)

# Get all points stored
print_points(z_index)

# Search for points
point_to_search1 = int(input("\nEnter point to search: "))
print(contains_value(z_index, get_bits(point_to_search1)))

point_to_search2 = int(input("\nEnter point to search: "))
print(contains_value(z_index, get_bits(point_to_search2)))
