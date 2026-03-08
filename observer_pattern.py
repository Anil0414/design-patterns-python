# observer_pattern.py

class Subscriber:
    def update(self, message):
        print(f"Subscriber received: {message}")


class Publisher:

    def __init__(self):
        self.subscribers = []

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)

    def unsubscribe(self, subscriber):
        self.subscribers.remove(subscriber)

    def notify(self, message):
        for subscriber in self.subscribers:
            subscriber.update(message)


# Client Code
if __name__ == "__main__":

    pub = Publisher()

    sub1 = Subscriber()
    sub2 = Subscriber()

    pub.subscribe(sub1)
    pub.subscribe(sub2)

    pub.notify("New Event Triggered!")