import math
from coalas import csvReader as c

c.importCSV('population.csv')
c.addCol('Year')
c.addCol('log')
c.addCol('pred')
for i in range(len(c.Pop)):
    print((math.log10(float(c.Pop[i]))))
    c.Year.append(i)
    c.log.append((math.log10(float(c.Pop[i]))))
    c.pred.append((i-1)*math.log10(2)+math.log10(126562371))
c.writeCSV('lin.csv')


