from django.db.models.signals import pre_save, pre_delete
from django.dispatch import receiver
from .models import document


@receiver(pre_delete, sender=document)
def pre_del_file(sender, instance, *args, **kwargs):
    """ Clean Old Image file """
    try:
        instance.file.delete(save=False)
    except:
        pass




@receiver(pre_save, sender=document)
def delete_file_on_update(sender, instance, *args, **kwargs):
    """ instance old image file will delete from os """

    if instance.id is None:
        pass
    else:
        current_file = instance.file.path
        if current_file is None:
            pass
        else:
            old_file = doc.objects.get(id=instance.id).file.path
            if old_file is None:
                pass
            else:
                import os
                if os.path.exists(old_file):
                    os.remove(old_file)
