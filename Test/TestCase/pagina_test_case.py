from Test.Funciones.funciones_globales import Funciones_Globales
from Test.Fixtures.browser import browser, context, playwright, page
from Test.Config.config_loader import load_config_json

config = load_config_json('config.json')
URL = config['base_url']

def test_Pageina_Test_Case(playwright, page, context, browser) -> None:
    try:
        page.goto(URL)
        page.set_default_timeout(3000)
        F = Funciones_Globales(page)
        F.Validar_Elemento_Visible("(//div[@class='carousel-inner'])[1]")
        F.Click("(//button[contains(.,'Test Cases')])[1]")
        F.Validar_Elemento_Visible("//b[contains(.,'Test Cases')]")
        F.Esperar(5)
        context.close()
        browser.close()
        assert True
    except Exception as e:
        context.close()
        browser.close()
        assert False, f"Error: {str(e)}"


