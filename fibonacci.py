from functools import lru_cache

def fib(n, mem = None):
    if mem == None:
        mem = {}

    if n <=2:
        return 1
    elif n in mem:
        return mem[n]
    else:
        mem[n] = fib(n-1, mem) + fib(n-2, mem)
        return mem[n]

def fib_b(n, mem = None):
    if mem == None:
        mem = {1:1,2:1}

    if n in mem:
        return mem[n]
    else:
        mem[n] = fib(n-1, mem) + fib(n-2, mem)
        return mem[n]

def iter_fib(n):
    a,b = 1,1
    for i in range(n):
        a,b = b, a+b

    return b

def fib_gen(n):
    yield 0
    if n > 0: yield 1 # special case
    last: int = 0 # initially set to fib(0)
    next: int = 1 # initially set to fib(1)
    for _ in range(1, n):
        last, next = next, last + next
        yield next # main generation step




print(fib(5))
print(fib_b(5))
print(iter_fib(3))

print(fib(10))
print(fib_b(10))

for i in fib_gen(10):
    print(i)