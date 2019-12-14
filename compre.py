#squares = []
#for i in range(10):
 #   squares.append(i * i)

squares = [i * i for i in range(10)]


taxes = [1.09, 23.56, 57.84, 4.56, 6.78]
TR = .08
def get_price_tax(txn):
    return txn * (1 + TR)
final_prices = map(get_price_tax, taxes)
list(final_prices)


txns = [2.09, 33.56, 57.84, 7.56, 9.78]
TR = .08
def get_price_tax(txn):
    return txn * (1 + TR)
final_prices1 = [get_price_tax(i) for i in txns]
list(final_prices1)
    
vowels = []
sentence = "the rocket came back from mars"
for i in range(len(sentence)):
    if sentence[i] in 'aeiou':
        print(sentence[i])


        

