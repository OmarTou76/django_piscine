def print_numbers():
    with open('numbers.txt', 'r') as f:
        content = f.read().strip()
        numbers = content.split(',')
        for number in numbers:
            print(number.strip())

if __name__ == '__main__':
    print_numbers()