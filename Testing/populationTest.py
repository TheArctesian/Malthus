from coalas import csvReader as c
import torch
import torch.nn.functional as F

c.importCSV('pop.csv')

c.printSmall()

test_list1 = ([float(x) for x in c.Predicted])
test_list2 = ([float(x) for x in c.NormalizedPop])

#a = torch.FloatTensor(EX)
#b = torch.FloatTensor(OBS)

print(len(set(test_list1) & set(test_list2)) / float(len(set(test_list1) | set(test_list2))) * 100)

