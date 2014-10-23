from django.db import models
from django.contrib.auth.models import User

class Person(models.Model):
    user = models.OneToOneField(User)
    zoobars = models.IntegerField(default=10)
    profile = models.TextField(max_length=5000, default="")

    def __str__(self):
        return "(User %s, zoobars=%d)" % (self.user.username, self.zoobars)

class Transfer(models.Model):
    sender = models.ForeignKey(Person, related_name='sent_transfers')
    recipient = models.ForeignKey(Person, related_name='received_transfers')
    amount = models.IntegerField()
    time = models.DateTimeField()

    def __str__(self):
        return "Transfer of %d zoobars from %s to %s" % (self.amount, self.sender.user.username, self.recipient.user.username)
