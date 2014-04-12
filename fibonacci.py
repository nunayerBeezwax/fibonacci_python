fibonacci = [0, 1]

def fib(x, y):
    z = x + y
    fibonacci.append(z)

number = int(input('Input a number to see its equivalent in the fibonacci sequence: '))
i = 0

while i < number:
    fib(fibonacci[-2], fibonacci[-1])
    i += 1

print fibonacci[-3]
