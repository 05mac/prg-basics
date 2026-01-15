def f(uid):
    unique_id = len(set(uid))
    
    return len(uid) == unique_id
#
if __name__ == "__main__":
    print(f(["john5","ann123","JOHN5","xxx","abc333","a10"]))
    print(f(["abc123","ann","abc123","a10"]))