Sistema de Login con Tkinter
📋 Descripción
Sistema de autenticación completo desarrollado en Python utilizando la biblioteca Tkinter. Permite a los usuarios registrarse, iniciar sesión y acceder a una pantalla principal personalizada con persistencia de datos en formato JSON.

👥 Autores
Pablo Arce Álvarez
Universidad Creativa - Certificación en Inteligencia Artificial
Curso: IA04 - Razonamiento Artificial
Profesor: Angelo Ortiz Vega
🚀 Características
✨ Funcionalidades Principales
Registro de Usuarios
Formulario completo con nombre, apellido, correo y contraseña
Validación de correo electrónico
Validación robusta de contraseñas
Verificación de correos duplicados
Inicio de Sesión
Autenticación segura
Validación de credenciales
Mensajes de error descriptivos
Pantalla Principal (Home)
Mensaje de bienvenida personalizado
Visualización de información del usuario
Función de cierre de sesión
🔒 Validaciones de Seguridad
La contraseña debe cumplir con los siguientes requisitos:

✅ Mínimo 6 caracteres
✅ Al menos 1 letra mayúscula
✅ Al menos 1 letra minúscula
✅ Al menos 1 carácter especial (!@#$%^&*(),.?":{}|<>)
🛠️ Requisitos del Sistema
Software Necesario
Python 3.7 o superior
Tkinter (incluido por defecto en Python)
Bibliotecas estándar de Python:
json - Manejo de datos
re - Expresiones regulares
os - Operaciones del sistema
Instalación de Python
Windows:

bash
# Descargar desde https://www.python.org/downloads/
# Asegúrate de marcar "Add Python to PATH" durante la instalación
macOS:

bash
brew install python3
Linux:

bash
sudo apt-get update
sudo apt-get install python3 python3-tk
📦 Instalación
1. Clonar el repositorio
bash
git clone https://github.com/tu-usuario/sistema-login-tkinter.git
cd sistema-login-tkinter
2. Verificar instalación de Python
bash
python --version
# o
python3 --version
3. Verificar que Tkinter esté instalado
bash
python -m tkinter
# Debe abrir una ventana de prueba
🎮 Uso
Ejecutar la aplicación
bash
python tkinter_py.py
Flujo de uso paso a paso
1️⃣ Primera vez - Registro
Al iniciar la aplicación, verás la pantalla de Inicio de Sesión
Haz clic en el botón "Crear Cuenta Nueva" (azul)
Completa el formulario de registro:
Nombre
Apellido
Correo electrónico
Contraseña (debe cumplir los requisitos de seguridad)
Haz clic en "Registrarse"
Si el registro es exitoso, serás redirigido al inicio de sesión
2️⃣ Iniciar Sesión
Ingresa tu correo electrónico
Ingresa tu contraseña
Haz clic en "Iniciar Sesión" (verde)
Serás redirigido a la pantalla principal
3️⃣ Pantalla Principal
Verás un mensaje de bienvenida con tu nombre completo
Se muestra tu correo electrónico registrado
Para salir, haz clic en "Cerrar Sesión" (rojo)
📁 Estructura del Proyecto
sistema-login-tkinter/
│
├── tkinter_py.py          # Código principal de la aplicación
├── usuarios.json          # Base de datos de usuarios (se crea automáticamente)
├── README.md              # Este archivo
└── .gitignore            # Archivos ignorados por Git (opcional)
💾 Persistencia de Datos
Formato de Almacenamiento
Los usuarios se guardan en el archivo usuarios.json con la siguiente estructura:

json
[
  {
    "nombre": "Juan",
    "apellido": "Pérez",
    "correo": "juan.perez@example.com",
    "contrasena": "MiPass123!"
  },
  {
    "nombre": "María",
    "apellido": "González",
    "correo": "maria.gonzalez@example.com",
    "contrasena": "Secure456#"
  }
]
Ubicación del Archivo
El archivo usuarios.json se crea automáticamente en el mismo directorio que tkinter_py.py
Si el archivo no existe, se creará vacío al iniciar la aplicación
Los datos persisten entre ejecuciones de la aplicación
⚠️ Solución de Problemas
Error: "No module named 'tkinter'"
Solución en Linux:

bash
sudo apt-get install python3-tk
Solución en macOS:

bash
brew install python-tk
Error: "Permission denied" al crear usuarios.json
Solución:

Asegúrate de tener permisos de escritura en el directorio
Ejecuta la aplicación desde una carpeta donde tengas permisos
La aplicación no inicia
Verificar:

Que Python esté correctamente instalado
Que el archivo tkinter_py.py no tenga errores de sintaxis
Que tengas permisos de ejecución
No puedo iniciar sesión
Posibles causas:

Verifica que hayas registrado el usuario primero
Asegúrate de escribir el correo y contraseña correctamente
Revisa que el archivo usuarios.json exista y contenga datos
🎨 Capturas de Pantalla
Pantalla de Inicio de Sesión
┌─────────────────────────────────────┐
│                                     │
│         Iniciar Sesión              │
│                                     │
│  Correo electrónico:                │
│  [____________________]             │
│                                     │
│  Contraseña:                        │
│  [____________________]             │
│                                     │
│   [   Iniciar Sesión   ]            │
│                                     │
│          - O -                      │
│                                     │
│   [  Crear Cuenta Nueva ]           │
│                                     │
└─────────────────────────────────────┘
Pantalla de Registro
┌─────────────────────────────────────┐
│                                     │
│         Crear Cuenta                │
│                                     │
│  Nombre:                            │
│  [____________________]             │
│                                     │
│  Apellido:                          │
│  [____________________]             │
│                                     │
│  Correo electrónico:                │
│  [____________________]             │
│                                     │
│  Contraseña:                        │
│  [____________________]             │
│                                     │
│  Mínimo 6 caracteres, 1 mayúscula,  │
│  1 minúscula y 1 carácter especial  │
│                                     │
│     [   Registrarse    ]            │
│                                     │
│  ¿Ya tienes cuenta? Iniciar Sesión  │
│                                     │
└─────────────────────────────────────┘
Pantalla Principal (Home)
┌─────────────────────────────────────┐
│                                     │
│        ¡Bienvenido/a!               │
│                                     │
│        Juan Pérez                   │
│                                     │
│  ┌─────────────────────────────┐   │
│  │   Panel Principal           │   │
│  │                             │   │
│  │ Correo: juan@example.com    │   │
│  │                             │   │
│  │ Has iniciado sesión         │   │
│  │ correctamente en el sistema │   │
│  └─────────────────────────────┘   │
│                                     │
│     [   Cerrar Sesión    ]          │
│                                     │
└─────────────────────────────────────┘
🔄 Flujo de Navegación
      ┌─────────────────┐
      │  Inicio Sesión  │
      └────────┬────────┘
               │
         ┌─────┴─────┐
         │           │
    Registrarse   Iniciar
         │        Sesión
         │           │
         ▼           ▼
   ┌──────────┐  ┌──────┐
   │ Registro │  │ Home │
   └────┬─────┘  └───┬──┘
        │            │
        └────────────┤
                     │
              Cerrar Sesión
                     │
                     ▼
            ┌─────────────────┐
            │  Inicio Sesión  │
            └─────────────────┘
🧪 Casos de Prueba
Test 1: Registro Exitoso
Abrir la aplicación
Clic en "Crear Cuenta Nueva"
Ingresar datos válidos
Verificar mensaje de éxito
Verificar redirección a login
Test 2: Registro con Correo Duplicado
Intentar registrar un correo ya existente
Verificar mensaje de error
Test 3: Contraseña Inválida
Intentar registrar con contraseña débil
Verificar mensaje de error específico
Test 4: Login Exitoso
Ingresar credenciales correctas
Verificar acceso a home
Verificar nombre mostrado correctamente
Test 5: Login Fallido
Ingresar credenciales incorrectas
Verificar mensaje de error
Test 6: Cerrar Sesión
Estando en home, clic en "Cerrar Sesión"
Verificar redirección a login
📚 Documentación Adicional
Estructura de Clases
Clase SistemaLogin
Atributos:

ventana: Ventana principal de Tkinter
archivo_usuarios: Ruta al archivo JSON
usuario_actual: Usuario actualmente autenticado
Métodos principales:

__init__(): Inicializa la aplicación
mostrar_inicio_sesion(): Muestra pantalla de login
mostrar_registro(): Muestra pantalla de registro
mostrar_home(): Muestra pantalla principal
validar_login(): Valida credenciales
procesar_registro(): Procesa nuevo registro
validar_contrasena(): Valida requisitos de contraseña
cargar_usuarios(): Carga usuarios desde JSON
guardar_usuario(): Guarda nuevo usuario en JSON
cerrar_sesion(): Cierra sesión actual
ejecutar(): Inicia el loop principal
🔐 Consideraciones de Seguridad
⚠️ IMPORTANTE: Este es un proyecto educativo. En un entorno de producción:

❌ NO guardes contraseñas en texto plano
✅ Usa hash con bcrypt o argon2
✅ Implementa HTTPS para comunicación
✅ Usa bases de datos seguras
✅ Implementa tokens de sesión
✅ Agrega autenticación de dos factores
✅ Implementa rate limiting
🤝 Contribuciones
Este es un proyecto académico, pero si deseas mejorarlo:

Fork el repositorio
Crea una rama (git checkout -b feature/mejora)
Commit tus cambios (git commit -m 'feat: agregar nueva funcionalidad')
Push a la rama (git push origin feature/mejora)
Abre un Pull Request
📝 Licencia
Este proyecto fue creado con fines educativos para el curso de Razonamiento Artificial de la Universidad Creativa de Costa Rica.

📞 Contacto
Estudiante: Pablo Arce Álvarez
Email: pablo.arcealvarez@ucreativa.com
Profesor: Angelo Ortiz Vega
Universidad: Universidad Creativa
🎯 Criterios de Evaluación Cumplidos
✅ Pantalla de inicio de sesión funcional
✅ Pantalla de registro con validaciones
✅ Pantalla home personalizada
✅ Validación de contraseñas robusta
✅ Persistencia en JSON
✅ Flujo de navegación completo
✅ Manejo de errores
✅ Interfaz gráfica intuitiva
✅ Documentación completa (README)
✅ Control de versiones con Git
🔄 Historial de Versiones
v1.0.0 (Octubre 2025)
✨ Implementación inicial del sistema
✨ Registro e inicio de sesión
✨ Persistencia en JSON
✨ Validaciones completas
