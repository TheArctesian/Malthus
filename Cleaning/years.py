from coalas import csvReader as c

c.importCSV('food-time.csv')

for i in range(len(c.Year)): 
    c.YearSince[i] = int(c.Year[i])-1960

c.writeCSV('food-time.csv')