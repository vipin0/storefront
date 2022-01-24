from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
# Create your models here.
User = get_user_model()

class LikedItem(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    # for generic relation
    content_type = models.ForeignKey(ContentType,on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    conent_object = GenericForeignKey()