from django.db import models
from country_info_tree.models import province, division, district, tehsil, phn_code
# Create your models here.



# office model start
class office(models.Model):
    class Meta:
        verbose_name = 'office'
        verbose_name_plural = 'offices'


    office_code = models.SlugField(max_length=30,unique=True, blank=False, null= False, verbose_name='Office Type')
    province=models.ForeignKey(province, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Province')
    division=models.ForeignKey(division, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Division')
    district=models.ForeignKey(district, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='District')
    tehsil=models.ForeignKey(tehsil, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='City')
    post_code = models.IntegerField(unique=True, verbose_name='Postal Code')
    address = models.CharField(max_length=100, blank=False, null=False, verbose_name='Complex Address')
    phone_area_code = models.ForeignKey(phn_code, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Dialing Code')
    phone_num= models.CharField(max_length=8, verbose_name='Landline')
    opening_time = models.TimeField(auto_now=False, auto_now_add=False, default='', blank=True, null=True, verbose_name='Opening Time')
    closing_time = models.TimeField(auto_now=False, auto_now_add=False, default='', blank=True, null=True, verbose_name='Closing Time')
    week_start_day = models.CharField(max_length=50, default='Monday', verbose_name='Week Start Day')
    week_end_day = models.CharField(max_length=50, default='Saturday', verbose_name='Week End Day')
    break_day = models.CharField(max_length=50, default='Friday', verbose_name='Break Day')
    friday_break_start = models.TimeField(auto_now=False, auto_now_add=False, null=True, verbose_name='Break Start')
    friday_break_end = models.TimeField(auto_now=False, auto_now_add=False, null=True, verbose_name='Break End')
    email = models.EmailField(max_length=50, blank=False, null=False, verbose_name='Email')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    office_status = models.BooleanField(default=True, verbose_name='Status')

    def __str__(self):
        return self.office_code
# office model end

# query/complaint model start
class query(models.Model):
    class Meta:
        verbose_name = 'query'
        verbose_name_plural = 'queries'


    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=30)
    phone = models.SlugField(max_length=12)
    subject = models.CharField(max_length=50)
    message = models.TextField(max_length=300)
    query_resolve_status = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_marked_resolve = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject
# query/complaint model end

# subscribe news letter model start
class subscriber(models.Model):
    class Meta:
        verbose_name = 'subscriber'
        verbose_name_plural = 'subscribers'

    email = models.EmailField(max_length=50, blank=False, null=False, verbose_name='Email')
    is_verified =  models.BooleanField(default=False)
    sub_status =  models.BooleanField(default=False)
    sub_date = models.DateTimeField(auto_now_add=True)
    sub_change_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email
# subscribe news letter model end