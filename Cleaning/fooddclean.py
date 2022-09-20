from coalas import csvReader as c 

c.importCSV('plotFood.csv')
c.printHeaders()
# c.addCol('D')

# for i in range(len(c.Food)):
#     c.D.append(float(c.Food[i])/float(c.Food[i-1]))

# c.writeCSV('plotFood.csv')
print(c.D)