def calculate(*args):
    total = sum(args)
    lowest = min(args)
    decline = lowest / total
    return [arg*(1-decline) for arg in args]

#original_prices = (10.0, 20.0, 30.0)
original_prices = (25.69, 24.99, 26.99)

new_prices = calculate(*original_prices)


print "Original Prices", ["%0.2f" % i for i in original_prices]
print "Original Total Price %0.2f" % sum(original_prices)

print

print "Return Prices", ["%0.2f" % i for i in new_prices]
print "New Total Price %0.2f" % sum(new_prices)


