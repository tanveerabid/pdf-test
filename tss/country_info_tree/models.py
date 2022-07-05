from django.db import models

# Create your models here.


class province(models.Model):
    p_code=models.CharField(max_length=5, unique=True)
    name=models.CharField(max_length=50, unique=True)
    category=models.CharField(max_length=50, default='Province')
    p_date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class division(models.Model):
    province=models.ForeignKey(province,on_delete=models.CASCADE)
    name=models.CharField(max_length=50, unique=True)
    div_date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class district(models.Model):
    division=models.ForeignKey(division,on_delete=models.CASCADE)
    name=models.CharField(max_length=50, unique=True)
    dis_date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class tehsil(models.Model):
    district=models.ForeignKey(district,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    tehsil_date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class phn_code(models.Model):
    district=models.ForeignKey(district,on_delete=models.CASCADE)
    code=models.CharField(max_length=6)
    code_date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.code




