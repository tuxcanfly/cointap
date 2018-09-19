from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

from faucet.models import Transaction
from faucet.rpc import WalletClient

@receiver(post_save, sender=Transaction)
def tx_save_handler(sender, instance, created, **kwargs):
    if created:
        balance = WalletClient.get_balance()
        instance.amount = int(balance * settings.COIN_SHARE)
        instance.tx = WalletClient.send(instance.address, instance.amount)
        instance.save()
