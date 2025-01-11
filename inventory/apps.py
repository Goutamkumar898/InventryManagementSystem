from django.apps import AppConfig

class InventoryConfig(AppConfig):
    name = 'inventory'
    verbose_name = 'Inventory Management'

    def ready(self):
        # This method is called when the app is ready
        # You can use this to import signals or perform any setup for the app.
        pass
