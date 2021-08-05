from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey, OneToOneField
from django.utils.translation import ugettext_lazy as _
from .managers import CustomUserManager,PlanCompletedManager
from .choices import WEEKDAYS
from tinymce import models as tinymce_models
from django.db.models.signals import pre_save
from datetime import datetime
from phonenumber_field.modelfields import PhoneNumberField

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    is_trainer = models.BooleanField(_('is_trainer'), default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' ' + self.email
        
class Package(models.Model):
    name = models.CharField(max_length=100)
    price= models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=300)
    stripe_product_id = models.CharField(max_length=50,default="")
    stripe_product_price = models.CharField(max_length=50,default="")
    time = models.IntegerField()
    class Meta:
        verbose_name = _('package')
        verbose_name_plural = _('packages')
    def __str__(self):
        return self.name

    
class Event(models.Model):
    date = models.DateField()
    start_hour = models.TimeField()
    end_hour = models.TimeField()
    trainer = models.ForeignKey(CustomUser,on_delete=CASCADE)
    client_name = models.CharField(max_length=100,default='')
    client_email = models.EmailField(default='')
    client_phone = PhoneNumberField()
    package = models.ForeignKey(Package,on_delete=CASCADE,null=True,blank=False)
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


class Post(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=CASCADE)
    title = models.CharField(max_length=100)
    image = models.FileField()
    content = tinymce_models.HTMLField()
    date = models.DateTimeField(auto_now_add=True,null=True)
    slug = models.SlugField(null=True,blank=True)
    class Meta:
        ordering = ('-date',)
        verbose_name = _('post')
        verbose_name_plural = _('posts')
    def __str__(self):
        return self.title

class TrainingByDay:
    def __init__(self, email, content, created=None):
        self.email = email
        self.content = content
        self.created = created or datetime.now()



class Plan(models.Model):
    client_name = models.CharField(max_length=100,default='')
    client_email = models.EmailField(default='')
    client_phone = PhoneNumberField()
    trainer = models.ForeignKey(CustomUser,on_delete=CASCADE)
    package = models.ForeignKey('Package',on_delete=models.CASCADE)
    events = models.ManyToManyField('Event')
    completed = models.BooleanField(default=False)
    objects = models.Manager()
    plans = PlanCompletedManager()
    def __str__(self):
        return self.client_name + ' ' + self.client_email + ' plan ' + self.package.name

