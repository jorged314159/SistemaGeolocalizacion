Característica: Login del sistema
    Como administrador
    requiero iniciar sesion en el Sistema de Geolocalizacion
    para realizar las actividades correspondientes

    Escenario: Credenciales validas
    Dado que ingreso el usuario "alexdlcruz" 
    Y la contraseña "36172889"
    Cuando presiono el boton Iniciar Sesión
    Entonces puedo ver en la página principal el mensaje "BIENVENIDO AL SISTEMA"

    Escenario: Credenciales no validas
    Dado que ingreso el usuario "jorge" 
    Y la contraseña "jorgeRikudo"
    Cuando presiono el boton Iniciar Sesión
    Entonces aparece el mensaje de error "Datos de inicio de sesión incorrectos"