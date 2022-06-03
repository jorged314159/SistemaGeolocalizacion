from behave import given, when, then
import time


@given(u'que me encuentro en la lista de enfoques y presiono el boton Editar del primer elemento de la lista')
def step_impl(context):
    context.driver.get(context.url + '/enfoques')
    context.driver.find_element_by_xpath('/html/body/div/div/div[3]/table/tbody/tr[1]/td[3]/a[1]').click()
    


@given(u'cambio el nombre del enfoque a "{nombre}" y la descripción "{desc}"')
def step_impl(context, nombre, desc):
    context.driver.find_element_by_name('nombre').clear()
    context.driver.find_element_by_name('nombre').send_keys(nombre)
    context.driver.find_element_by_name('descripcion').clear()
    context.driver.find_element_by_name('descripcion').send_keys(desc)
    


@when(u'presiono el boton Guardar')
def step_impl(context):
    context.driver.find_element_by_xpath('/html/body/div/div/div[3]/form/input[2]').click()
    time.sleep(5)


@then(u'puedo ver en la lista el nuevo nombre asignado "{esperado}"')
def step_impl(context, esperado):
    tabla = context.driver.find_element_by_tag_name('tbody')
    trs = tabla.find_elements_by_tag_name('tr')
    enfoques2 = []
    for tr in trs:
        tds = tr.find_elements_by_tag_name('td')
        enfoques2.append(tds[0].text)
        
    assert esperado in enfoques2