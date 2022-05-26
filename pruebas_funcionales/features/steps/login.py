from behave import given, when, then


@given(u'que ingreso el usuario "{usuario}"')
def step_impl(context, usuario):
    context.driver.get(context.url + '/usuarios/entrar')
    context.driver.find_element_by_xpath('/html/body/div/div/div/section/form/div[1]/input').send_keys(usuario)


@given(u'la contraseña "{contrasena}"')
def step_impl(context, contrasena):
    context.driver.find_element_by_xpath('/html/body/div/div/div/section/form/div[2]/input').send_keys(contrasena)


@when(u'presiono el boton Iniciar Sesión')
def step_impl(context):
    context.driver.find_element_by_xpath('/html/body/div/div/div/section/form/div[3]/button').click()


@then(u'puedo ver en la página principal el mensaje "{esperado}"')
def step_impl(context, esperado):
    respuesta = context.driver.find_element_by_xpath('/html/body/div/div/div[3]/h1').text
    assert respuesta == esperado


@then(u'aparece el mensaje de error "{esperado}"')
def step_impl(context, esperado):
    respuesta = context.driver.find_element_by_xpath('/html/body/div/div/div/section/div').text
    assert esperado in respuesta