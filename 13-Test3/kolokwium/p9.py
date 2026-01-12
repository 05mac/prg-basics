def f(uid):
    # kazdy wyraz musi byc inny
    return list(dict.fromkeys(uid)) == uid

if __name__ == "__main__":
    print(f(["john5","ann123","JOHN5","xxx","abc333","a10"]))
    print(f(["abc123","ann","abc123","a10"]))    
