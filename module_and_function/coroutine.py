
async def greeting(name):
    return 'Hello ' + name

async def hello():
    names = ['Guido', 'Dave', 'Paula']
    for name in names:
        print(await greeting(name))

if __name__ == '__main__':
    g = greeting('Guido')
    
    import asyncio
    loop = asyncio.get_event_loop()
    s = loop.run_until_complete(g)
    print(s)
    
    h = hello()
    loop.run_until_complete(h)
