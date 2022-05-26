from selenium.webdriver.support.ui import Select
from behave import given, then, when
import time

@given(u'que presiono el boton Centro de Investigación')
def step_impl(context):
    context.driver.find_element_by_link_text('Centro de Investigación').click()
    time.sleep(0.5)


@given(u'luego presiono el boton Nuevo')
def step_impl(context):
    context.driver.find_element_by_link_text('Nuevo').click()


@given(u'lleno el formulario con el nombre "{nombre}", dirección "{direccion}" , latitud "{latitud}", longitud "{longitud}", telefono "{telefono}" y le asigno un Enfoque')
def step_impl(context, nombre, direccion, latitud, longitud, telefono):
    context.driver.find_element_by_xpath('/html/body/div/div/div[3]/form/p[1]/input').send_keys(nombre)
    context.driver.find_element_by_xpath('/html/body/div/div/div[3]/form/p[2]/input').send_keys(direccion)
    context.driver.find_element_by_xpath('/html/body/div/div/div[3]/form/p[3]/input').send_keys(latitud)
    context.driver.find_element_by_xpath('/html/body/div/div/div[3]/form/p[4]/input').send_keys(longitud)
    context.driver.find_element_by_xpath('/html/body/div/div/div[3]/form/p[5]/input').send_keys(telefono)
    context.driver.find_element_by_xpath('/html/body/div/div/div[3]/form/p[6]/select').click()
    time.sleep(1)
    context.driver.find_element_by_xpath('//*[@id="id_enfoque"]/option[2]').click()
        
@when(u'presiono el boton verde de Agregar')
def step_impl(context):
    context.driver.find_element_by_xpath('/html/body/div/div/div[3]/form/input[2]').click()
    time.sleep(5)


@then(u'puedo ver la lista de centros de investigación y el nombre del que agregué "{nombre}".')
def step_impl(context, nombre):
    tabla = context.driver.find_element_by_tag_name('tbody')

    trs = tabla.find_elements_by_tag_name('tr')
    centros = []
    for tr in trs:
        tds = tr.find_elements_by_tag_name('td')
        centros.append(tds[0].text)

    assert nombre in centros

@then(u'me indica con un mensaje que "{esperado}"')
def step_impl(context, esperado):
    respuesta = context.driver.find_element_by_xpath('/html/body/div/div/div[3]/form/ul/li').text
    assert esperado in respuesta