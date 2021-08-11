import datetime

def log(func):

    def inner(*args,**kwargs):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        res = func(*args,**kwargs)
        print(f"[{timestamp}] ({func.__name__}) {args} -> {res}")
        return res
    return inner()

@log
def test(a,b):
    print(a+b)

test(1,2)