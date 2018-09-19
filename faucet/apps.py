from django.apps import AppConfig


class FaucetConfig(AppConfig):
    name = 'faucet'

    def ready(self):
        import faucet.signals
