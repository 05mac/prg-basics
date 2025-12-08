# # takes two numbers from keyboard
# n1 = int(input("Podaj pierwszą liczbę: "))
# n2 = int(input("Podaj drugą liczbę: "))

# # define an anonymous function
# mean = lambda x,y: (x+y)/2


# # calculates arightmtic mean and print result
# result = mean(n1,n2)
# print(f"The arithmetic mean of {result}")



# # 3 - Data Mapping - 1
# transactions_in_eur = [15.90,38.47,4.07,132.70,9.15]
# transactions_in_pln = list(map(lambda x:x*4.5, transactions_in_eur))
# print(transactions_in_pln)



#3.2

# sentence = 'I completely agree with you'
# result = list(map(lambda x: len(x) , sentence.split(" ")))
# print(result)

#3.3

stock = [(20,5.50),(15,8.30),(37,3.85),(4,11.60)]

result = list(map(lambda x: (x) ))
print(result)