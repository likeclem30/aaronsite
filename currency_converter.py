def converter_to_dollar(rate,euro):
    dollar = rate * euro
    return dollar
r = float(input("Enter rate :"))
euro = float(input("Enter euro amount :"))

print(converter_to_dollar(r,euro))