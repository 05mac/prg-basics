def f(value1):
    def f2(value2):
    
        return value1 * value2

if __name__ == "__main__":
   times_five = f(5)
   print(times_five(8))
