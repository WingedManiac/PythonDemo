from datetime import  datetime
birth_year = input("Enter your birth year: ")
age = datetime.today().year - int(birth_year)
print(age)