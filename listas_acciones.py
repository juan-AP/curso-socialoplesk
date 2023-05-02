correo = "fOo@foo.com"
nombre = "foosi"

#lista
correos = ["bar@bar.com","bax@bax.com","equals@eali.com","fred@fred.com"]

#agregar valores al final de una lista
correos.append("foot@foot.com")
print(correos)

#agregar valores al comienzo de una lista
correos.insert(0,"hola@hola.com")
print(correos)

#eliminar un correo de la lista
#del correos[0]
r = correos.pop(0)#eliminar con indice
print(correos)
#valor o correo que se elimino de la lista
print(r)
correos.remove("bax@bax.com")#eliminar por valor 
print(correos)

del correos[:3]
print(correos)

correos[0] = "nuevo@nuevo.com"
print(correos)