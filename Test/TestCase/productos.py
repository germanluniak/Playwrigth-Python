from Test.Funciones.funciones_globales import Funciones_Globales
from Test.Fixtures.browser import browser, context, playwright, page
from Test.Config.config_loader import load_config_json

config = load_config_json('config.json')
URL = config['base_url']
path_download = config['file_paths']['path_download']
lista_productos = []


def test_Validar_Productos(playwright, page, context, browser) -> None:
    try:
        page.goto(URL)
        page.set_default_timeout(3000)
        F = Funciones_Globales(page)
        F.Validar_Elemento_Visible("(//div[@class='carousel-inner'])[1]")
        F.Click("//a[contains(.,' Products')]")
        F.Validar_Elemento_Visible("//h2[contains(.,'All Products')]")
        F.Click("(//a[contains(.,'View Product')])[1]")
        F.Validar_Elemento_Visible("(//a[contains(.,'View Product')])[1]")
        F.Validar_Elemento_Visible("//p[contains(.,'Category: Women > Tops')]")
        F.Validar_Elemento_Visible("(//span[contains(.,'Rs. 500')])[2]")
        F.Validar_Elemento_Visible("//p[contains(.,'Availability: In Stock')]")
        F.Validar_Elemento_Visible("//p[contains(.,'Condition: New')]")
        F.Validar_Elemento_Visible("//p[contains(.,'Brand: Polo')]")
        F.Esperar(5)
        context.close()
        browser.close()
        assert True
    except Exception as e:
        context.close()
        browser.close()
        assert False, f"Error: {str(e)}"

def test_Buscar_Producto(playwright, page, context, browser) -> None:
    try:
        page.goto(URL)
        page.set_default_timeout(3000)
        F = Funciones_Globales(page)
        F.Validar_Elemento_Visible("(//div[@class='carousel-inner'])[1]")
        F.Click("//a[contains(.,' Products')]")
        F.Validar_Elemento_Visible("//h2[contains(.,'All Products')]")
        F.Set_Texto("//input[@id='search_product']","Premium Polo T-Shirts")
        F.Click("//i[@class='fa fa-search']")
        F.Validar_Elemento_Visible("//h2[contains(.,'Searched Products')]")
        F.Validar_Texto("//p[contains(.,'Premium Polo T-Shirts')]", "Premium Polo T-Shirts")
        F.Esperar(5)
        context.close()
        browser.close()
        assert True
    except Exception as e:
        context.close()
        browser.close()
        assert False, f"Error: {str(e)}"

def test_Validar_Suscripcion_Home(playwright, page, context, browser) -> None:
    try:
        page.goto(URL)
        page.set_default_timeout(3000)
        F = Funciones_Globales(page)
        F.Validar_Elemento_Visible("(//div[@class='carousel-inner'])[1]")
        F.Desplazar_Hasta_Elemento("//h2[contains(.,'Subscription')]")
        F.Set_Texto("//input[@id='susbscribe_email']","prueba@prueba.com")
        F.Click("//i[@class='fa fa-arrow-circle-o-right']")
        F.Validar_Elemento_Visible("(//div[contains(.,'You have been successfully subscribed!')])[6]")
        F.Esperar(5)
        context.close()
        browser.close()
        assert True
    except Exception as e:
        context.close()
        browser.close()
        assert False, f"Error: {str(e)}"

def test_Validar_Suscripcion_Carrito(playwright, page, context, browser) -> None:
    try:
        page.goto(URL)
        page.set_default_timeout(3000)
        F = Funciones_Globales(page)
        F.Validar_Elemento_Visible("(//div[@class='carousel-inner'])[1]")
        F.Click("(//a[contains(.,'Cart')])[1]")
        F.Desplazar_Hasta_Elemento("//h2[contains(.,'Subscription')]")
        F.Set_Texto("//input[@id='susbscribe_email']","prueba@prueba.com")
        F.Click("//i[@class='fa fa-arrow-circle-o-right']")
        F.Validar_Elemento_Visible("(//div[contains(.,'You have been successfully subscribed!')])[6]")
        F.Esperar(5)
        context.close()
        browser.close()
        assert True
    except Exception as e:
        context.close()
        browser.close()
        assert False, f"Error: {str(e)}"

def test_Agregar_Producto_Carrito(playwright, page, context, browser) -> None:
    try:
        page.goto(URL)
        page.set_default_timeout(3000)
        F = Funciones_Globales(page)
        F.Validar_Elemento_Visible("(//div[@class='carousel-inner'])[1]")
        F.Click("//a[contains(.,' Products')]")
        F.Validar_Elemento_Visible("//h2[contains(.,'All Products')]")
        F.Agregar_Producto_Carrito(1)
        F.Click("//button[contains(.,'Continue Shopping')]")
        nombre1 = F.GetNombre("(//div[@class='productinfo text-center']//p)[1]")
        precio1 = F.GetPrecio("(//div[@class='productinfo text-center']//h2)[1]")
        F.Agregar_Producto_Carrito(3)
        nombre2 = F.GetNombre("(//div[@class='productinfo text-center']//p)[2]")
        precio2 = F.GetPrecio("(//div[@class='productinfo text-center']//h2)[2]")
        F.Click("//u[contains(.,'View Cart')]")
        F.Verificar_Producto_Carrito(1, nombre1, precio1, 1)
        F.Verificar_Producto_Carrito(2, nombre2, precio2, 1)
        total_esperado = precio1 + precio2
        total_en_carrito = F.GetTotal(2)
        assert total_en_carrito == total_esperado, f"Total esperado: {total_esperado}, encontrado: {total_en_carrito}"
        F.Esperar(5)
        context.close()
        browser.close()
        assert True
    except Exception as e:
        context.close()
        browser.close()
        assert False, f"Error: {str(e)}"

def test_Verificar_Cantidad_Producto_Carrito(playwright, page, context, browser) -> None:
    try:
        cantidad_unidades = "4"
        page.goto(URL)
        page.set_default_timeout(3000)
        F = Funciones_Globales(page)
        F.Validar_Elemento_Visible("(//div[@class='carousel-inner'])[1]")
        F.Click("//a[contains(.,' Products')]")
        F.Validar_Elemento_Visible("//h2[contains(.,'All Products')]")
        F.Click("(//a[contains(.,'View Product')])[1]")
        F.Set_Texto("//input[@id='quantity']", cantidad_unidades)
        F.Click("//button[contains(.,'Add to cart')]")
        nombre1 = F.GetNombre("(//div[@class='product-information']//h2)[1]")
        precio1 = F.GetPrecio("(//div[@class='product-information']//span)[2]")
        F.Click("//u[contains(.,'View Cart')]")
        F.Verificar_Producto_Carrito(1, nombre1, precio1, 4)
        total_esperado = precio1 * int(cantidad_unidades)
        total_en_carrito = F.GetTotal(1)
        assert total_en_carrito == total_esperado, f"Total esperado: {total_esperado}, encontrado: {total_en_carrito}"
        F.Esperar(5)
        context.close()
        browser.close()
        assert True
    except Exception as e:
        context.close()
        browser.close()
        assert False, f"Error: {str(e)}"

def test_Realizar_Pedido(playwright, page, context, browser) -> None:
    try:
        page.goto(URL)
        page.set_default_timeout(3000)
        F = Funciones_Globales(page)
        Email = F.generate_random_email()
        nombre = "juan"
        apellido = "perez"
        compania = "test inc"
        direccion1 = "direccion 1"
        direccion2 = "direccion 2"
        pais = "Canada"
        estado = "Quebec"
        ciudad = "Montreal"
        cp = "1000"
        telefono = "3442445566"
        F.Validar_Elemento_Visible("(//div[@class='carousel-inner'])[1]")
        F.Click("//a[contains(.,' Products')]")
        F.Validar_Elemento_Visible("//h2[contains(.,'All Products')]")
        F.Agregar_Producto_Carrito(1)
        F.Click("//button[contains(.,'Continue Shopping')]")
        nombre1 = F.GetNombre("(//div[@class='productinfo text-center']//p)[1]")
        precio1 = F.GetPrecio("(//div[@class='productinfo text-center']//h2)[1]")
        F.Agregar_Producto_Carrito(3)
        nombre2 = F.GetNombre("(//div[@class='productinfo text-center']//p)[2]")
        precio2 = F.GetPrecio("(//div[@class='productinfo text-center']//h2)[2]")
        F.Click("(//a[contains(.,'Cart')])[1]")
        F.Click("//a[contains(.,'Proceed To Checkout')]")
        F.Click("//u[contains(.,'Register / Login')]")
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
        F.Completar_Formulario(nombre, apellido, compania, direccion1, direccion2, pais, estado, ciudad, cp, telefono)
        F.Click("//button[contains(.,'Create Account')]")
        F.Validar_Elemento_Visible("//b[contains(.,'Account Created!')]")
        F.Click("(//a[contains(.,'Cart')])[1]")
        F.Click("//a[contains(.,'Proceed To Checkout')]")
        F.Validar_Elemento_Visible("//h2[contains(.,'Address Details')]")
        F.Validar_Informacion_Entrega(nombre, apellido, compania, direccion1, direccion2, pais, estado, ciudad, cp, telefono)
        F.Verificar_Producto_Carrito(1, nombre1, precio1, 1)
        F.Verificar_Producto_Carrito(2, nombre2, precio2, 1)
        total_esperado = precio1 + precio2
        total_en_carrito = F.GetTotal(2)
        assert total_en_carrito == total_esperado, f"Total esperado: {total_esperado}, encontrado: {total_en_carrito}"
        F.Set_Texto("//textarea[@name='message']", "dejo un comentario")
        F.Click("//a[contains(.,'Place Order')]")
        F.CargarDatosTarjeta()
        F.Click("//button[contains(.,'Pay and Confirm Order')]")
        F.Validar_Elemento_Visible("(//div[contains(.,'Your order has been placed successfully!')])[7]")
        F.Validar_Elemento_Visible("//b[contains(.,'Order Placed!')]")
        F.Validar_Texto("(//div[@class='container']//p)[1]", "Congratulations! Your order has been confirmed!")
        F.Click("//a[contains(.,'Continue')]")
        F.Click("//a[contains(.,'Delete Account')]")
        F.Validar_Elemento_Visible("//b[contains(.,'Account Deleted!')]")
        F.Click("//a[contains(.,'Continue')]")
        F.Esperar(5)
        context.close()
        browser.close()
        assert True
    except Exception as e:
        context.close()
        browser.close()
        assert False, f"Error: {str(e)}"

def test_Realizar_Pedido_Registrado(playwright, page, context, browser) -> None:
    try:
        page.goto(URL)
        page.set_default_timeout(3000)
        F = Funciones_Globales(page)
        Email = F.generate_random_email()
        nombre = "juan"
        apellido = "perez"
        compania = "test inc"
        direccion1 = "direccion 1"
        direccion2 = "direccion 2"
        pais = "Canada"
        estado = "Quebec"
        ciudad = "Montreal"
        cp = "1000"
        telefono = "3442445566"
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
        F.Completar_Formulario(nombre, apellido, compania, direccion1, direccion2, pais, estado, ciudad, cp, telefono)
        F.Click("//button[contains(.,'Create Account')]")
        F.Validar_Elemento_Visible("//b[contains(.,'Account Created!')]")
        F.Click("//a[contains(.,' Products')]")
        F.Validar_Elemento_Visible("//h2[contains(.,'All Products')]")
        F.Agregar_Producto_Carrito(1)
        F.Click("//button[contains(.,'Continue Shopping')]")
        nombre1 = F.GetNombre("(//div[@class='productinfo text-center']//p)[1]")
        precio1 = F.GetPrecio("(//div[@class='productinfo text-center']//h2)[1]")
        F.Agregar_Producto_Carrito(3)
        nombre2 = F.GetNombre("(//div[@class='productinfo text-center']//p)[2]")
        precio2 = F.GetPrecio("(//div[@class='productinfo text-center']//h2)[2]")
        F.Click("(//a[contains(.,'Cart')])[1]")
        F.Click("//a[contains(.,'Proceed To Checkout')]")
        F.Validar_Elemento_Visible("//h2[contains(.,'Address Details')]")
        F.Validar_Informacion_Entrega(nombre, apellido, compania, direccion1, direccion2, pais, estado, ciudad, cp, telefono)
        F.Verificar_Producto_Carrito(1, nombre1, precio1, 1)
        F.Verificar_Producto_Carrito(2, nombre2, precio2, 1)
        total_esperado = precio1 + precio2
        total_en_carrito = F.GetTotal(2)
        assert total_en_carrito == total_esperado, f"Total esperado: {total_esperado}, encontrado: {total_en_carrito}"
        F.Set_Texto("//textarea[@name='message']", "dejo un comentario")
        F.Click("//a[contains(.,'Place Order')]")
        F.CargarDatosTarjeta()
        F.Click("//button[contains(.,'Pay and Confirm Order')]")
        F.Validar_Elemento_Visible("(//div[contains(.,'Your order has been placed successfully!')])[7]")
        F.Validar_Elemento_Visible("//b[contains(.,'Order Placed!')]")
        F.Validar_Texto("(//div[@class='container']//p)[1]", "Congratulations! Your order has been confirmed!")
        F.Validar_Descarga("//a[contains(.,'Download Invoice')]")
        F.Click("//a[contains(.,'Continue')]")
        F.Click("//a[contains(.,'Delete Account')]")
        F.Validar_Elemento_Visible("//b[contains(.,'Account Deleted!')]")
        F.Click("//a[contains(.,'Continue')]")
        F.Esperar(5)
        context.close()
        browser.close()
        assert True
    except Exception as e:
        context.close()
        browser.close()
        assert False, f"Error: {str(e)}"

def test_Realizar_Pedido_Logeado(playwright, page, context, browser) -> None:
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
        F.Click("//a[@href='/products']")
        F.Esperar(2)
        F.Validar_Elemento_Visible("//h2[contains(.,'All Products')]")
        F.Agregar_Producto_Carrito(1)
        F.Click("//button[contains(.,'Continue Shopping')]")
        nombre1 = F.GetNombre("(//div[@class='productinfo text-center']//p)[1]")
        precio1 = F.GetPrecio("(//div[@class='productinfo text-center']//h2)[1]")
        F.Agregar_Producto_Carrito(3)
        nombre2 = F.GetNombre("(//div[@class='productinfo text-center']//p)[2]")
        precio2 = F.GetPrecio("(//div[@class='productinfo text-center']//h2)[2]")
        F.Click("(//a[contains(.,'Cart')])[1]")
        F.Click("//a[contains(.,'Proceed To Checkout')]")
        F.Validar_Elemento_Visible("//h2[contains(.,'Address Details')]")
        F.Verificar_Producto_Carrito(1, nombre1, precio1, 1)
        F.Verificar_Producto_Carrito(2, nombre2, precio2, 1)
        total_esperado = precio1 + precio2
        total_en_carrito = F.GetTotal(2)
        assert total_en_carrito == total_esperado, f"Total esperado: {total_esperado}, encontrado: {total_en_carrito}"
        F.Set_Texto("//textarea[@name='message']", "dejo un comentario")
        F.Click("//a[contains(.,'Place Order')]")
        F.CargarDatosTarjeta()
        F.Click("//button[contains(.,'Pay and Confirm Order')]")
        F.Validar_Elemento_Visible("(//div[contains(.,'Your order has been placed successfully!')])[7]")
        F.Validar_Elemento_Visible("//b[contains(.,'Order Placed!')]")
        F.Validar_Texto("(//div[@class='container']//p)[1]", "Congratulations! Your order has been confirmed!")
        F.Click("//a[contains(.,'Continue')]")
        F.Esperar(5)
        context.close()
        browser.close()
        assert True
    except Exception as e:
        context.close()
        browser.close()
        assert False, f"Error: {str(e)}"

def test_Eliminar_Producto_Carrito(playwright, page, context, browser) -> None:
    try:
        page.goto(URL)
        page.set_default_timeout(3000)
        F = Funciones_Globales(page)
        F.Validar_Elemento_Visible("(//div[@class='carousel-inner'])[1]")
        F.Click("//a[contains(.,' Products')]")
        F.Validar_Elemento_Visible("//h2[contains(.,'All Products')]")
        F.Agregar_Producto_Carrito(1)
        nombre1 = F.GetNombre("(//div[@class='productinfo text-center']//p)[1]")
        precio1 = F.GetPrecio("(//div[@class='productinfo text-center']//h2)[1]")
        F.Click("//u[contains(.,'View Cart')]")
        F.Verificar_Producto_Carrito(1, nombre1, precio1, 1)
        F.Eliminar_Producto(1)
        F.Validar_Elemento_No_Visible("(//div[@class='productinfo text-center']//p)[1]")
        F.Esperar(5)
        context.close()
        browser.close()
        assert True
    except Exception as e:
        context.close()
        browser.close()
        assert False, f"Error: {str(e)}"

def test_Validar_Categoria_Producto(playwright, page, context, browser) -> None:
    try:
        page.goto(URL)
        page.set_default_timeout(3000)
        F = Funciones_Globales(page)
        F.Validar_Elemento_Visible("(//div[@class='carousel-inner'])[1]")
        F.Validar_Elemento_Visible("//h2[contains(.,'Category')]")
        F.Click("//a[contains(.,'Women')]")
        F.Click("(//a[contains(.,'Dress')])[1]")
        F.Validar_Elemento_Visible("//h2[contains(.,'Women - Dress Products')]")
        F.Validar_Elemento_Visible("//a[contains(.,'Men')]")
        F.Click("//a[contains(.,'Men')]")
        F.Click("//a[contains(.,'Tshirts')]")
        F.Validar_Elemento_Visible("//h2[contains(.,'Men - Tshirts Products')]")
        F.Esperar(5)
        context.close()
        browser.close()
        assert True
    except Exception as e:
        context.close()
        browser.close()
        assert False, f"Error: {str(e)}"

def test_Validar_Marca_Producto(playwright, page, context, browser) -> None:
    try:
        page.goto(URL)
        page.set_default_timeout(3000)
        F = Funciones_Globales(page)
        F.Validar_Elemento_Visible("(//div[@class='carousel-inner'])[1]")
        F.Validar_Elemento_Visible("//h2[contains(.,'Brands')]")
        F.Click("//a[contains(.,'Polo')]")
        F.Validar_Elemento_Visible("//h2[contains(.,'Brand - Polo Products')]")
        F.Esperar(2)
        F.Validar_Elemento_Visible("//a[contains(.,'Kookie Kids')]")
        F.Click("//a[contains(.,'Kookie Kids')]")
        F.Validar_Elemento_Visible("//h2[contains(.,'Brand - Kookie Kids Products')]")
        F.Esperar(5)
        context.close()
        browser.close()
        assert True
    except Exception as e:
        context.close()
        browser.close()
        assert False, f"Error: {str(e)}"

def test_Buscar_Agregar_Producto_Carrito(playwright, page, context, browser) -> None:
    try:
        page.goto(URL)
        page.set_default_timeout(3000)
        F = Funciones_Globales(page)
        F.Validar_Elemento_Visible("(//div[@class='carousel-inner'])[1]")
        F.Click("//a[contains(.,' Products')]")
        F.Validar_Elemento_Visible("//h2[contains(.,'All Products')]")
        F.Set_Texto("//input[@id='search_product']","Tshirt")
        F.Click("//i[@class='fa fa-search']")
        F.Validar_Elemento_Visible("//h2[contains(.,'Searched Products')]")
        lista_productos = F.Obtener_Lista_Porductos()
        F.Agregar_Productos_Al_Carrito()
        F.Validar_Productos_Agregados_Carrito(lista_productos)
        F.Click("//a[contains(.,'Signup / Login')]")
        F.Validar_Elemento_Visible("//h2[contains(.,'Login to your account')]")
        F.Set_Texto("(//input[@name='email'])[1]", "pruebas@pruebas.com")
        F.Set_Texto("//input[@name='password']", "prueba")
        F.Click("//button[contains(.,'Login')]")
        F.Validar_Elemento_Visible("//a[contains(.,'Logged in as german')]")
        F.Click("(//a[contains(.,'Cart')])[1]")
        F.Validar_Productos_Agregados_Carrito(lista_productos)
        F.Esperar(5)
        context.close()
        browser.close()
        assert True
    except Exception as e:
        context.close()
        browser.close()
        assert False, f"Error: {str(e)}"

def test_Agregar_Comentario_Producto(playwright, page, context, browser) -> None:
    try:
        page.goto(URL)
        page.set_default_timeout(3000)
        F = Funciones_Globales(page)
        F.Validar_Elemento_Visible("(//div[@class='carousel-inner'])[1]")
        F.Click("//a[contains(.,' Products')]")
        F.Validar_Elemento_Visible("//h2[contains(.,'All Products')]")
        F.Click("(//a[contains(.,'View Product')])[1]")
        F.Set_Texto("//input[@id='name']", "German")
        F.Set_Texto("//input[@id='email']","pruebas@pruebas.com")
        F.Set_Texto("//textarea[@id='review']","Una review sobre el producto")
        F.Click("//button[contains(.,'Submit')]")
        F.Validar_Elemento_Visible("//button[contains(.,'Submit')]")
        F.Esperar(5)
        context.close()
        browser.close()
        assert True
    except Exception as e:
        context.close()
        browser.close()
        assert False, f"Error: {str(e)}"

def test_Agregar_Producto_Recomendado_Carrito(playwright, page, context, browser) -> None:
    try:
        page.goto(URL)
        F = Funciones_Globales(page)
        F.Esperar(3)
        F.Validar_Elemento_Visible("(//div[@class='carousel-inner'])[1]")
        F.Desplazar_Hasta_Elemento("//h2[contains(.,'recommended items')]")
        lista_productos.append(F.GetNombre("//div[@class='carousel-inner']//div[@class='item active']//div[@class='product-image-wrapper']//p"))
        F.hacer_click_en_primer_producto()
        F.Click("//u[contains(.,'View Cart')]")
        F.Validar_Productos_Agregados_Carrito(lista_productos)
        F.Esperar(5)
        context.close()
        browser.close()
        assert True
    except Exception as e:
        context.close()
        browser.close()
        assert False, f"Error: {str(e)}"

def test_Validar_Desplazamiento_Arriba(playwright, page, context, browser) -> None:
    try:
        page.goto(URL)
        F = Funciones_Globales(page)
        F.Esperar(3)
        F.Validar_Elemento_Visible("(//div[@class='carousel-inner'])[1]")
        F.Desplazar_Hasta_Elemento("//h2[contains(.,'Subscription')]")
        F.Validar_Elemento_Visible("//h2[contains(.,'Subscription')]")
        F.Esperar(2)
        F.Click("//i[@class='fa fa-angle-up']")
        F.Validar_Elemento_Visible("(//h2[contains(.,'Full-Fledged practice website for Automation Engineers')])[3]")
        F.Esperar(5)
        context.close()
        browser.close()
        assert True
    except Exception as e:
        context.close()
        browser.close()
        assert False, f"Error: {str(e)}"

def test_Validar_Desplazamiento_Abajo_Arriba(playwright, page, context, browser) -> None:
    try:
        page.goto(URL)
        F = Funciones_Globales(page)
        F.Esperar(3)
        F.Validar_Elemento_Visible("(//div[@class='carousel-inner'])[1]")
        F.Desplazar_Hasta_Elemento("//h2[contains(.,'Subscription')]")
        F.Validar_Elemento_Visible("//h2[contains(.,'Subscription')]")
        F.Esperar(2)
        F.Desplazar_Hasta_Elemento("(//h2[contains(.,'Full-Fledged practice website for Automation Engineers')])[1]")
        F.Validar_Elemento_Visible("(//h2[contains(.,'Full-Fledged practice website for Automation Engineers')])[1]")
        F.Esperar(5)
        context.close()
        browser.close()
        assert True
    except Exception as e:
        context.close()
        browser.close()
        assert False, f"Error: {str(e)}"






