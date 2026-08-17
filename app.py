import os

from dotenv import load_dotenv

from whatsapp_bot import WhatsAppBot


def main():
    load_dotenv()

    telefono = os.getenv("PHONE_NUMBER")

    if not telefono:
        print("Falta configurar PHONE_NUMBER en el archivo .env")
        return

    mensaje = "Tarea finalizada.\nPatrones utilizados: Builder, Page Object Model, Strategy."

    bot = WhatsAppBot(telefono, mensaje)
    bot.ejecutar()


if __name__ == "__main__":
    main()