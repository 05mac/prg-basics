def f(fnc,prods):
    filtered = list(map(fnc,prods))
    return filtered
    
if __name__ == "__main__":
    prods = ["water","cheese","tomato"]  
    fnc1 = lambda x: "id:"+ x[:2]  
    print(f(fnc1,prods)) 

    fnc2 = lambda x: (x[0]+x[-1]).upper()  
    f(fnc2,prods)
    print(f(fnc2,prods))