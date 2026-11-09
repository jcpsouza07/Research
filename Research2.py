import math
import statistics
from sympy import primerange

limit = int(input("Enter the prime range limit: "))
primes = list(primerange(1, limit+1))

x0s = []

mean = []
median = []
total_fails = []
deviation = []

for x0 in range(1,11):

    iterations = []
    fails = 0

    for p in primes:
        for q in primes:

            if p >= q:
                continue
            N = p * q

            x = [x0]
            i = 0
            j = 0
            factor = 1

            while factor == 1:

                if i == len(x) - 1:
                    x.append((x[i] ** 2 + 1) % N)

                    i = 0
                    j += 1
                else:

                    difference = abs (x[-1] - x[i])
                    factor = math.gcd(difference, N)

                    i += 1

                    if factor == N:
                        fails += 1
                        break
            if 1 < factor < N:
                iterations.append(j)
    if len(iterations) > 1:

        mean_value = sum(iterations) / len(iterations)
        median_value = statistics.median(iterations)
        deviation_value = statistics.stdev(iterations)

        x0s.append(x0)
        mean.append(mean_value)
        median.append(median_value)
        total_fails.append(fails)
        deviation.append(deviation_value)

        print(f"\nx0 = {x0}")
        print(f"mean = {mean_value:.3f}")
        print(f"median = {median_value:.3f}")
        print(f"number of fails = {fails:}")
        print(f"standard deviation = {deviation_value:.3f}")
        print(f"number of iterations = {sum(iterations)}")