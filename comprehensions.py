from math import factorial, sqrt
from pprint import pprint as pp

fact_ = [len(str(factorial(item))) for item in range(21)]
# print(fact_)
# print(type(fact_))

new_set = {item for item in fact_ }

# print(new_set)

country_to_capital = {"kenya"   :"Nairobi",
                      "Tanzania":"Dodoma",
                      "Uganda"  :"Kampala",
                      "Rwanda" :"Kigali",
                      "Burundi":"Gitega"}

# print(country_to_capital.items())                      

for (country,capital) in country_to_capital.items():
    # print(capital,country)
    pass

capital_to_country = {capital:country for (country,capital) in country_to_capital.items()}

# pp(capital_to_country)

def is_prime(x):
    if x < 2:
        return False

    for i in range(2,int( sqrt(x) + 1 )):
        
        if x % i == 0:
            return False
    
    return True       

# pp(is_prime(100))

list_prime = [item for item in range(101) if is_prime(item)]

# print(list_prime)

def first(iterable):
    
    iterator = iter(iterable)
    
    try:
        return next(iterator)
    
    except StopIteration:
        raise ValueError("Iterable is empty")

# print (first(["first","second","third"]))

