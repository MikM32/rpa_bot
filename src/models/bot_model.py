class BotConfig:
    def __init__(self):
        self.message = ""
        self.phone_number = ""


# Patron BUILDER: construye la configuracion paso a paso
class BotConfigBuilder:
    def __init__(self):
        self.config = BotConfig()

    def set_phone(self, phone_number):
        self.config.phone_number = phone_number
        return self

    def set_message(self, message):
        self.config.message = message
        return self

    def build(self):
        return self.config