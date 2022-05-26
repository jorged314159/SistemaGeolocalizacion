from behave import given, when, then
import time


@given(u'que presiono el boton Enfoque')
def step_impl(context):
    context.driver.find_element_by_link_text('Enfoque').click()
    time.sleep(0.5)
    

@given(u'después presiono el boton Nuevo')
def step_impl(context):
    context.driver.find_element_by_link_text('Nuevo').click()


@given(u'lleno el formulario con el nombre "{nombre}" y la descripción "{descripcion}"')
def step_impl(context, nombre, descripcion):
    context.driver.find_element_by_xpath('/html/body/div/div/div[3]/form/p[1]/input').send_keys(nombre)
    context.driver.find_element_by_xpath('/html/body/div/div/div[3]/form/p[2]/input').send_keys(descripcion)


@when(u'presiono el boton Agregar')
def step_impl(context):
    context.driver.find_element_by_xpath('/html/body/div/div/div[3]/form/input[2]').click()
    time.sleep(3)


@then(u'puedo ver la lista de enfoques y el nombre del enfoque que agregué "{nombre}".')
def step_impl(context, nombre):
    
    tabla = context.driver.find_element_by_tag_name('tbody')
        
    trs = tabla.find_elements_by_tag_name('tr')
    enfoques = []
    for tr in trs:
        tds = tr.find_elements_by_tag_name('td')
        enfoques.append(tds[0].text)
        
    assert nombre in enfoques
    
@then(u'puedo ver el mensaje de error "{esperado}".')
def step_impl(context, esperado):
    respuesta = context.driver.find_element_by_xpath('/html/body/div/div/div[3]/form/ul/li').text
    assert respuesta == esperado
    
