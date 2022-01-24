from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from ..models import Customer

User = get_user_model()
@receiver(post_save,sender=User)
def create_customer_for_new_user(sender,**kwargs):
    if kwargs['created']:
        user = kwargs['instance']
        # print(user.first_name)
        # print(user.last_name)
        Customer.objects.create(first_name=user.first_name,last_name=user.last_name,user=user)