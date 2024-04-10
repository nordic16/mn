import matplotlib.pyplot as plt
from math import log

def f(x):
    return x ** 2 - 4

def f_dx(x):
    return 2 * x


def secant(x0, x1, kmax):
    f_x0 = f(x0)
    f_x1 = f(x1)
    e = 10 ** -5
    d = f_x0 / f_dx(x0)
    errors = []

    x2 = 0

    k = 0
    while abs(d) > e:
        errors.append(abs(d))
        x2 = x1 - d
        x0 = x1
        x1 = x2
        f_x0 = f_x1
        f_x1 = f(x1)
        d = f_x1 * (x1-x0)/(f_x1 - f_x0)

        if k > kmax:
            print(f"REACHED MAX NUMBER OF ITERATIONS! {kmax}")
            print("Aborting...")
            
            return None

        k += 1

    return (x2, errors)


def main():
    # k: max_iter
    results = secant(1, 3, 50)

    print(f'Root is: {results[0]}')

    # errors
    errors = results[1]
    plt.plot(range(1, len(errors) + 1), errors)
    plt.yscale('log')
    plt.show()



if __name__ == '__main__':
    main()