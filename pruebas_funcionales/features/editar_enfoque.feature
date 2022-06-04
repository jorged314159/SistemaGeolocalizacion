Característica: Editar informacion de un enfoque
    Como administrador quiero editar el nombre de un enfoque
    para mantener los datos actualizados

    Antecedentes: Inicio de sesión
    Dado que ingreso el usuario "alexdlcruz"
    Y la contraseña "36172889"        
    Cuando presiono el boton Iniciar Sesión
    Entonces puedo ver en la página principal el mensaje "BIENVENIDO AL SISTEMA"


    Escenario: Editar datos
    Dado que me encuentro en la lista de enfoques y presiono el boton Editar del primer elemento de la lista
    Y cambio el nombre del enfoque a "TICS" y la descripción "les dan tocs"
    Cuando presiono el boton Guardar
    Entonces puedo ver en la lista el nuevo nombre asignado "TICS"