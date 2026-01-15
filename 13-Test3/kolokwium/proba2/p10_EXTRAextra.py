def f(a,b):
    def f2(x):
        return f"y = {a * x + b}"
    return f2

if __name__ == "__main__":
    line = f(2,3)
    print(line(5))
