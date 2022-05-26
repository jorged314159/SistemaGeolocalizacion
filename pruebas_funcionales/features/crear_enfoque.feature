Característica: Dar de alta Enfoque
    Como administrador quiero dar de alta un Enfoque
    para posteriormente poder asignarlo a algún centro de investigacion

    Antecedentes: Inicio de sesión
    Dado que ingreso el usuario "jorgeD"
    Y la contraseña "jorgeRikudo"
    Cuando presiono el boton Iniciar Sesión
    Entonces puedo ver en la página principal el mensaje "BIENVENIDO AL SISTEMA"

    Escenario: Datos correctos
    Dado que presiono el boton Enfoque
    Y después presiono el boton Nuevo
    Y lleno el formulario con el nombre "Quantum" y la descripción "Hacen ciencia segun esto"
    Cuando presiono el boton Agregar
    Entonces puedo ver la lista de enfoques y el nombre del enfoque que agregué "Quantum".

    Escenario: Datos duplicados
    Dado que presiono el boton Enfoque
    Y después presiono el boton Nuevo
    Y lleno el formulario con el nombre "Quantum" y la descripción "existe algo"
    Cuando presiono el boton Agregar
    Entonces puedo ver el mensaje de error "Ya existe un/a Enfoque con este/a Nombre.".
