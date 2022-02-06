#Dizeler bile yinelenebilir nesnelerdir ve bir yineleyici döndürebilir.
stringim = "Cilek"
iterable = iter(stringim)

print(next(iterable))
print(next(iterable))
print(next(iterable))
print(next(iterable))
print(next(iterable))


#Iterable dögü ile kullanmak.
mytuple = ("Elma", "Muz", "Cilek")
for x in mytuple:
  print(x)