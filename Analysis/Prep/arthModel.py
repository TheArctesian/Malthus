'''
y=1.6860994313337951016(x-1)*0.04
'''
from coalas import csvReader as c


def model(i):
    return 1.686099431333795*10**(16)*(i-1)*0.04


c.importCSV('food.csv')
c.printHeaders()


c.addCol('Predicted')

for i in c.Year:
    c.Predicted.append(model(int(i)))

c.writeCSV('food.csv')

