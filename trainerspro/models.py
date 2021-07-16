from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE
from django.utils.translation import ugettext_lazy as _
from .managers import CustomUserManager
from .choices import WEEKDAYS

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    is_trainer = models.BooleanField(_('is_trainer'), default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.first_name + ' ' + self.last_name
        
class Package(models.Model):
    name = models.CharField(max_length=100)
    price= models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=300)
    time = models.IntegerField()
    class Meta:
        verbose_name = _('package')
        verbose_name_plural = _('packages')

    
class Event(models.Model):
    date = models.DateField()
    start_hour = models.TimeField()
    end_hour = models.TimeField()
    trainer = models.ForeignKey(CustomUser,on_delete=CASCADE)
    client_email = models.EmailField(default='')
    client_phone = models.IntegerField(default=1)
    package = models.ForeignKey(Package,on_delete=CASCADE)
    class Meta:
        verbose_name = _('event')
        verbose_name_plural = _('events')

class TrainerHoursPerDay(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=CASCADE)
    weekday = models.IntegerField(choices=WEEKDAYS)
    from_hour = models.TimeField()
    to_hour = models.TimeField()
    
    class Meta:
        ordering = ('weekday', 'from_hour')
        unique_together = ('weekday', 'from_hour', 'to_hour')
        verbose_name = _('hour')
        verbose_name_plural = _('hours')
       
    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name+ ' ' + self.get_weekday_display()




