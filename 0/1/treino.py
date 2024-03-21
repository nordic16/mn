import matplotlib.pyplot as plt

def main():
    print('#' * 20, 'EX1.1', '#' * 20)
    plot_abs_error(10, 20)
    print('#' * 46)
    
    print('#' * 20, 'EX1.1', '#' * 20)
    plot_abs_error(2, 60)
    print('#' * 46)
    
        
def plot_abs_error(x, max):
    h = [x ** -i for i in range(0,  max+1)]
    err = [(abs_error(func, func_dx, x, h[i])) for i in range(0, max+1)]

    plt.plot(h, err)

    plt.yscale('log')
    plt.ylabel('Absolute error')
    plt.xscale('log')
    plt.xlabel('h value')

    plt.show()

    [print(i) for i in err]



def func(x: float) -> float:
    return x ** 2

def func_dx(x: float) -> float:
    return 2 * x

def abs_error(func, func_derivative, x, h) -> float:
    return abs(func_derivative(x) - (func(x + h) - func(x))/h)

if __name__ == '__main__':
    main() 


