import allure
import os

def handle_error(page, context, browser, error_message):
    # Define el path del directorio
    allure_results_dir = '/allure-results'
    os.makedirs(allure_results_dir, exist_ok=True)

    # Define el path para la captura de pantalla y el archivo de log
    screenshot_path = os.path.join(allure_results_dir, 'screenshot.png')
    log_path = os.path.join(allure_results_dir, 'error_log.txt')

    # Captura la pantalla
    page.screenshot(path=screenshot_path)
    print(f"Screenshot saved to {screenshot_path}")

    # Adjunta la captura de pantalla al reporte de Allure
    with open(screenshot_path, 'rb') as file:
        allure.attach(file.read(), name='Error Screenshot', attachment_type=allure.attachment_type.PNG)

    # Guarda detalles del error
    with open(log_path, 'a') as f:
        f.write(f"Error: {error_message}\n")
        f.write(f"Screenshot saved to {screenshot_path}\n")

    context.close()
    browser.close()
    assert False, f"Error: {error_message}"
