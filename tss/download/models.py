from django.db import models

# Create your models here.

# download document category model start
class document_category(models.Model):
    class Meta:
        verbose_name = 'Document Category'
        verbose_name_plural = 'Document Categories'

    name = models.CharField(max_length=100, null=False, blank=False)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
# download document category model end

# download document model start
def doc_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'document_upload/{0}/{1}'.format(instance.category, filename)

class document(models.Model):
    class Meta:
        verbose_name = 'Document'
        verbose_name_plural = 'Documents'
    
    name = models.CharField(max_length=50)
    discription =  models.TextField(max_length=100)
    document_category = models.ForeignKey(
        document_category, on_delete=models.SET_NULL, null=True, blank=True)
    file = models.FileField(upload_to=doc_directory_path,null=False, blank=False)
    public_status = models.BooleanField(default=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.name
# download document model end
class invoice(models.Model):
    class Meta:
        verbose_name = 'Invoive'
        verbose_name_plural = 'Invoices'
    
    name = models.CharField(max_length=50)
    business = models.CharField(max_length=50)
    ntn = models.CharField(max_length=50)
    discription =  models.TextField(max_length=100)
    public_status = models.BooleanField(default=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)