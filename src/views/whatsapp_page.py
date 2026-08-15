class WhatsAppPage:
    def __init__(self, page):
        self.page = page

    def navigate_to_chat(self, phone: str):
        print(f"Navegando al chat del número: {phone}")
        clean_phone = phone.replace("+", "")
        # API web de WhatsApp para ir directo a un chat
        self.page.goto(f"https://web.whatsapp.com/send?phone={clean_phone}")
        
        # Esperamos a que cargue la caja de texto del chat
        self.page.wait_for_selector('#main div[contenteditable="true"]', timeout=60000)

    def send_message(self, text: str):
        print("Escribiendo mensaje...")
        # Localizamos la caja de texto y escribimos
        chat_box = self.page.locator('#main div[contenteditable="true"]').nth(0)
        chat_box.click()
        chat_box.fill(text)
        
        # Simulamos presionar la tecla Enter para enviar
        self.page.keyboard.press("Enter")
        print("Mensaje enviado.")
        
        # Pausa breve para asegurar que el mensaje salga antes de cerrar
        self.page.wait_for_timeout(3000)