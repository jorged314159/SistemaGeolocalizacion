Característica: Crear un centro de investigación
    Yo como administrador quiero agregar un nuevo centro de investigación en la base de datos para que 
    pueda ser vista posteriormente en el mapa y pueda ser ubicado.

    Antecedentes: Inicio de sesión
    Dado que ingreso el usuario "alexdlcruz"
    Y la contraseña "36172889"
    Cuando presiono el boton Iniciar Sesión
    Entonces puedo ver en la página principal el mensaje "BIENVENIDO AL SISTEMA"

    Escenario: Datos correctos
    Dado que presiono el boton Centro de Investigación
    Y luego presiono el boton Nuevo
    Y lleno el formulario con el nombre "Hola", dirección "Cara 20, Soles, 98000, Guadalupe" , latitud "22.64646", longitud "23.95611", telefono "4921234567" y le asigno un Enfoque
    Cuando presiono el boton verde de Agregar
    Entonces puedo ver la lista de centros de investigación y el nombre del que agregué "Hola".

    Escenario: Datos duplicados
    Dado que presiono el boton Centro de Investigación
    Y luego presiono el boton Nuevo
    Y lleno el formulario con el nombre "UAZ", dirección "Muy lejos 10, Pero Lejos, 98612, Guadalupe" , latitud "21.64646", longitud "22.95611", telefono "4921234568" y le asigno un Enfoque
    Cuando presiono el boton verde de Agregar
    Entonces me indica con un mensaje que "Ya existe un/a Centro investigacion con este/a Nombre."