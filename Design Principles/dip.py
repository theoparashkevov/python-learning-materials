"""
The Dependency Inversion principle states that high-level modules should not depend on low-level modules.
Instead, both should depend on abstractions. Abstractions should not depend on details.
Details should depend on abstractions. This principle encourages the use of interfaces and abstract classes to
decouple the system components.
In this example, NotificationService is a high-level module that is responsible for sending notifications. It takes a
notifier object as a dependency, which could be an email notifier, SMS notifier, or any other notifier that implements
the send() method.

Instead of instantiating the EmailNotifier or SMSNotifier classes directly, NotificationService relies on
an abstraction, which is the notifier parameter. This abstraction could be an interface or an abstract class that
defines the send() method.

By depending on an abstraction rather than a concrete implementation, the NotificationService class is decoupled from
the specific notification method, making it easier to change or add new notification methods in the future.
Similarly, the EmailNotifier and SMSNotifier classes depend on the abstraction instead of the details of the
NotificationService class, making them decoupled and reusable in other contexts.
"""


class NotificationService:
	def __init__(self, notifier):
		self.notifier = notifier

	def send_notification(self, message):
		self.notifier.send(message)


class EmailNotifier:
	def send(self, message):
		print(f"Sending email notification: {message}")


class SMSNotifier:
	def send(self, message):
		print(f"Sending SMS notification: {message}")
