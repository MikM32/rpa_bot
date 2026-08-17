# Patron PAGE OBJECT MODEL: encapsula los elementos de la pagina
class WhatsAppPage:
    def __init__(self, page):
        self.page = page

    def navigate_to_chat(self, phone):
        print(f"Abriendo el chat del numero {phone}...")
        clean_phone = phone.replace("+", "")
        self.page.goto(f"https://web.whatsapp.com/send?phone={clean_phone}")
        self.page.wait_for_selector('#main div[contenteditable="true"]', timeout=60000)

    def send_message(self, text):
        print("Escribiendo el mensaje...")
        chat_box = self.page.locator('#main div[contenteditable="true"]').nth(0)
        chat_box.click()
        chat_box.fill(text)
        self.page.keyboard.press("Enter")
        print("Mensaje enviado.")
        self.page.wait_for_timeout(3000)