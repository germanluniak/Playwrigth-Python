from Test.Funciones.funciones_globales import Funciones_Globales
from Test.Fixtures.browser import browser, context, playwright, page
from Test.Config.config_loader import load_config_json

config = load_config_json('config.json')
URL = config['base_url']
archivo = config['file_paths']['path_archivo']


def test_Formulario_Contacto(playwright, page, context, browser) -> None:
    try:
        page.goto(URL)
        page.set_default_timeout(3000)
        F = Funciones_Globales(page)
        F.Validar_Elemento_Visible("(//div[@class='carousel-inner'])[1]")
        F.Click("//a[contains(.,'Contact us')]")
        F.Validar_Elemento_Visible("//h2[contains(.,'Contact Us')]")
        F.Completar_Formulario_Contacto("German", "prueba@prueba.com","Un asunto", "Un comentario", archivo)
        F.Esperar(5)
        context.close()
        browser.close()
        assert True
    except Exception as e:
        context.close()
        browser.close()
        assert False, f"Error: {str(e)}"


