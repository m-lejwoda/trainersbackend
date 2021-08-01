from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Post
from django.utils.text import slugify

@receiver(pre_save,sender=Post)
def add_slug(instance,new_slug=None,**kwargs):
    print(instance)
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs=Post.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug= "%s-%s" %(slug, qs.first().id)
        return add_slug(instance,new_slug=new_slug)
    instance.slug = slug
    return slug

