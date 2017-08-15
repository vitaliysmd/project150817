from django.db import models


class Subscriber(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=128)
    message = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return "Пользователь %s %s %s" % (self.name, self.email, self.message)

    class Meta:
        verbose_name = 'MySubscriber'
        verbose_name_plural = 'A lot of Subscribers'