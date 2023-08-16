import numpy as np 

lista1 = [1,2,3,4,5,6]
lista2 = [7,8,9,10,11,12]

ar1 = np.array(lista1)
ar2 = np.array(lista2)

ar3 = ar1 + ar2
print(ar3)

ar3 = ar3.reshape(2,3)
print(ar3)

ar3 = ar3.astype(np.float32)
print(ar3)

ar3 = np.transpose(ar3)
print(ar3)

