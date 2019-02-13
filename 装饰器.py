

def check(func):
    def inner(*args,**kwargs):
        print("====")
        ret = func(*args,**kwargs)
        print("//////")
        return ret
    return inner


def aa():
    for i in range(1000):
        if i>900:
            print(i)




aa()

print("ooooo"+"pppp")