'''
y=126562371*2^(x-1)
'''
from coalas import csvReader as c


def model(i):
    return 126562371*2**(i-1)


c.importCSV('pop.csv')
c.printHeaders()


c.addCol('Predicted')

for i in c.Year:
    c.Predicted.append(model(float(i)))

c.writeCSV('pop.csv')
