from django.db import models
from django.contrib.auth.models import User

class Person(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    zoobars = models.IntegerField(default=10)
    profile = models.TextField(max_length=5000, default="")

    def __str__(self):
        return "(User %s, zoobars=%d)" % (self.user.username, self.zoobars)

class Transfer(models.Model):
    sender = models.ForeignKey(Person, related_name='sent_transfers')
    recipient = models.ForeignKey(Person, related_name='received_transfers')
    amount = models.IntegerField()
    time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Transfer of %d zoobars from %s to %s" % (self.amount, self.sender.user.username, self.recipient.user.username)

def create_person(instance, created, raw, **kwargs):
    # Ignore fixtures and saves for existing courses.
    if not created or raw:
        return

    person = Person()
    person.user = instance
    person.save()

models.signals.post_save.connect(create_person, sender=User, dispatch_uid='create_user_person')
