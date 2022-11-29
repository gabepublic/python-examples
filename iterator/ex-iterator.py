
# Generator
def countdown(n):
    print('counting from: ', n)
    while n > 0:
        yield n      # emit a values
        print('countdown n: ', n)
        n -= 1
    print('done')


if __name__ == '__main__':

    # use the countdown with iterator
    for x in countdown(5):
        print(x)

    # equivalent under the cover
    c = countdown(5)        # NOTE: c is usable once only
    it = c.__iter__()
    print('it: ', it.__next__())
    print('it: ', it.__next__())
    print('----------------------')

    squares = [x*x for x in [1,2,3,4,5,]]
    print(squares)
    for y in squares:
        print(y)