from time import sleep, time


def add(num1, num2):
    start = time()
    sleep(num1)
    sleep(num2)
    return int(time() - start)


def suj(n1, n2):
    return n1 + n2


print(f"{add(20, 1)} it is fast")

print(suj(20, 1))
