i = 0.15
n = 10
a = 15000
pvi = a * ((1+i)**n - 1)/(i*(1+i)**n)
for n in range(1, 11):
    pvi = a * ((1 + i) ** n - 1) / (i * (1 + i) ** n)
    print("pvi: ", pvi, "year: ", n, 60000-pvi)

i = 0.15
n = 10
a = 15000
pvi = a * ((1+i)**n - 1)/(i*(1+i)**n)
for n in range(1, 11):
    pvi = a * ((1 + i) ** n - 1) / (i * (1 + i) ** n)
    fac = 1 / (1 + i) ** n
    pvd = pvi * fac
    print("pvd: ", pvd, "year: ", n, 60000-pvi)

i = 0.18
n = 8
a = 50000
pvi = a * ((1+i)**n - 1)/(i*(1+i)**n)
net = pvi - 225000
print("net: ", net)

salvage = 20000
nsal = salvage * (1/(1+i)**n)
newnet = net + nsal
print("sal net: ", newnet)


i = 0.14
n = 8
a = 50000
pvi = a * ((1+i)**n - 1)/(i*(1+i)**n)
net = pvi - 225000

irr = 0.15
n = 8
a = 50000
pvirr = a * ((1+irr)**n - 1)/(irr*(1+irr)**n)
irrz = 225000 - pvirr
print("irrz: 恰好为正", irrz)