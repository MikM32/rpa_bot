from src.models.bot_model import BotConfigBuilder
from src.strategies.message_strategy import DirectMessageStrategy
from src.controllers.bot_controller import BotController
import os
from dotenv import load_dotenv



def main():

    load_dotenv() 
    
    # 1. Construimos la configuración usando el patrón BUILDER
    mensaje_tarea = "Tarea finalizada.\nPatrones utilizados: Builder, Page Object Model, Strategy y mvc."

    phone_number = os.getenv("PHONE_NUMBER")

    if not phone_number:
        raise ValueError("¡Falta configurar PHONE_NUMBER en el archivo .env!")
    
    config = (BotConfigBuilder()
              .set_phone(phone_number)  
              .set_message(mensaje_tarea)
              .build())

    # 2. Definimos el comportamiento usando el patrón STRATEGY
    strategy = DirectMessageStrategy()

    # 3. Inicializamos el Controlador (MVC) inyectando dependencias
    bot = BotController(config, strategy)
    
    # Arrancamos la ejecución
    bot.run()

if __name__ == "__main__":
    main()