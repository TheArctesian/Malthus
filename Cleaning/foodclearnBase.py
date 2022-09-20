from coalas import csvReader as c
def badprinter(years, fo): 
    with open("plotFood.csv", "w") as f:
        for i in range(len(years)): 
            Sfmt = ''
            Sfmt += str(years[i])
            Sfmt += ','
            Sfmt += str(fo[i])
            Sfmt += '\n'
            print(Sfmt)
            f.write(Sfmt)

c.importCSV('food-time.csv')

y = [] 
food = []

for i in range(len(c.Year)):
    y.append(int(c.Year[i])-1961)
    food.append(float(c.Food[i])-1.686099431333795e+16)


badprinter(y,food)
