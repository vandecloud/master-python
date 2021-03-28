from datetime import time
import notas.nota as modelo


class Acciones:
    def crear (self, usuario):
        print(f"\nOK {usuario[1]}!! Vamos a crear una nota ...")
        
        titulo = input ("Introduce el titulo de tu nota: ")
        descripcion = input ("Introduce el contenido de tu nota: ")
        
        nota = modelo.Nota(usuario[0], titulo, descripcion)
        guardar = nota.guardar()
        
        if guardar [0] >= 1:
            print (f"\nPerfecto Guardamos has guardado tu nota  {nota.titulo}")
        
        else:
            print (f"\nNo se a guardo la nota {usuario[1]}")
    
    def mostrar(self, usuario):
        print(f"\nVale {usuario [1]}!! Aqui tienes tus notas: ")
        
        nota = modelo.Nota(usuario[0])
        notas = nota.listar()
        
        for nota in notas:
            print("\n*********************************")
            print(nota[2])
            print(nota[3])
            print("\n*********************************")
    
    def borrar (self, usuario):
        print(f"\n Okey {usuario[1]}!! vamos a borrar notas ")
        
        titulo = input("Introduce el titulo de la nota a borrar: ")
        
        nota = modelo.Nota(usuario[0], titulo)
        
        eliminar = nota.eliminar()
        
        if eliminar[0] >= 1:
            print(f"Hemos borrado la nota {nota.titulo}")
            
        else:
            print ("No se ha borrado la nota, prueba luego.. ")
        
    