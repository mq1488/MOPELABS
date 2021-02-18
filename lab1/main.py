from random import randrange

a0 = 2
a1 = 3
a2 = 2
a3 = 1

X1, X2, X3, Xn1, Xn2, Xn3 = [], [], [], [], [], []


print("a0={0} \na1={1} \na2={2} \na3={3}\n".format(a0, a1, a2, a3))




for i in range(0,8):
    X1.append(randrange(1, 21, 1))
    X2.append(randrange(1, 21, 1))
    X3.append(randrange(1, 21, 1))

print("X1: " + str(X1))
print("X2: " + str(X2))
print("X3: " + str(X3) + '\n')


Y = [a0 + a1*X1[i] + a2*X2[i] + a3*X3[i] for i in range(8)]
print("Y: " + str(Y))
print('Max Y = ' + str(max(Y))+ '\n')



X01 = (max(X1)+min(X1))/2
X02 = (max(X2)+min(X2))/2
X03 = (max(X3)+min(X3))/2
print("x01={0} \nx02={1} \nx03={2} \n".format(X01, X02, X03))


dX1 = X01-min(X1)
dX2 = X02-min(X2)
dX3 = X03-min(X3)
print("dx01={0} \ndx02={1} \ndx03={2} \n".format(dX1, dX2, dX3))



for i in range(0, 8):
    Xn1.append((X1[i] - X01)/dX1)
    Xn2.append((X2[i] - X02)/dX2)
    Xn3.append((X3[i] - X03)/dX3)

print("Xn1: " + str(Xn1))
print("Xn2: " + str(Xn2))
print("Xn3: " + str(Xn3) + '\n')


Yet = a0 + a1*X01 + a2*X02 + a3*X03
f = [(Y[i]-Yet)**2 for i in range(8)]
res = min(f)

print("Yэт: " + str(Yet))
print("(Y-Yэт)²: " + str(f))
print("min(Y-Yэт)²: " + str(res))
