from coalas import csvReader as c
import torch
import torch.nn.functional as F

c.importCSV('food.csv')


test_list1 = ([int(x) for x in c.Food])
test_list2 = ([int(x) for x in c.Predicted])

#a = torch.FloatTensor(EX)
#b = torch.FloatTensor(OBS)

print(len(set(test_list1) & set(test_list2)) / float(len(set(test_list1) | set(test_list2))) * 100)


