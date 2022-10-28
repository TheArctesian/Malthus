import math
from coalas import csvReader as c

c.importCSV('population.csv')
c.addCol('log')
#for i in range(len(Pop)):
#    temp = (math.log(126562371.0)+(i-1)*math.log(t)
#    print(temp)
for i in range(len(c.Pop)):
    # c.log.append(math.log(4184537.2)-(math.log(float(c.Pop[i]))/(i-1)-math.log(2)))
    print((math.log(float(c.Pop[i]))-10))
    c.log.append((math.log(float(c.Pop[i]))-10))

c.writeCSV('lin.csv')

