# apps.py

from django.apps import AppConfig

class PizzaOrderingConfig(AppConfig):
    name = 'pizza_ordering'

    def ready(self):
        import pizza_ordering.signals
