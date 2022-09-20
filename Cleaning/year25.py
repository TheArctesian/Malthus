from coalas import csvReader as c
c.importCSV('population.csv')
c.addCol('Y25')
for i in c.Year: 
    c.Y25.append((int(i)-1800)/25)
c.writeCSV('population.csv')