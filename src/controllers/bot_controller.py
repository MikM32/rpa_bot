import os
from playwright.sync_api import sync_playwright
from src.views.whatsapp_page import WhatsAppPage

class BotController:
    def __init__(self, config, strategy):
        self.config = config
        self.strategy = strategy

    def run(self):
        with sync_playwright() as p:
            session_dir = "auth/user_data"
            
            print("Iniciando navegador con persistencia de sesión...")
            
            context = p.chromium.launch_persistent_context(
                user_data_dir=session_dir,
                headless=False
            )
            
            page = context.pages[0]

            page.goto("https://web.whatsapp.com")
            print("Verificando estado de la sesión de WhatsApp...")

            try:
                # Intentamos ver si carga el panel de chats rápido (10 segundos)
                page.wait_for_selector('#pane-side', timeout=10000)
                print("Sesión validada correctamente. Procediendo al chat...")
            except:
                # Si da Timeout, significa que nos está pidiendo escanear el QR
                print("No se encontró sesión activa. Por favor, escanea el código QR...")
                
                # Le damos 2 minutos para que escanees el QR
                page.wait_for_selector('#pane-side', timeout=120000)
                
                # Pausa VITAL de 5 segundos para que WhatsApp guarde sus claves de IndexedDB
                print("¡QR escaneado! Dando 5 segundos a WhatsApp para guardar credenciales...")
                page.wait_for_timeout(5000)

            # Instanciamos la Vista (POM) y ejecutamos la Estrategia (Strategy)
            wa_page = WhatsAppPage(page)
            self.strategy.send(wa_page, self.config.phone_number, self.config.message)

            # Cerramos el contexto para asegurar que los datos se escriban en disco correctamente
            context.close()