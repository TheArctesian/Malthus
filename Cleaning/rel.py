from coalas import csvReader as c 

c.importCSV('food-time.csv')
c.addCol('Dif')

for i in range(len(c.Food)): 
    c.Dif.append(float(c.Food[i]) - float(c.Food[i-1]))
    c.YearSince.append(int(c.Year[i])-1961)
c.writeCSV('food-time.csv')
