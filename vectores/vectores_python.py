# PUNTO 1
lista = []

# PUNTO 2
elem = ['chevrolet','ford','bmw','audi','cadillac','susuki','hyundai']

# PUNTO 3
print('longitud de listas',len(lista))
print('longitud de listas',len(elem))

# PUNTO 4
a1= elem[0]
print(a1)
a2=elem[3]
print(a2)
a3=elem[6]
print(a3)

# PUNTO 5
datosp=['Josue','17 años','1,78','comprometido','crespo']
datos=input("ingrese datos")
datosp.append(datos)
print(datosp)

# PUNTO 6
it_companies=['facebook','google','microsoft','apple','ibm','oracle','amazon']

# PUNTO 7
it_companies1=input('ingrese otra empresa')
it_companies.insert(5,it_companies1)
print(it_companies)

# PUNTO 8
comprobar= 'apple' in it_companies
print(comprobar)

# PUNTO 9
it_companies.sort()
print(it_companies)

# PUNTO 10
it_companies.sort(reverse=True)
print(it_companies)

# PUNTO 11
it_companies.pop()
print(it_companies)

del it_companies[4]
print(it_companies)

# PUNTO 12
it_companies.clear()
print(it_companies)