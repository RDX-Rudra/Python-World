letter ="Hey my name is {} and I am from {}"
country = "India"
name = "Rudra"
print(letter.format(name, country))
print(letter.format("das", country))
print(f"Hey my name is {name} and I am from {country}")
print(f"Hey my name is {{name}} and I am from {{country}}")
price = 54.7896
txt= f"For only {price:.2f} dollars!"
print(txt)
print(type(f"{2*30}"))