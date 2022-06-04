from behave import given, when, then
import time

@given(u'que me encuentro en la lista de enfoques y presiono el boton Eliminar del primer elemento de la lista')
def step_impl(context):
    context.driver.get(context.url + '/enfoques')
    context.driver.find_element_by_xpath('/html/body/div/div/div[3]/table/tbody/tr[1]/td[3]/a[2]').click()


@given(u'que me encuentro en la lista de enfoques y presiono el boton Eliminar del segundo elemento de la lista')
def step_impl(context):
    context.driver.get(context.url + '/enfoques')
    context.driver.find_element_by_xpath('/html/body/div/div/div[3]/table/tbody/tr[2]/td[3]/a[2]').click()


@given(u'aparece el mensaje de confirmación "{esperado}"')
def step_impl(context, esperado):
    respuesta = context.driver.find_element_by_xpath('/html/body/div/div/div[3]/form/p').text
    assert esperado in respuesta
    

@when(u'presiono el boton Eliminar')
def step_impl(context):
    context.driver.find_element_by_xpath('/html/body/div/div/div[3]/form/input[2]').click()


@then(u'me redirije a la lista de enfoques y puedo ver el mensaje "{esperado}".')
def step_impl(context, esperado):
    respuesta = context.driver.find_element_by_xpath('/html/body/div/div/div[3]/div').text
    assert esperado in respuesta
    
@given(u'además este enfoque tiene algun centro de investigacion asociado')
def step_impl(context):
    pass


@then(u'me redirije a la lista de enfoques y puedo ver el mensaje de error "{esperado}".')
def step_impl(context, esperado):
    respuesta = context.driver.find_element_by_xpath('/html/body/div/div/div[3]/div').text
    assert esperado in respuesta