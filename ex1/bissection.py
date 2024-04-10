"""BISSECTION METHOD TO FIND ROOTS"""

import matplotlib.pyplot as plt

# example of x^2 - c function, where c is an integer
def f(x) -> float:
    return x ** 2 - 4

def eq_sign(a, b) -> bool:
    return (a > 0 and b > 0) or (a < 0 and b < 0)


def bissection(a0, b0):
    e = 10 ** -5
    c = 0

    i = 0
    values = []
    errors = []

    # abs(b0 - a0) is the error.
    while abs(b0 - a0) > e:
        errors.append(abs(b0-a0))

        c = (a0 + b0) / 2
        values.append(c)

        if f(c) == 0:
            break

        if eq_sign(f(a0), f(c)):
            a0 = c

        else:
            b0 = c

        i += 1
    
    plt.plot(range(0, i), values)
    plt.title(f'Plot calculated by bissection method as x approaches {c}')
    plt.show()

    # error:
    plt.plot(range(0, i), errors)
    plt.yscale('log')
    plt.title('Error by bissection method as x approaches')
    plt.show()

    return c


def main():
    values = {0: {'a0': 0.7, 'b0': 2.6}, 1: {'a0': 0.4, 'b0': 1.7}, 2: {'a0': -3, 'b0': 0.6}}

    for i in range(3):
        a0 = values[i]['a0']
        b0 = values[i]['b0']
        print(f'Root is: {bissection(a0, b0)}')


if __name__ == '__main__':
    main()
