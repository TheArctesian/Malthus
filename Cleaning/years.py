from coalas import csvReader as c

c.importCSV('population.csv')
c.addCol('NormalizedPop')
for i in range(len(c.Year)): 
    c.NormalizedPop.append(float(c.Population[i])-946764816)

c.writeCSV('population.csv')
