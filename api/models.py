from django.db import models


class CurrencyPairs(models.Model):
    currency_pair = models.CharField(max_length=10)


class CurrencyPair(models.Model):
    currency_pair = models.ForeignKey(
        CurrencyPairs, on_delete=models.CASCADE, related_name='currency_pairs')
    date = models.DateTimeField(auto_now_add=True)
    min = models.FloatField()
    max = models.FloatField()
