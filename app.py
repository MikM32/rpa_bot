from playwright.sync_api import sync_playwright

def run():

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)  # Abre la ventana visualmente

        page = browser.new_page()
        page.goto("https://playwright.dev")

        print("Título de la página:", page.title())

        input("Presiona Enter en la terminal para cerrar el navegador...")

        browser.close()

if __name__ == "__main__":
    run()