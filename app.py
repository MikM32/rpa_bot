import os

from dotenv import load_dotenv

from src.controllers.bot_controller import BotController
from src.models.bot_model import BotConfigBuilder
from src.strategies.message_strategy import DirectMessageStrategy


def main():
    load_dotenv()

    telefono = os.getenv("PHONE_NUMBER")

    if not telefono:
        print("Falta configurar PHONE_NUMBER en el archivo .env")
        return

    mensaje = "Tarea finalizada.\nPatrones utilizados: Builder, Page Object Model, Strategy."

    config = (BotConfigBuilder()
              .set_phone(telefono)
              .set_message(mensaje)
              .build())

    strategy = DirectMessageStrategy()

    bot = BotController(config, strategy)
    bot.run()


if __name__ == "__main__":
    main()