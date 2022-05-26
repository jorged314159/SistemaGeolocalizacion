from behave import given, when, then
import time

@given(u'que estoy en la ventana del login')
def step_impl(context):
    context.driver.get(context.url + '/usuarios/entrar')
    context.driver.find_element_by_xpath('/html/body/div/div/div/section/form/h1').text
    time.sleep(5)


@given(u'presiono el boton Registrarse')
def step_impl(context):
    context.driver.find_element_by_xpath('/html/body/div/div/div/section/form/div[5]/p/a').click()
    time.sleep(5)

@given(u'lleno el formulario con los siguientes datos nombre "{nombre}", correo "{email}", contraseña "{contra}" y la confirmación de contraseña "{conf_contra}"')
def step_impl(context, nombre, email, contra, conf_contra):
    context.driver.get(context.url + '/usuarios/registrar')
    context.driver.find_element_by_xpath('/html/body/div/div/div/section/form/div[1]/input').send_keys(nombre)
    context.driver.find_element_by_xpath('/html/body/div/div/div/section/form/div[2]/input').send_keys(email)
    context.driver.find_element_by_xpath('/html/body/div/div/div/section/form/div[3]/input').send_keys(contra)
    context.driver.find_element_by_xpath('/html/body/div/div/div/section/form/div[4]/input').send_keys(conf_contra)


@when(u'presiono el boton Registrar')
def step_impl(context):
    context.driver.find_element_by_xpath('/html/body/div/div/div/section/form/div[5]/button').click()
    time.sleep(5)

@then(u'me reedirige a la página de login')
def step_impl(context):
    # context.driver.get(context.url + '/usuarios/entrar')
    context.driver.find_element_by_xpath('/html/body/div/div/div/section/form/h1').text
    time.sleep(5)


@then(u'me muestra el mensaje "{esperado}"')
def step_impl(context, esperado):
    respuesta = context.driver.find_element_by_xpath('/html/body/div/div/div/section/div').text
    assert esperado in respuesta