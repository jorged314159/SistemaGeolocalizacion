Característica: Modificar los datos de un centro de investigación
    Yo como administrador quiero modificar la información de un centro de investigación 
    para que esta se mantenga de manera actualizada.

    Antecedentes: Inicio de sesión
    Dado que ingreso el usuario "alexdlcruz"
    Y la contraseña "36172889"
    Cuando presiono el boton Iniciar Sesión
    Entonces puedo ver en la página principal el mensaje "BIENVENIDO AL SISTEMA"

    Escenario: Modificación correcta
    Dado que presiono el boton de la izquierda Centro de Investigación
    Y después al boton Lista
    Y luego le doy click al boton Editar del primer elemento de la lista
    Y modifico el nombre del centro de investigación a "Software"
    Cuando presiono el boton Guardar
    Entonces puedo ver la lista actualizada de los centros de investigación.