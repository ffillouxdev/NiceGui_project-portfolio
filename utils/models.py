from tortoise import fields, models

class CounterForWebsiteTrafic(models.Model):
    id = fields.IntField(pk=True)
    counter = fields.IntField()