availability ='In stock (22 available)'
price_new = int(availability.split()[2].replace('(', ''))
print(price_new)



bien = "Â£33.34"
availible_new = float(bien.split('£')[1])
print(availible_new)