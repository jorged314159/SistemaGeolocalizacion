Característica: Crear cuenta de admin
    Yo como administrador quiero poder crear una cuenta para acceder al sistema y así administrarlo.

    Escenario: Datos válidos
    Dado que estoy en la ventana del login
    Y presiono el boton Registrarse
    Y lleno el formulario con los siguientes datos nombre "alejandro", correo "alex@hotmail.com", contraseña "alex1234" y la confirmación de contraseña "alex1234"  
    Cuando presiono el boton Registrar
    Entonces me reedirige a la página de login

    Escenario: Datos repetidos
    Dado que estoy en la ventana del login
    Y presiono el boton Registrarse
    Y lleno el formulario con los siguientes datos nombre "alejandro", correo "alex@hotmail.com", contraseña "jorgeRikudo" y la confirmación de contraseña "jorgeRikudo"
    Cuando presiono el boton Registrar
    Entonces me muestra el mensaje "Ya existe un usuario con ese nombre."