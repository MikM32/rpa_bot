import os
from playwright.sync_api import sync_playwright
from src.views.whatsapp_page import WhatsAppPage

class BotController:
    def __init__(self, config, strategy):
        self.config = config
        self.strategy = strategy

    def run(self):
        with sync_playwright() as p:
            session_exists = os.path.exists(self.config.session_file)
            browser = p.chromium.launch(headless=False)

            if session_exists:
                print("Sesión encontrada. Cargando credenciales...")
                context = browser.new_context(storage_state=self.config.session_file)
                page = context.new_page()
                
                # TRUCO: Entrar a la raíz primero para que WhatsApp acepte el storage_state
                page.goto("https://web.whatsapp.com")
                print("Validando sesión de WhatsApp...")
                page.wait_for_selector('#pane-side', timeout=60000)
                print("Sesión validada correctamente. Procediendo al chat...")
                
            else:
                print("No se encontró sesión. Preparando para escanear QR...")
                context = browser.new_context()
                page = context.new_page()
                
                page.goto("https://web.whatsapp.com")
                print("Por favor, escanea el código QR de WhatsApp en el navegador.")
                
                page.wait_for_selector('#pane-side', timeout=120000)
                
                print("Cargando chats, guardando sesión en 5 segundos...")
                page.wait_for_timeout(5000)
                
                os.makedirs(os.path.dirname(self.config.session_file), exist_ok=True)
                context.storage_state(path=self.config.session_file)
                print("¡Sesión guardada con éxito!")

            # Instanciamos la Vista (POM) y ejecutamos la Estrategia (Strategy)
            wa_page = WhatsAppPage(page)
            self.strategy.send(wa_page, self.config.phone_number, self.config.message)

            # Cerrar el contexto correctamente asegura que no se corrompan los datos
            context.close()
            browser.close()