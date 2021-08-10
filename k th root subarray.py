import math


def main_():
    n, k, q = map(int, input().split())
    array = list(map(int, input().split()))
    for i in range(q):
        queries = list(map(int, input().split()))
        if queries[0] == 1:
            l, r = queries[1] - 1, queries[2]
            product = 1
            for j in range(l, r):
                product *= array[j]
            special_value = math.pow(product, 1 / k)
            if math.ceil(special_value) == math.floor(special_value):
                print("Yes")
            else:
                print("No")
        elif queries[0] == 2:
            l, r, x, y = queries[1] - 1, queries[2], queries[3], queries[4]
            for j in range(l, r):
                array[j] = array[j] * math.pow(x, y)
        elif queries[0] == 3:
            l, r, x = queries[1] - 1, queries[2], queries[3]
            for j in range(l, r):
                array[j] = x


main_()
