Característica: Eliminar un enfoque
    Como administrador quiero eliminar un enfoque
    para que ya no sea asignado a mas centros de investigacion

    Antecedentes: Inicio de sesión
    Dado que ingreso el usuario "jorgeD"
    Y la contraseña "jorgeRikudo"        
    Cuando presiono el boton Iniciar Sesión
    Entonces puedo ver en la página principal el mensaje "BIENVENIDO AL SISTEMA"


    Escenario: Eliminar datos
    Dado que me encuentro en la lista de enfoques y presiono el boton Eliminar del primer elemento de la lista
    Y aparece el mensaje de confirmación "¿Deseas eliminar el enfoque Quantum?"
    Cuando presiono el boton Eliminar
    Entonces me redirije a la lista de enfoques y puedo ver el mensaje "Se eliminó con éxito".

    Escenario: Eliminacion fallida
    Dado que me encuentro en la lista de enfoques y presiono el boton Eliminar del primer elemento de la lista
    Y aparece el mensaje de confirmación "¿Deseas eliminar el enfoque Ciencias basicas?"
    Y además este enfoque tiene algun centro de investigacion asociado
    Cuando presiono el boton Eliminar
    Entonces me redirije a la lista de enfoques y puedo ver el mensaje de error "No se puede eliminar el enfoque, tiene centros de investigacion agregados".