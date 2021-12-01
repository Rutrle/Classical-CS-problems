def square_gen(num):
    while True:
        num = num+1
        yield num**2

def string_gen():
    yield 'asdasd'
    yield 'sadasd'
    yield 'asdssssssasd'
    yield 'asdafffsd'
    yield 'oooo'
    yield 'lll'
    yield 'jj'
    yield 'h'
    yield 'ende'





sq = square_gen(5)

print(next(sq))
print(next(sq))
print(next(sq))
print(next(sq))
st = string_gen()
print(next(st))
print(next(st))
print(next(st))
print(next(st))
print(next(st))
print(next(st))


