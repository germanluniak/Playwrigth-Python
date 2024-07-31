# Playwright-Python

Este repositorio contiene una serie de pruebas automatizadas utilizando Playwright y Python, diseñadas para validar diversas funcionalidades de una aplicación web. Las pruebas están basadas en los casos de prueba detallados en el sitio [Automation Exercise](https://automationexercise.com/test_cases).
## Estructura del Proyecto

- **.idea**: Configuraciones del proyecto de IntelliJ IDEA.
- **Test**: Contiene las pruebas y configuraciones.
  - **Config**: Configuraciones y archivos comunes.
  - **TestCase**: Casos de prueba y resultados de Allure.
  
## Requisitos

- Python 3.x
- Playwright
- pytest
- allure-pytest

## Instalación

1. Clona este repositorio:
    ```sh
    git clone https://github.com/germanluniak/Playwright-Python.git
    cd Playwright-Python
    ```

2. Crea y activa un entorno virtual:
    ```sh
    python -m venv venv
    source venv/bin/activate   # En Windows: venv\Scripts\activate
    ```

3. Instala las dependencias:
    ```sh
    pip install -r requirements.txt
    ```

4. Instala Playwright y sus navegadores:
    ```sh
    playwright install
    ```

## Ejecución de Pruebas

Para ejecutar las pruebas y generar un reporte de Allure:

```sh
pytest --alluredir=Test/TestCase/allure-results
allure serve Test/TestCase/allure-results
