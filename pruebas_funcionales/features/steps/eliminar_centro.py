from behave import given, then, when
import time

@given(u'que presiono el boton que dice Centro de Investigación')
def step_impl(context):
    context.driver.find_element_by_link_text('Centro de Investigación').click()
    time.sleep(0.5)

@given(u'luego presiono al boton Lista')
def step_impl(context):
    context.driver.find_element_by_xpath('//*[@id="sidebar-menu"]/div/ul/li[1]/ul/li[1]/a').click()

@when(u'le doy click al boton Eliminar al primer elemento de la lista')
def step_impl(context):
    context.driver.find_element_by_xpath('/html/body/div/div/div[3]/table/tbody/tr[1]/td[7]/a[2]').click()

@then(u'el sistema me muestra la lista actualizada de los centros de investigación.')
def step_impl(context):
    context.driver.get(context.url + '/centros')
    