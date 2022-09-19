from coalas import csvReader as c
c.importCSV('food-time.csv')
c.addCol('Y25')
for i in c.Year: 
    c.Y25.append(((int(i)-1961)/25)+1)
c.writeCSV('food-time.csv')