from playwright.sync_api import sync_playwright

from src.views.whatsapp_page import WhatsAppPage


class BotController:
    def __init__(self, config, strategy):
        self.config = config
        self.strategy = strategy

    def run(self):
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

            wa_page = WhatsAppPage(page)
            self.strategy.send(wa_page, self.config.phone_number, self.config.message)

            context.close()