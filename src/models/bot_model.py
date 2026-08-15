class BotConfig:
    def __init__(self):
        self.message = ""
        self.phone_number = ""
        self.session_file = "auth/state.json"

# Patrón BUILDER: Nos permite construir la configuración paso a paso
class BotConfigBuilder:
    def __init__(self):
        self.config = BotConfig()

    def set_message(self, message: str):
        self.config.message = message
        return self

    def set_phone(self, phone_number: str):
        self.config.phone_number = phone_number
        return self

    def build(self):
        return self.config