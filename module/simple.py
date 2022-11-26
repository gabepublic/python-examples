
# global var
x = 88

def spam():
    print("x is ", x)

def run():
    print("fn: run...")
    spam()

if __name__ == '__main__':
    print("running simple.py...")
    run()