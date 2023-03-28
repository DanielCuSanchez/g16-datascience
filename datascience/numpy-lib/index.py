import numpy as np
import matplotlib.pyplot as plt

#arrays


#print(type(np))
#print(np)


a = np.array([100,244,3,4,5,6,7,8,9,10,300])
b = np.array([14.4,2,3,4,5.3,6,7,7.6,9,True, False, "kjddk"])

print(type(a))

print(a)
print(b)

# arr = [1,3,4,6]
# arr.map(e=> e > 3)
# arr.filter(e=> e > 3)

#print(type(None))
a.sort()
#print(a.sort())

c = np.array([[100,3,4,10],[6,7,0,10]])
d = np.array([[[100,3],[6,7], [4.5,5]]])

print(c[1][1])
c.sort(axis=1)

#print(c)
print(np.sort(c, axis=1))


# probability, statistics, distributions and more...

mean = a.mean()
print(mean)

max = a.max()
print(max)

min = a.min()
print(min)

avg = np.average(a)
print(avg)

std = np.std(a)
print(std)

# Dimensions

print("Dimensiones")
print("A =",a.ndim)
print("B =",b.ndim)
print("C =",c.ndim)
print("D =",d.ndim)

print("Tamaños")
print("A =", a.size)
print("B =", b.size)
print("C =", c.size)
print("D =", d.size)

print("Formas")
print("A = ",np.shape(a))
print("B = ",np.shape(b))
print("C = ",np.shape(c))
print("D = ",np.shape(d))

e = np.array([[[56,76,100,32,1,4,0]]])


#Tradicional
print("Tradicional")
for a in e:
  for b in a:
    for c in b:
      print(c)

for x in e:
  print(x)

#Nditer
for x in np.nditer(e[:,:,1:3]):
  print(x)


a = np.array([100, 244, 3, 4, 5, 6, 7, 8, 9, 10, 300])
print(a)
print(a[1:3])

# index every item
for idn, n in np.ndenumerate(e):
  print(idn, n)

plt.plot(a)
plt.show()