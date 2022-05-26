from behave import given, then, when
import time

@given(u'que presiono el boton de la izquierda Centro de Investigación')
def step_impl(context):
    context.driver.find_element_by_link_text('Centro de Investigación').click()
    time.sleep(0.5)

@given(u'después al boton Lista')
def step_impl(context):
    context.driver.find_element_by_xpath('//*[@id="sidebar-menu"]/div/ul/li[1]/ul/li[1]/a').click()

@given(u'luego le doy click al boton Editar del primer elemento de la lista')
def step_impl(context):
    context.driver.find_element_by_xpath('/html/body/div/div/div[3]/table/tbody/tr/td[7]/a[1]').click()

@given(u'modifico el nombre del centro de investigación a "{nombre}"')
def step_impl(context, nombre):
    context.driver.find_element_by_xpath('//*[@id = "id_nombre"]').clear()
    context.driver.find_element_by_xpath('//*[@id = "id_nombre"]').send_keys(nombre)

@when(u'presiono el boton Guardar')
def step_impl(context):
    context.driver.find_element_by_xpath('/html/body/div/div/div[3]/form/input[2]').click()

@then(u'puedo ver la lista actualizada de los centros de investigación.')
def step_impl(context):
    context.driver.get(context.url + '/centros')