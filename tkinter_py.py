import tkinter as tk
from tkinter import messagebox
import json
import re 
import os 

class SistemaLogin:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Sistema de Login")
        self.ventana.geometry("400x500")
        self.ventana.resizable(False, False)
        
        # Archivo para guardar usuarios
        self.archivo_usuarios = "usuarios.json"  
        self.usuario_actual = None 
    
        # Inicializar archivo si no existe
        if not os.path.exists(self.archivo_usuarios):  
            with open(self.archivo_usuarios, 'w') as f:  
                json.dump([], f)
                
        # Mostrar pantalla de inicio de sesión
        self.mostrar_inicio_sesion()
        
    def limpiar_ventana(self):
        """Elimina todos los widgets de la ventana"""
        for widget in self.ventana.winfo_children():
            widget.destroy()
    
    def cargar_usuarios(self):
        """Carga usuarios desde el archivo JSON"""
        try: 
            with open(self.archivo_usuarios, 'r') as f:  
                return json.load(f)
        except:
            return []
        
    def guardar_usuario(self, usuario):  
        """Guarda un nuevo usuario en el archivo JSON"""
        usuarios = self.cargar_usuarios()
        usuarios.append(usuario)  
        with open(self.archivo_usuarios, 'w') as f:
            json.dump(usuarios, f, indent=2)
                
    def validar_contrasena(self, contrasena):
        """Valida que la contraseña cumpla con los requisitos"""
        if len(contrasena) < 6:
            return False, "La contraseña debe tener mínimo 6 caracteres"
        
        if not re.search(r'[A-Z]', contrasena):
            return False, "La contraseña debe tener al menos una mayúscula"
        
        if not re.search(r'[a-z]', contrasena):
            return False, "La contraseña debe tener al menos una minúscula"
        
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', contrasena):
            return False, "La contraseña debe tener al menos un carácter especial"
    
        return True, ""  # 
    
    def mostrar_inicio_sesion(self):
        """Muestra la pantalla de inicio de sesión"""
        self.limpiar_ventana()
        self.ventana.title("Inicio de Sesión")
        
        # Frame principal
        frame = tk.Frame(self.ventana, bg="#f0f0f0")
        frame.pack(expand=True, fill="both", padx=20, pady=20)
        
        # Título
        titulo = tk.Label(frame, text="Iniciar Sesión", 
                          font=("Arial", 24, "bold"), bg="#f0f0f0")  
        titulo.pack(pady=30)
        
        # Correo electrónico
        tk.Label(frame, text="Correo electrónico:", 
                 font=("Arial", 12), bg="#f0f0f0").pack(anchor="w", pady=(10, 5))
        entry_correo = tk.Entry(frame, font=("Arial", 12), width=30)
        entry_correo.pack(pady=(0, 15))
        
        # Contraseña
        tk.Label(frame, text="Contraseña:",
                 font=("Arial", 12), bg="#f0f0f0").pack(anchor="w", pady=(10, 5))
        entry_contrasena = tk.Entry(frame, font=("Arial", 12), width=30, show="*")  
        entry_contrasena.pack(pady=(0, 20))
        
        # Botón de inicio de sesión
        btn_inicio = tk.Button(frame, text="Iniciar Sesión",
                               font=("Arial", 12, "bold"),
                               bg="#4CAF50", fg="white",
                               width=20, height=2,
                               command=lambda: self.validar_login(
                                    entry_correo.get(), 
                                    entry_contrasena.get()))
        btn_inicio.pack(pady=15)
        
        # Separador
        tk.Label(frame, text="- O -", 
                font=("Arial", 10), bg="#f0f0f0", fg="gray").pack(pady=10)
        
        # Botón de registro
        btn_registro = tk.Button(frame, text="Crear Cuenta Nueva", 
                                font=("Arial", 12, "bold"),
                                bg="#2196F3", fg="white",
                                width=20, height=2,
                                command=self.mostrar_registro)
        btn_registro.pack(pady=10)
        
    def validar_login(self, correo, contrasena):
        """Valida las credenciales de inicio de sesión"""
        if not correo or not contrasena:
            messagebox.showerror("Error", "Por favor complete todos los campos")
            return  
                
        usuarios = self.cargar_usuarios()
            
        for usuario in usuarios: 
            if usuario['correo'] == correo and usuario['contrasena'] == contrasena:
                self.usuario_actual = usuario 
                self.mostrar_home()
                return
            
        messagebox.showerror("Error",
                           "Correo o contraseña incorrectos.\n"
                           "Usuario no encontrado o credenciales inválidas.")
            
    def mostrar_registro(self):
        """Muestra la pantalla de registro"""
        self.limpiar_ventana()
        self.ventana.title("Registro de Usuario")

        # Frame principal 
        frame = tk.Frame(self.ventana, bg="#f0f0f0")
        frame.pack(expand=True, fill="both", padx=20, pady=20)
                
        # Título
        titulo = tk.Label(frame, text="Crear Cuenta",
                          font=("Arial", 24, "bold"), bg="#f0f0f0") 
        titulo.pack(pady=20)
                
        # Nombre 
        tk.Label(frame, text="Nombre:",
                font=("Arial", 12), bg="#f0f0f0").pack(anchor="w", pady=(10, 5))  
        entry_nombre = tk.Entry(frame, font=("Arial", 12), width=30)
        entry_nombre.pack(pady=(0, 10))
                                       
        # Apellido
        tk.Label(frame, text="Apellido:",
                font=("Arial", 12), bg="#f0f0f0").pack(anchor="w", pady=(10, 5))  
        entry_apellido = tk.Entry(frame, font=("Arial", 12), width=30)
        entry_apellido.pack(pady=(0, 10))
                
        # Correo electrónico
        tk.Label(frame, text="Correo electrónico:",
                font=("Arial", 12), bg="#f0f0f0").pack(anchor="w", pady=(10, 5))  
        entry_correo = tk.Entry(frame, font=("Arial", 12), width=30)
        entry_correo.pack(pady=(0, 10))
                
        # Contraseña
        tk.Label(frame, text="Contraseña:",
                font=("Arial", 12), bg="#f0f0f0").pack(anchor="w", pady=(10, 5)) 
        entry_contrasena = tk.Entry(frame, font=("Arial", 12), width=30, show="*")
        entry_contrasena.pack(pady=(0, 15))
                
        # Requisitos de contraseña
        info_contrasena = tk.Label(frame,
                                  text="Mínimo 6 caracteres, 1 mayúscula,\n1 minúscula y 1 carácter especial",
                                  font=("Arial", 9), fg="gray", bg="#f0f0f0")
        info_contrasena.pack(pady=(0, 15))
                
        # Botón de registro
        btn_registro = tk.Button(frame, text="Registrarse",
                                font=("Arial", 12, "bold"),
                                bg="#2196F3", fg="white",
                                width=20, height=2,
                                command=lambda: self.procesar_registro(
                                    entry_nombre.get(),
                                    entry_apellido.get(),
                                    entry_correo.get(),
                                    entry_contrasena.get()))
        btn_registro.pack(pady=10)
                
        # Enlace a inicio de sesión
        frame_login = tk.Frame(frame, bg="#f0f0f0")
        frame_login.pack(pady=10)
                
        tk.Label(frame_login, text="¿Ya tienes cuenta? ",
                font=("Arial", 10), bg="#f0f0f0").pack(side="left")
            
        link_login = tk.Label(frame_login, text="Iniciar Sesión",
                             font=("Arial", 10, "underline"),
                             fg="blue", bg="#f0f0f0", cursor="hand2")
        link_login.pack(side="left")
        link_login.bind("<Button-1>", lambda e: self.mostrar_inicio_sesion())
                
    def procesar_registro(self, nombre, apellido, correo, contrasena):
        """Procesa el registro de un nuevo usuario"""
        # Validar campos vacíos
        if not nombre or not apellido or not correo or not contrasena:
            messagebox.showerror("Error", "Por favor complete todos los campos")
            return
        
        # Validar formato de correo
        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', correo):
            messagebox.showerror("Error", "Por favor ingrese un correo válido")
            return
        
        # Validar que el correo no esté registrado
        usuarios = self.cargar_usuarios()
        for usuario in usuarios:
            if usuario['correo'] == correo:
                messagebox.showerror("Error", "El correo ya está registrado.\nPor favor utilice otro correo.")
                return
        
        # Validar contraseña
        valida, mensaje = self.validar_contrasena(contrasena)  
        if not valida:
            messagebox.showerror("Error", mensaje)
            return
                
        # Guardar nuevo usuario
        nuevo_usuario = {
            'nombre': nombre,
            'apellido': apellido,
            'correo': correo,
            'contrasena': contrasena
        }
                
        self.guardar_usuario(nuevo_usuario)  
        messagebox.showinfo("Éxito", "Usuario registrado correctamente.\nAhora puede iniciar sesión.")
                
        self.mostrar_inicio_sesion()
            
    def mostrar_home(self):
        """Muestra la pantalla principal"""
        self.limpiar_ventana()
        self.ventana.title("Inicio")
                
        # Frame Principal
        frame = tk.Frame(self.ventana, bg="#e8f5e9")
        frame.pack(expand=True, fill="both")  
                
        # Mensaje de bienvenida
        bienvenida = tk.Label(frame,
                            text="¡Bienvenido/a!",
                            font=("Arial", 28, "bold"),  
                            bg="#e8f5e9", fg="#2e7d32")
        bienvenida.pack(pady=30)
        
        nombre_completo = tk.Label(frame,
                                  text=f"{self.usuario_actual['nombre']} {self.usuario_actual['apellido']}",
                                  font=("Arial", 20),
                                  bg="#e8f5e9", fg="#1b5e20")
        nombre_completo.pack(pady=10)
                
        # Contenido Adicional 
        info_frame = tk.Frame(frame, bg="#ffffff", relief="solid", borderwidth=1)
        info_frame.pack(pady=30, padx=40, fill="both", expand=True)
                
        tk.Label(info_frame,
                text="Panel Principal",
                font=("Arial", 18, "bold"),  
                bg="#ffffff").pack(pady=20)
                
        tk.Label(info_frame,
                text=f"Correo: {self.usuario_actual['correo']}",
                font=("Arial", 12),
                bg="#ffffff").pack(pady=10)
                         
        tk.Label(info_frame,
                text="Has iniciado sesión correctamente en el sistema.", 
                font=("Arial", 11),
                bg="#ffffff", fg="gray").pack(pady=20)
                
        # Botón de cerrar sesión
        btn_cerrar_sesion = tk.Button(frame, text="Cerrar Sesión",
                                     font=("Arial", 12, "bold"),
                                     bg="#f44336", fg="white",
                                     width=20, height=2,
                                     command=self.cerrar_sesion)
        btn_cerrar_sesion.pack(pady=20)
                
    def cerrar_sesion(self):
        """Cierra la sesión del usuario actual"""
        self.usuario_actual = None
        self.mostrar_inicio_sesion()
                
    def ejecutar(self):
        """Inicia la aplicación"""
        self.ventana.mainloop()


if __name__ == "__main__":
    app = SistemaLogin()
    app.ejecutar()