from Test.Funciones.funciones_globales import Funciones_Globales
from Test.Fixtures.browser import browser, context, playwright, page
from Test.Config.config_loader import load_config_json
from Test.Utils.handle_error import handle_error

config = load_config_json('config.json')
URL = config['base_url']

def test_Registrar_Usuario(playwright, page, context, browser) -> None:
    try:
        page.goto(URL)
        page.set_default_timeout(3000)
        F = Funciones_Globales(page)
        Email = F.generate_random_email()
        F.Validar_Elemento_Visible("(//div[@class='carousel-inner'])[1]")
        F.Click("//a[contains(.,'Signup / Login')]")
        F.Validar_Elemento_Visible("//h2[contains(.,'Login to your account')]")
        F.Set_Texto("//input[@name='name']", "Juan")
        F.Set_Texto("(//input[@name='email'])[2]", Email)
        F.Click("//button[contains(.,'Signup')]")
        F.Validar_Elemento_Visible("//b[contains(.,'Enter Account Information')]")
        F.Click("//input[@value='Mr']")
        F.Set_Texto("//input[@name='password']", "prueba")
        F.Select_Fecha("17", "7", "1986")
        F.Click("//input[@name='newsletter']")
        F.Click("//input[@name='optin']")
        F.Completar_Formulario("juan", "perez", "test inc", "direccion 1", "direccion 2", "Canada", "Quebec", "Montreal", "1000", "3442445566")
        F.Click("//button[contains(.,'Create Account')]")
        F.Validar_Elemento_Visible("//b[contains(.,'Account Created!')]")
        F.Click("//a[contains(.,'Continue')]")
        F.Validar_Elemento_Visible("//a[contains(.,'Logged in as juan')]")
        F.Click("//a[contains(.,'Delete Account')]")
        F.Validar_Elemento_Visible("//b[contains(.,'Account Deleted!')]")
        context.close()
        browser.close()
        assert True
    except Exception as e:
        context.close()
        browser.close()
        assert False, f"Error: {str(e)}"

def test_Logearse(playwright, page, context, browser) -> None:
    try:
        page.goto(URL)
        page.set_default_timeout(3000)
        F = Funciones_Globales(page)
        F.Validar_Elemento_Visible("(//div[@class='carousel-inner'])[1]")
        F.Click("//a[contains(.,'Signup / Login')]")
        F.Validar_Elemento_Visible("//h2[contains(.,'Login to your account')]")
        F.Set_Texto("(//input[@name='email'])[1]", "pruebas@pruebas.com")
        F.Set_Texto("//input[@name='password']", "prueba")
        F.Click("//button[contains(.,'Login')]")
        F.Validar_Elemento_Visible("//a[contains(.,'Logged in as german')]")
        context.close()
        browser.close()
        assert True
    except Exception as e:
        context.close()
        browser.close()
        assert False, f"Error: {str(e)}"

def test_Error_Login(playwright, page, context, browser) -> None:
    try:
        page.goto(URL)
        page.set_default_timeout(3000)
        F = Funciones_Globales(page)
        F.Validar_Elemento_Visible("(//div[@class='carousel-inner'])[1]")
        F.Click("//a[contains(.,'Signup / Login')]")
        F.Validar_Elemento_Visible("//h2[contains(.,'Login to your account')]")
        F.Set_Texto("(//input[@name='email'])[1]", "pruebas@pruebas.com")
        F.Set_Texto("//input[@name='password']", "pruebas")
        F.Click("//button[contains(.,'Login')]")
        F.Validar_Elemento_Visible("//p[contains(.,'Your email or password is incorrect!')]")
        context.close()
        browser.close()
        assert True
    except Exception as e:
        context.close()
        browser.close()
        assert False, f"Error: {str(e)}"

def test_Deslogearse(playwright, page, context, browser) -> None:
    try:
        page.goto(URL)
        page.set_default_timeout(3000)
        F = Funciones_Globales(page)
        F.Validar_Elemento_Visible("(//div[@class='carousel-inner'])[1]")
        F.Click("//a[contains(.,'Signup / Login')]")
        F.Validar_Elemento_Visible("//h2[contains(.,'Login to your account')]")
        F.Set_Texto("(//input[@name='email'])[5]", "pruebas@pruebas.com")
        F.Set_Texto("//input[@name='password']", "prueba")
        F.Click("//button[contains(.,'Login')]")
        F.Validar_Elemento_Visible("//a[contains(.,'Logged in as german')]")
        F.Esperar(3)
        F.Click("//a[contains(.,'Logout')]")
        F.Validar_Elemento_Visible("//h2[contains(.,'Login to your account')]")
        context.close()
        browser.close()
        assert True
    except Exception as e:
        handle_error(page, context, browser, str(e))

def test_Registrar_Usuario_Registrado(playwright, page, context, browser) -> None:
    try:
        page.goto(URL)
        page.set_default_timeout(3000)
        F = Funciones_Globales(page)
        F.Validar_Elemento_Visible("(//div[@class='carousel-inner'])[1]")
        F.Click("//a[contains(.,'Signup / Login')]")
        F.Validar_Elemento_Visible("//h2[contains(.,'Login to your account')]")
        F.Set_Texto("//input[@name='name']", "german")
        F.Set_Texto("(//input[@name='email'])[2]", "prueba@prueba.com")
        F.Click("//button[contains(.,'Signup')]")
        F.Validar_Elemento_Visible("//p[contains(.,'Email Address already exist!')]")
        context.close()
        browser.close()
        assert True
    except Exception as e:
        context.close()
        browser.close()
        assert False, f"Error: {str(e)}"


