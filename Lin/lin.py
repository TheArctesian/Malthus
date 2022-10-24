import math
from coalas import csvReader as c

c.importCSV('population.csv')
c.printHeaders()

Pop = c.Population

print(Pop)

## for i in range(len(Pop)):
##     temp = (float(c.Y25[i])-1)+math.log(126562371)
##     print(temp)
## 
## for i in range(len(Pop)):
##     print(c.Y25[i])
## 
## for i in range(len(Pop)):
##     print(math.log(float(Pop[i])),2)
## 
# That was stupid 


for i in range(len(Pop)):
