import matplotlib.pyplot as plt

def f(x):
    return x**2 - 4


def f_dx(x):
    return 2*x


def newton(x0, epsilon, max_iter):
    values = []
    for i in range(0, max_iter+1):
        val = abs(f(x0))
        values.append(val)


        if val < epsilon:
            return (x0, i, values)
        
        elif f_dx(x0) == 0:
            print("Zero derivative. Not found.")
            break

        else:
            x0 -= f(x0)/f_dx(x0)

    
    return (None, i, values)


def main():
    x0 = 0.4

    results = newton(0.4, 0.000000001, 25)

    if results[0]:
        print(f'Found 0 ({results[0]}) in {results[1]} iterations.')
    else:
        print(f'It took me {results[1]} iterations, but I found nothing.')

    y_field = results[2]
    x_field = range(1, len(y_field) + 1)

    plt.plot(x_field, y_field)
    plt.yscale('log')
    plt.show()

if __name__ == '__main__':
    main()