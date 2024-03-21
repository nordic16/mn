def print_arr(arr):
    for i in range(0, len(arr), 2):
        print(arr[i])

def sep(len):
    print ('#' * len)

def avg(arr):
    sum = 0

    for i in arr:
        sum += i

    return sum / len(arr)

def variance(arr):
    average = avg(arr)
    val = 0

    for i in arr:
        val += (i - average) ** 2

    return val / (len(arr) - 1)

def main():
    arr = [10.5, 9.3, 11.4, 10.9, 13.0, 8.4, 9.2, 8.9, 10.3, 11.2, 12.1, 8.4, 9.2, 9.9, 10.1]

    print_arr(arr)
    arr.append(-1)
    arr.append(3)
    arr.append(5)
    arr.remove(5)

    sep(15)
    print_arr(arr)
    sep(15)

    arr.pop()
    arr.pop()
    print(f'Average: {avg(arr)}')
    print(f'Variance: {variance(arr)}')
    print(f'Sigma: {variance(arr) ** 0.5}')

if __name__ == '__main__':
    main()