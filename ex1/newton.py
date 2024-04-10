import matplotlib.pyplot as plt
from math import log

def f(x):
    return x**2 - 4


def f_dx(x):
    return 2*x


def newton(x0, epsilon, max_iter):
    values = []
    errors = []
    for i in range(0, max_iter+1):
        err = abs(f(x0))
        errors.append(err)
        values.append(x0)

        if err < epsilon:
            return (x0, values, errors)
        
        if f_dx(x0) == 0:
            print("Zero derivative. Not found.")
            break

        
        x0 -= f(x0) / f_dx(x0)

    
    return (None, values, errors)


def main():
    x0 = 0.4

    results = newton(x0, 10**-5, 25)

    if results[0]:
        print(f'Found 0 ({results[0]}) in {results[1]} iterations.')
    else:
        print(f'It took me {results[1]} iterations, but I found nothing.')

    y_field = results[1]
    x_field = range(1, len(y_field) + 1)

    # plt.plot(x_field, y_field)
    # plt.title(f"x values as x approaches {results[0]}")
    # plt.show()


    # errors.
    errors = results[2]
    plt.title("Errors")
    plt.plot(x_field, errors)
    plt.yscale('log')
    plt.show()

if __name__ == '__main__':
    main()