import sys

def factorize(number):
    for i in range(2, number):
        if number % i == 0:
            return i, number // i
    return None

def factorize_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            number = int(line.strip())
            factors = factorize(number)
            if factors:
                p, q = factors
                print(f'{number}={p}*{q}')

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: factors <file>')
        sys.exit(1)

    file_path = sys.argv[1]
    factorize_file(file_path)
