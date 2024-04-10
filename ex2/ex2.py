import matplotlib.pyplot as plt
import math
import numpy


def f(t):
    return 9 * numpy.exp(-t) * math.sin(2 * math.pi * t) - 1.5 * 10**-3


def f_dx(t):
    return 18 * math.pi * numpy.exp(-t) * math.cos(2 * math.pi * t) - 9 * numpy.exp(-t) * math.sin(2 * math.pi * t)


def newton(x0, epsilon, max_iter):
    vals = []
    for i in range(0, max_iter+1):
        err = abs(f(x0))
        vals.append(x0)

        if err < epsilon:
            return (x0, vals)
        
        if f_dx(x0) == 0:
            print("Zero derivative. Not found.")
            break

        
        x0 -= f(x0) / f_dx(x0)

    
    return (None, vals)



def main():
    values = [0.6, 0.7, 0.75, 0.8, 0.9]
    for i in values:
        results = newton(i, 10**-6, 50)
        print(results[0])


if __name__ == '__main__':
    main()