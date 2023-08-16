import numpy as np 
import numpy.random as npr

lista1 = [1,2,3,4,5,6]
lista2 = [7,8,9,10,11,12]

ar1 = np.array(lista1)
ar2 = np.array(lista2)

ar3 = ar1 + ar2
print(ar3)

ar3r = ar3.reshape(2,3)
print(ar3r)

ar3 = ar3.astype(np.float32)
print(ar3)

ar3t = np.transpose(ar3r)
print(ar3t)

ar4 = np.array([[13,14,15,16,17,18],[19,20,21,22,23,24]])
print(ar4)

ar4 = np.multiply(ar3,ar4)
print(ar4)

ar5 = np.array(npr.randint(25,31,size = (2,2)))
ar6 = np.array(npr.randint(25,31,size = (2,2)))
print(ar5)
print(ar6)

arCommon = (ar5 == ar6)
print(arCommon)
print(ar5[arCommon])

arDiff = (ar5 != ar6)
print(arDiff)
print(ar5[arDiff])
