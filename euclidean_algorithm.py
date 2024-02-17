def euclidean_algorithm(a, b):
    if a > b:
        return euclidean_algorithm(a - b, b)
    elif a < b:
        return euclidean_algorithm(a, b - a)
    else:
        return a


if __name__ == "__main__":
    f1 = 938
    f2 = 124
    print("mcd between {} and {} = {}".format(f1, f2, euclidean_algorithm(f1, f2)))
