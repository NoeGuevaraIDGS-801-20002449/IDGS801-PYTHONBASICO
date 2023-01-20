cadena = "universidad tecnologica de Leon"

print(cadena)
print(cadena.lower()) # Minusculas
print(cadena.upper()) # Mayusculas
print(cadena.title()) # En forma de Titulo
print(cadena.find("de")) # Encuentra
print(cadena.count("a")) # Cuenta

texttoFinal = cadena.replace("a" , "4") # Remplaza
print(texttoFinal)
cadenaNueva = cadena.split(" ") # Separa las palabras por comillas
print(cadenaNueva)