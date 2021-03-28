from logging import exception
import usuarios.usuario as modelo
import notas.acciones


class Acciones:

    def registro(self):
        print("\nOK!! Vamos a registrarte en el sistema..")

        nombre = input("¿cual es tu Nombre?: ")
        apellidos = input("¿cuales son tus Apellido: ")
        email = input("Introduce tu email: ")
        password = input("Introduce una contraseña: ")

        usuario = modelo.Usuario(nombre, apellidos, email, password)
        registro = usuario.registrar()

        if registro[0] >= 1:
            print(
                f"Perfecto {registro[1].nombre} te has registrado con el email {registro[1].email}")

        else:
            ("NO te has registrado correctamente")

    def login(self):
        print("\nIdentificate en el sistema.." )
        
        try:
            
            email = input ("Introduce tu email: ")
            password = input ("Introduce tu contraseña: ")

            usuario = modelo.Usuario("", "",email, password)
            login = usuario.identificar()
                    
            if email == login[3]:
                print(f"\nBienvenido {login [1]}, te has registrador en el sistema el {login[5]} ")
                self.proximasAcciones(login)
        except Exception as e:
            print (type(e))
            print (type(e).__name__)
            print(f"Login Incorrecto intentalo mas tarde")
            
    def proximasAcciones(self, usuario):
        print("""
              Acciones disponibles
              - Crear nota (crear)
              - Mostrar tus notas (mostrar)
              - Eliminar Notas (eliminar)
              - Salir (salir)
              """)
        
        acciones = input ("¿que quieres hacer?: ")
        hazEl = notas.acciones.Acciones()
        
        if acciones == "crear":
            hazEl.crear(usuario)
            self.proximasAcciones(usuario)
            
        elif acciones == "mostrar":
            hazEl.mostrar(usuario)
            self.proximasAcciones(usuario)
            
        elif acciones == "eliminar":
            hazEl.borrar(usuario)
            self.proximasAcciones(usuario)
            
        elif acciones == "salir":
            print (f"Hasta pronto {usuario [1]}")
            exit()               
         
                        
            
