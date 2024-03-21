import matplotlib.pyplot as plt
from math import log, sin

def square(end):
    list = [i ** 2 for i in range(end)]
    plt.plot(list)
    plt.show()

def operation(end, cb, start=0):
    list = [cb(i) for i in range(start, end)]

    plt.plot(list)
    plt.show()

def main():
    x = 10

    print(f'#####Squares#####')
    square(10)
    print('#####sin(x)#####')
    operation(10, sin)
    print('#####log(x)#####')
    operation(10, log, start=1)

if __name__ == '__main__':
    main()
