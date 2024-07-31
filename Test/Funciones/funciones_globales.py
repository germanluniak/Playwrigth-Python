import os
import random
import re
import string
import time

nombres = []

class Funciones_Globales:

    def __init__(self, page):
        self.page = page

    def Esperar(self, tiempo):
        time.sleep(tiempo)

    def Click(self, selector, tiempo=0.5):
        element = self.page.locator(selector)
        element.wait_for(state="visible", timeout=10000)
        element.click()
        time.sleep(tiempo)

    def Validar_Elemento_Visible(self, selector, tiempo=0.5):
        try:
            # Espera a que el elemento esté visible
            element = self.page.locator(selector)
            element.wait_for(state='visible', timeout=5000)  # Timeout de 5 segundos
            print("El elemento es visible.")
        except Exception as e:
            print(f"El elemento no es visible. Error: {e}")

    def Set_Texto(self, selector, texto, tiempo=1):
        t = self.page.locator(selector)
        t.fill('')
        self.Esperar(2)
        t.fill(texto)
        time.sleep(tiempo)

    def Select_Fecha(self, dia, mes, anio, tiempo=0.5):
        self.page.locator("#days").select_option(dia)
        self.page.locator("#months").select_option(mes)
        self.page.locator("#years").select_option(anio)

    def generate_random_email(self):
        random_part = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
        email = f"mail{random_part}@prueba.com"
        return email

    def Completar_Formulario(self, nombre, apellido, compania, direccion1, direccion2, pais, estado, ciudad, cp, telefono):
        self.Set_Texto("//input[@id='first_name']",nombre)
        self.Set_Texto("//input[@id='last_name']",apellido)
        self.Set_Texto("//input[@id='company']",compania)
        self.Set_Texto("//input[@id='address1']",direccion1)
        self.Set_Texto("//input[@id='address2']",direccion2)
        self.page.locator("#country").select_option(pais)
        self.Set_Texto("//input[@id='state']",estado)
        self.Set_Texto("//input[@id='city']",ciudad)
        self.Set_Texto("//input[@id='zipcode']",cp)
        self.Set_Texto("//input[@id='mobile_number']",telefono)

    def Completar_Formulario_Contacto(self, nombre, email, asunto, mensaje, archivo):
        self.Set_Texto("//input[@name='name']",nombre)
        self.Set_Texto("//input[@name='email']",email)
        self.Set_Texto("//input[@name='subject']",asunto)
        self.Set_Texto("//textarea[@name='message']",mensaje)
        self.Upload_file("//input[@type='file']", archivo)

    def Upload_file(self, selector, archivo, tiempo=0.5):
        input_element = self.page.locator(selector)
        archivo = os.path.normpath(archivo)
        input_element.set_input_files(archivo)
        time.sleep(tiempo)

    def Validar_Texto(self, selector, texto_esperado):
        texto_obtenido = self.page.text_content(selector)
        assert texto_obtenido == texto_esperado, f"El texto del selector '{selector}' es '{texto_obtenido}', pero se esperaba '{texto_esperado}'."
        print(f"El texto del selector '{selector}' coincide con el texto esperado: '{texto_esperado}'.")

    def Desplazar_Hasta_Elemento(self, selector):
        try:
            # Obtener el elemento
            elemento = self.page.query_selector(selector)

            if elemento:
                # Desplazar la pantalla hasta que el elemento esté en la vista
                self.page.evaluate("element => element.scrollIntoView()", elemento)
                print(f"Desplazado hasta el elemento con selector '{selector}'")
            else:
                raise Exception(f"El elemento con selector '{selector}' no fue encontrado.")
        except Exception as e:
            print(f"Error: {str(e)}")

    def GetPrecio(self, selector):
        text = self.page.text_content(selector)
        match = re.search(r'\d+', text)
        if match:
            number = int(match.group())
            return number
        else:
            print("No se encontró ningún número en el texto")
            return None

    def GetNombre(self, selector):
        text = self.page.text_content(selector)
        return re.sub(r'\s+', ' ', text).strip()

    def Agregar_Producto_Carrito(self, position):
            add_to_cart_selector = f"(//a[contains(.,'Add to cart')])[{position}]"
            self.page.click(add_to_cart_selector)

    def Agregar_Productos_Al_Carrito(self):
        # Contar la cantidad de elementos 'Add to cart' disponibles
        cantidad_elementos = self.Cantidad_Prodcutos("(//a[contains(.,'View Product')])")

        # Iterar sobre los valores de position en pasos de 2, cantidad_elementos veces
        for i in range(cantidad_elementos):
            position = (i * 2) + 1  # Esto asegura que se seleccionen posiciones 1, 3, 5, ..., hasta el límite
            add_to_cart_selector = f"(//a[contains(.,'Add to cart')])[{position}]"
            self.Click(add_to_cart_selector)
            if i < cantidad_elementos - 1:  # Solo hacer click en 'Continue Shopping' si no es el último elemento
                self.Click("//button[contains(.,'Continue Shopping')]")
            else:  # Si es el último, hacer click en 'View Cart'
                self.Click("//u[contains(.,'View Cart')]")

    def Verificar_Producto_Carrito(self, producto_id, nombre, precio, cant_producto):
        nombre_selector = f"//tr[@id='product-{producto_id}']//a[contains(@href,'details/{producto_id}')]"
        precio_selector = f"(//td[contains(@class,'cart_price')])[{producto_id}]"
        cantidad_selector = f"(//button[@class='disabled'])[{producto_id}]"

        nombre_en_carrito = self.GetNombre(nombre_selector)
        precio_en_carrito = self.GetPrecio(precio_selector)
        cantidad_en_carrito = int(self.page.text_content(cantidad_selector))

        assert nombre_en_carrito == nombre, f"Nombre esperado: {nombre}, encontrado: {nombre_en_carrito}"
        assert precio_en_carrito == precio, f"Precio esperado: {precio}, encontrado: {precio_en_carrito}"
        assert cantidad_en_carrito == cant_producto, f"Cantidad esperada: {cant_producto}, encontrada: {cantidad_en_carrito}"

    def Limpiar_Espacios(self, texto):
        # Reemplaza múltiples espacios con un solo espacio y elimina espacios iniciales y finales
        return ' '.join(texto.split())

    def Obtener_Lista_Porductos(self):
        cantidad_elementos = self.Cantidad_Prodcutos("//a[contains(.,'View Product')]")
        for i in range(1, cantidad_elementos + 1):
            nombre_selector = f"(//div[@class='productinfo text-center']//p)[{i}]"
            nombre = self.page.text_content(nombre_selector).strip()
            nombre_limpio = self.Limpiar_Espacios(nombre)
            nombres.append(nombre_limpio)
        return nombres

    def obtener_ids_productos(self):
        # Obtener una lista de todos los elementos tr con id que comienza con 'product-'
        tr_elements = self.page.query_selector_all("//tr[starts-with(@id, 'product-')]")
        ids_productos = [tr.get_attribute('id').split('-')[1] for tr in tr_elements]
        return ids_productos

    def Validar_Productos_Agregados_Carrito(self, lista_nombres):
        ids_productos = self.obtener_ids_productos()
        productos_encontrados = []

        for producto_id in ids_productos:
            nombre_en_pantalla = False
            nombre_selector = f"//tr[@id='product-{producto_id}']//a[contains(@href,'details/{producto_id}')]"
            nombre_actual = self.page.text_content(nombre_selector).strip()
            nombre_actual_limpio = self.Limpiar_Espacios(nombre_actual)

            if nombre_actual_limpio in lista_nombres:
                nombre_en_pantalla = True
                productos_encontrados.append(nombre_actual_limpio)

            assert nombre_en_pantalla, f"Nombre '{nombre_actual_limpio}' no encontrado en la pantalla"

        # Verificar si todos los productos en lista_nombres están en productos_encontrados
        for nombre in lista_nombres:
            assert nombre in productos_encontrados, f"Producto '{nombre}' no encontrado en el carrito"

    def GetTotal(self, cant_productos):
        monto_total = 0
        for i in range(1, cant_productos + 1):
            selector = f"(//p[contains(@class,'price')])[{i}]"
            monto_total += self.GetPrecio(selector)
        return monto_total

    def Eliminar_Producto(self, idProd):
        self.Click(f"(//i[@class='fa fa-times'])[{idProd}]")

    def Validar_Informacion_Entrega(self, nombre, apellido, compania, dir1, dir2, pais, estado, ciudad, cp, tel):
        # Obtener los valores de la página
        txt_nombre_apellido = self.page.text_content("(//li[contains(@class,'lastname')])[1]").strip()
        txt_compania = self.page.text_content("(//li[contains(@class,'address2')])[1]").strip()
        txt_direccion1 = self.page.text_content("(//li[contains(@class,'address2')])[2]").strip()
        txt_direccion2 = self.page.text_content("(//li[contains(@class,'address2')])[3]").strip()
        txt_estado_ciudad_cp = self.page.text_content("(//li[contains(@class,'postcode')])[1]").strip()
        estado_ciudad_cp_txt = re.sub(r'\s+', ' ', txt_estado_ciudad_cp).strip()
        txt_pais = self.page.text_content("(//li[@class='address_country_name'])[1]").strip()
        txt_telefono = self.page.text_content("(//li[contains(@class,'phone')])[1]").strip()

        # Construir las cadenas esperadas a partir de los parámetros
        nombre_apellido_esperado = f"Mr. {nombre} {apellido}"
        estado_ciudad_cp_esperado = f"{ciudad} {estado} {cp}"

        # Validar los valores obtenidos contra los valores esperados
        assert txt_nombre_apellido == nombre_apellido_esperado, f"Nombre y apellido esperados: {nombre_apellido_esperado}, encontrados: {txt_nombre_apellido}"
        assert txt_compania == compania, f"Compañía esperada: {compania}, encontrada: {txt_compania}"
        assert txt_direccion1 == dir1, f"Dirección 1 esperada: {dir1}, encontrada: {txt_direccion1}"
        assert txt_direccion2 == dir2, f"Dirección 2 esperada: {dir2}, encontrada: {txt_direccion2}"
        assert txt_pais == pais, f"País esperado: {pais}, encontrado: {txt_pais}"
        assert txt_telefono == tel, f"Teléfono esperado: {tel}, encontrado: {txt_telefono}"
        assert estado_ciudad_cp_txt == estado_ciudad_cp_esperado, f"Estado, ciudad y CP esperados: {estado_ciudad_cp_esperado}, encontrados: {estado_ciudad_cp_txt}"

    def CargarDatosTarjeta(self):
        self.Set_Texto("(//input[contains(@name,'card')])[1]","juan perez")
        self.Set_Texto("//input[@name='card_number']", "4509953566233704")
        self.Set_Texto("//input[@name='cvc']","123")
        self.Set_Texto("//input[@name='expiry_month']","11")
        self.Set_Texto("//input[@name='expiry_year']","2025")

    def Validar_Elemento_No_Visible(self, selector):
        # Verifica que el elemento no esté visible en la página
        elemento_visible = self.page.is_visible(selector)
        assert not elemento_visible, f"El elemento con el selector {selector} sigue siendo visible"

    def Cantidad_Prodcutos(self, selector):
        # Obtiene una lista de elementos que coinciden con el selector
        elementos = self.page.query_selector_all(selector)
        # Retorna la cantidad de elementos encontrados
        return len(elementos)

    def hacer_click_en_primer_producto(self) :
        # Selector para todos los botones de agregar al carrito en el carrusel visible
        boton_agregar_selector = "//div[@class='carousel-inner']//div[@class='item active']//i[contains(@class,'fa fa-shopping-cart')]"

        # Encuentra todos los botones de agregar al carrito
        botones = self.page.locator(boton_agregar_selector)

        # Verifica si hay al menos un botón y haz clic en el primero
        if botones.count() > 0:
            botones.first.click()
            print("Se hizo clic en el primer botón de agregar al carrito encontrado.")
        else:
            print("No se encontraron botones de agregar al carrito.")

    def Validar_Descarga(self, selector):
        try:
            with self.page.expect_download() as download_i:
                self.Click(selector)
            dl = download_i.value
            working_dir_path = os.getcwd()
            final_path = os.path.join(working_dir_path, "Descargas/archivo.txt")
            dl.save_as(final_path)
            if os.path.getsize(final_path) > 0:
                os.remove(final_path)
                return True
            else:
                print("El archivo está vacío.")
                return False

        except Exception as e:
            print("Error:", e)
            return False