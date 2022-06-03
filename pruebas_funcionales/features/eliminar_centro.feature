Característica: Eliminar un centro de investigación de una lista
    Yo como administrador quiero eliminar un centro de investigación cuando ya no sea requerido.

    Antecedentes: Inicio de sesión
    Dado que ingreso el usuario "jorgeD"
    Y la contraseña "jorgeRikudo"
    Cuando presiono el boton Iniciar Sesión
    Entonces puedo ver en la página principal el mensaje "BIENVENIDO AL SISTEMA"

    Escenario: Eliminación correcta
    Dado que presiono el boton que dice Centro de Investigación
    Y luego presiono al boton Lista
    Cuando le doy click al boton Eliminar al primer elemento de la lista
    Entonces el sistema me muestra la lista actualizada de los centros de investigación.