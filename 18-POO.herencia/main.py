import clases
from clases import Informatico, TecnicoRedes

persona = clases.Persona()
persona.setNombre ("Pablo")
persona.setApellido("Vandecaveye")
persona.setEdad ("90")
persona.setAltura ("172cm")

print("====================================================================")
print (f"La persona es: {persona.getNombre()} {persona.getApellido()}")
print(persona.hablar())

# Crar un informatico

Informatico = clases.Informatico()

Informatico.setNombre ("Carlos")
Informatico.setApellido ("Gomez")


print(f"El informatico es: {Informatico.getNombre()} {Informatico.getApellido()} ")
print(f"tiene Experiencia en: {Informatico.getLenguajes()}" )
print(Informatico.experiencia)

print("==================================================================")

tecnico = clases.TecnicoRedes()
tecnico.setNombre ("Manolo")
print(tecnico.auditarRedes, tecnico.getNombre(),tecnico.getLenguajes())

print("==================================================================")

