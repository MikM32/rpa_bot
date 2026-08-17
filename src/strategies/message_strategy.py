from abc import ABC, abstractmethod


# Patron STRATEGY: define la interfaz para enviar mensajes
class SendStrategy(ABC):
    @abstractmethod
    def send(self, page, phone, message):
        pass


class DirectMessageStrategy(SendStrategy):
    def send(self, page, phone, message):
        page.navigate_to_chat(phone)
        page.send_message(message)