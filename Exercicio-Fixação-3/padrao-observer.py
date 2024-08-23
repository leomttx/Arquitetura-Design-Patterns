
# Implementação do padrão Observer
class EventManager:
    def __init__(self):
        self.listeners = []
    
    def subscribe(self, listener):
        self.listeners.append(listener)
    
    # Notifica todos os observadores
    def notify(self, event):
        for listener in self.listeners:
            listener.update(event)
    
# Interface para os observadores
class EventObserver:
    def update(self, event):
        print(f"Event received: {event}")

class EmailNotifier(EventObserver):
    def update(self, event):
        print(f"Email notification: {event}")

class PushNotifier(EventObserver):
    def update(self, event):
        print(f"Push notification: {event}")

def main():
    event_manager = EventManager()
    email_notifier = EmailNotifier()
    push_notifier = PushNotifier()

    event_manager.subscribe(email_notifier)
    event_manager.subscribe(push_notifier)


    event_manager.notify("Notificação de um novo evento")

    
main()