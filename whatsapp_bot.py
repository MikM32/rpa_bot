from playwright.sync_api import sync_playwright


class WhatsAppBot:
    def __init__(self, telefono, mensaje):
        self.telefono = telefono
        self.mensaje = mensaje

    def ejecutar(self):
        with sync_playwright() as p:
            context = p.chromium.launch_persistent_context(
                user_data_dir="auth/user_data",
                headless=False,
            )

            page = context.pages[0]
            page.goto("https://web.whatsapp.com")
            print("Verificando la sesion de WhatsApp...")

            try:
                page.wait_for_selector("#pane-side", timeout=30000)
                print("Sesion activa. Entrando al chat...")
            except Exception:
                print("No hay sesion activa. Escanea el codigo QR...")
                page.wait_for_selector("#pane-side", timeout=120000)
                print("QR escaneado. Esperando unos segundos para guardar los datos...")
                page.wait_for_timeout(5000)

            self.enviar_mensaje(page)

            context.close()

    def enviar_mensaje(self, page):
        telefono_limpio = self.telefono.replace("+", "")
        url = f"https://web.whatsapp.com/send?phone={telefono_limpio}"

        print(f"Abriendo el chat del numero {telefono_limpio}...")
        page.goto(url)
        page.wait_for_selector('#main div[contenteditable="true"]', timeout=60000)

        print("Escribiendo el mensaje...")
        caja_texto = page.locator('#main div[contenteditable="true"]').nth(0)
        caja_texto.click()
        caja_texto.fill(self.mensaje)
        page.keyboard.press("Enter")

        print("Mensaje enviado.")
        page.wait_for_timeout(3000)