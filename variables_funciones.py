correo = "fOo@foo.com"
nombre = "foosi"
correos = ["bar@bar.com","bax@bax.com","equals@eali.com"]
edad = 19

#escribir texto en minusculas
correo_lower = correo.lower()

print(correo)
print(correo_lower)

#escribir texto en mayusculas
correo_upper = correo.upper()
print("-----------------------------------------")
print(correo)
print(correo_upper)

#escribir una extension .com y .fred
print("-----------------------------------------")
cp = correo.replace("com","fred")
print(correo)
print(cp)

#cuenta la cantidad de veces que aparece una letra en un texto
print("-----------------------------------------")
print(correo)
print(correo.count("o"))