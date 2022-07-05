from django.db import models
from PIL import Image
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from contact.models import office
# Create your models here.

# employee model start
class employee(models.Model):
    class Meta:
        verbose_name = 'employee'
        verbose_name_plural = 'employees'

    class desig(models.TextChoices):
        EMPTY = '', _('----------')
        DIRECTOR = 'DIR', _('Director')
        SECRETARY = 'SEC', _('Secretary')
        CHIEF_EXECUTIVE_OFFICER = 'CEO', _('Chief Executive Officer')
        CHIEF_OPERATING_OFFICER = 'COO', _('Chief Operating Officer')
        CHIEF_SECURITY_OFFICER = 'CSO', _('Chief Security Officer')
        CHIEF_MARKETING_OFFICER = 'CMO', _('Chief Marketing Officer')
        SECURITY_OFFICER = 'SO', _('Security Officer')
        SECURITY_SUPERVISOR = 'SS', _('Security Supervisor')

    office = models.ForeignKey(office,
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=50,  null=False, blank=False)
    designation =  models.CharField(max_length=3, choices=desig.choices, null=True, default=desig.EMPTY)
    cnic = models.PositiveBigIntegerField(help_text='CNIC Number', null=False, blank=False)
    date_added = models.DateTimeField(auto_now_add=True)
    emp_status =  models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def is_upperclass(self):
        return self.designation
# employee model end

# employee profile model start
def upload_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'team_upload/{0}/{1}'.format(instance.cnic.name, filename)

class employee_profile(models.Model):
    class Meta:

        verbose_name = 'profile'
        verbose_name_plural = 'profiles'

    cnic = models.OneToOneField(employee,
        on_delete=models.CASCADE,
        verbose_name='Employee Name',
    )
    address =models.TextField(max_length=150, verbose_name='Address')
    img = models.ImageField(upload_to=upload_directory_path, height_field=None, width_field=None, max_length=100,null=False, blank=False, verbose_name='Profile Pic')
    cell_number = PhoneNumberField(unique=True, null=False, verbose_name='Cell Number')
    fb= models.URLField(null=True, blank=True, verbose_name='Facebook Profile Link')
    twitt= models.URLField(null=True, blank=True, verbose_name='Twitter Profile Link')
    linkedin= models.URLField(null=True, blank=True, verbose_name='Linkedin Profile Link')
    insta= models.URLField(null=True, blank=True, verbose_name='Instagram Profile Link')
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cnic.name


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img= Image.open(self.img.path)
        new_image = img.resize((210, 250))
        new_image.save(self.img.path)
# employee profile model end