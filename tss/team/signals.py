from django.db.models.signals import pre_save, pre_delete
from django.dispatch import receiver
from .models import employee_profile
 
 
@receiver(pre_delete, sender=employee_profile)
def pre_del_image(sender, instance, *args, **kwargs):
    """ Clean Old Image file """
    try:
        instance.img.delete(save=False)
    except:
        pass



@receiver(pre_save, sender=employee_profile)
def delete_image_on_update(sender, instance, *args, **kwargs):
    """ instance old image file will delete from os """

    if instance.id is None:
        pass
    else:
        current_image = instance.img.path
        if current_image is None:
            pass
        else:
            old_img = employee_profile.objects.get(id=instance.id).img.path
            if old_img is None:
                pass
            else:
                import os
                if os.path.exists(old_img):
                    os.remove(old_img)