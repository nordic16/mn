"""BISSECTION METHOD TO FIND ROOTS"""

from math import sqrt
import matplotlib.pyplot as plt

# example of x^2 - c function, where c is an integer
def f(x):
    return x ** 2 - 4

def eq_sign(a, b):
    return (a > 0 and b > 0) or (a < 0 and b < 0)


def bissection(a0, b0):
    e = 10 ** -5
    c = 0

    i = 0
    values = []

    while (abs(b0 - a0) > e):
        c = (a0 + b0) / 2
        values.append(c)

        if f(c) == 0:
            break

        elif eq_sign(f(a0), f(c)):
            a0 = c

        else:
            b0 = c
        

        i += 1
    
    plt.plot(range(0, i), values)
    plt.show()
    return c

def main():
    values = {'elem1': {'a0': 0.7, 'b0': 2.6}, 'elem2': {'a0': 0.4, 'b0': 1.7}, 'elem3': {'a0': -3, 'b0': 0.6}}

    for i in range(1, 4):
        a0 = values[f'elem{i}']['a0']
        b0 = values[f'elem{i}']['b0']
        print(f'Root is: {bissection(a0, b0)}')
            

if __name__ == '__main__':
    main()









