from django.db import models


class Transaction(models.Model):
    PENDING = 0
    WAITING=1
    CONFIRMED = 2
    STATUSES = (
        (PENDING, 'Pending'),
        (WAITING, 'Waiting'),
        (CONFIRMED, 'Confirmed'),
    )

    created = models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length=64)
    amount = models.IntegerField(default=0)
    status = models.IntegerField(default=0, choices=STATUSES)
    tx = models.CharField(max_length=64, null=True, blank=True, default="")

    class Meta:
        ordering = ('created',)
        get_latest_by = "created"

    def __str__(self):
        return self.address
