from abc import ABC, abstractmethod

class SendStrategy(ABC):
    @abstractmethod
    def send(self, page_object, phone: str, message: str):
        pass

# Estrategia concreta para enviar un mensaje directo a un número
class DirectMessageStrategy(SendStrategy):
    def send(self, page_object, phone: str, message: str):
        page_object.navigate_to_chat(phone)
        page_object.send_message(message)