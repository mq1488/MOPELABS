import math, random,numpy


pList = (0.99, 0.98, 0.95, 0.90)
rkrTable = {2: (1.73, 1.72, 1.71, 1.69),
             6: (2.16, 2.13, 2.10, 2.00),
             8: (2.43, 4.37, 2.27, 2.17),
             10: (2.62, 2.54, 2.41, 2.29),
             12: (2.75, 2.66, 2.52, 2.39),
             15: (2.9, 2.8, 2.64, 2.49),
             20: (3.08, 2.96, 2.78, 2.62)}


minYlimit, maxYlimit = 70, 170
x1Min, x1MinNorm = -15, -1
x1Max, x1MaxNorm = 30, 1
x2Min, x2MinNorm = 5, -1
x2Max, x2MaxNorm = 40, 1




Experiments = 5


yArray = [[random.randint(minYlimit, maxYlimit) for i in range(Experiments)] for j in range(3)]

averArrayY = [sum(yArray[i][j] for j in range(Experiments)) / Experiments for i in range(3)]

for i in range(0,3):
    print('Y' + str(i+ 1) + ': ' + str(yArray[i]) + ' Середне значення: ' + str(averArrayY[i]))


sigma1 = sum([(j - averArrayY[0]) ** 2 for j in yArray[0]]) / Experiments
sigma2 = sum([(j - averArrayY[1]) ** 2 for j in yArray[1]]) / Experiments
sigma3 = sum([(j - averArrayY[2]) ** 2 for j in yArray[2]]) / Experiments
tetaSigma = math.sqrt((2 * (2 * Experiments - 2)) / (Experiments * (Experiments - 4)))


print('\nДисперсія: \n1: ' + str(sigma1) + '\n2: ' + str(sigma2) + '\n3: ' + str(sigma3) + '\n')
print('Основне відхилення: ' + str(tetaSigma) + '\n')


fUV1 = sigma1 / sigma2
fUV2 = sigma3 / sigma1
fUV3 = sigma3 / sigma2

print('fUV: \n1: ' + str(fUV1) + '\n2: ' + str(fUV2) + '\n3: ' + str(fUV3) + '\n')


tetaUV1 = ((Experiments - 2) / Experiments) * fUV1
tetaUV2 = ((Experiments - 2) / Experiments) * fUV2
tetaUV3 = ((Experiments - 2) / Experiments) * fUV3

print('Teta UV: \n1: ' + str(tetaUV1) + '\n2: ' + str(tetaUV2) + '\n3: ' + str(tetaUV3) + '\n')


rUV1 = abs(tetaUV1 - 1) / tetaSigma
rUV2 = abs(tetaUV2 - 1) / tetaSigma
rUV3 = abs(tetaUV3 - 1) / tetaSigma

print('rUV UV: \n1: ' + str(rUV1) + '\n2: ' + str(rUV2) + '\n3: ' + str(rUV3) + '\n')


mX1 = (-1 + 1 - 1) / 3
mX2 = (-1 - 1 + 1) / 3
mY = sum(averArrayY) / 3

print('Mx1: ' + str(mX1) + '\nMx2: ' + str(mX2) + '\nmY: ' + str(mY) + '\n')


A1 = (1 + 1 + 1) / 3
A2 = (1 - 1 - 1) / 3
A3 = (1 + 1 + 1) / 3
A11 = (-1 * averArrayY[0] + 1 * averArrayY[1] - 1 * averArrayY[2]) / 3
A22 = (-1 * averArrayY[0] - 1 * averArrayY[1] + 1 * averArrayY[2]) / 3

print('a1: ' + str(A1) + '\na2: ' + str(A2) + '\na3: ' + str(A3) + '\na11: '+ str(A11) + '\na22: '+ str(A22) + '\n')


B0 = numpy.linalg.det(numpy.dot([[mY, mX1, mX2],
                           [A11, A1, A2],
                           [A22, A2, A3]],
                          numpy.linalg.inv([[1, mX1, mX2],
                                         [mX1, A1, A2],
                                         [mX2, A2, A3]])))

B1 = numpy.linalg.det(numpy.dot([[1, mY, mX2],
                           [mX1, A11, A2],
                           [mX2, A22, A3]],
                          numpy.linalg.inv([[1, mX1, mX2],
                                         [mX1, A1, A2],
                                         [mX2, A2, A3]])))

B2 = numpy.linalg.det(numpy.dot([[1, mX1, mY],
                           [mX1, A1, A11],
                           [mX2, A2, A22]],
                          numpy.linalg.inv([[1, mX1, mX2],
                                         [mX1, A1, A2],
                                         [mX2, A2, A3]])))


print('b0: ' + str(B0) + '\nb1: ' + str(B1) + '\nb2: ' + str(B2) + '\n')


def checkRegression():
    normY1 = round(B0 - B1 - B2, 1)
    normY2 = round(B0 + B1 - B2, 1)
    normY3 = round(B0 - B1 + B2, 1)
    if normY1 == averArrayY[0] and normY2 == averArrayY[1] and normY3 == averArrayY[2]:
        print("Значення перевірки нормаваного рівняння регресії сходяться")
    else:
        print("Значення перевірки нормаваного рівняння регресії НЕ сходяться")

normY = B0 - B1 + B2

dx1 = math.fabs(x1Max - x1Min) / 2
dx2 = math.fabs(x2Max - x2Min) / 2
x10 = (x1Max + x1Min) / 2
x20 = (x2Max + x2Min) / 2

aa0 = B0 - B1 * x10 / dx1 - B2 * x20 / dx2
aa1 = B1 / dx1
aa2 = B2 / dx2

print('Натуралізація коефіцієнтів: ' + '\n' + 'dX1: ' + str(dx1) + '\ndX2: ' + str(dx2) + '\nx10: ' + str(x10) +
      '\nx20: ' + str(x10) + '\n' )

print('aa0: ' + str(aa0) + '\naa1: ' + str(aa1) + '\naa2: ' + str(aa2) + '\n')


def odnoridna_dispersion(Experements):
    global rUV1,rUV2,rUV3,rkrTable
    m = min(rkrTable, key=lambda x: abs(x - Experiments))
    p = 0
    for ruv in (rUV1, rUV2, rUV3):
        if ruv > rkrTable[m][0]:
            return False
        for rkr in range(len(rkrTable[m])):
            if ruv < rkrTable[m][rkr]:
                p = rkr
    return pList[p]


if not odnoridna_dispersion(Experiments):
    print('Дисперсія неоднорідна, збілушуемо кількість дослідів')
    Experiments += 1
    odnoridna_dispersion(Experiments)
else:
    print("Однорідна дисперсія:", odnoridna_dispersion(Experiments))

print('\n')

def naturalized_regression(x1, x2):
    return aa0 + aa1 * x1 + aa2 * x2



print("Натуралізоване рівняння регресії:")

NRY = [round(naturalized_regression(x1Min, x2Min), 2),
        round(naturalized_regression(x1Max, x2Min), 2),
        round(naturalized_regression(x1Min, x2Max), 2)]
print(NRY)
if NRY == averArrayY:
    print("Коефіцієнти натуралізованого рівняння регресії вірні")
else:
    print("Коефіцієнти натуралізованого рівняння регресії НЕ вірні")
checkRegression()
