import _utilities


@_utilities.benchmark
def solve():
    return max(_utilities.prime_factorization(600851475143))


if __name__ == '__main__':
    solve()
