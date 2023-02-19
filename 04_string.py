name = 'Miguel'
last_name = 'Jaramillo'
print(name)
print(last_name)

full_name = name + " " + last_name

print(full_name)

quote = "I'm Miguel"
print(quote)

quote2 = 'She said "Hello" '
print(quote2)

#format
# Tres formas de dar formato al texto

template = "Hola, mi nombre es " + name + " y mi apellido es " + last_name
print('v1',template)

template = "Hola, mi nombre es {} y mi apellido es {}".format(name,last_name)
print('v2',template)

template = f"Hola, mi nombre es {name} y mi apellido es {last_name}"
print('v3',template)

#reto, juntar el nombre con el apellido y agregar la edad

#Craemos la variable edad
my_age = 29

template = f"Hola, mi nombre es {name} {last_name} y mi edad es {my_age} años"
print('v3',template)


