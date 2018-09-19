import requests

from django.conf import settings


class WalletClient:

    def get_balance():
        url = '%s/wallet/%s/balance' % (settings.COIN_NODE, settings.COIN_WALLET)
        response = requests.get(url, auth=settings.COIN_AUTH)
        json = response.json()
        return json['confirmed']

    def send(address, amount):
        url = '%s/wallet/%s/send' % (settings.COIN_NODE, settings.COIN_WALLET)
        data = """{
            "rate": %s,
            "outputs": [{
                "address": "%s",
                "value": %s
            }]
        }""" % (settings.COIN_FEE, address, amount)
        response = requests.post(url, data, auth=settings.COIN_AUTH)
        json = response.json()
        return json['hash']
