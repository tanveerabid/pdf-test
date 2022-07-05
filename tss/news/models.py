from django.db import models

# Create your models here.


def upload_news_category_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'news_upload/category/{0}/{1}'.format(instance.cnic.name, filename)

class News_Category(models.Model):
	class Meta:
		verbose_name = 'News Category'
		verbose_name_plural = 'News Categories'

	name = models.CharField(max_length=100)
	description = models.CharField(blank=True, max_length=255)
	image = models.ImageField(upload_to=upload_news_category_path, height_field=None, width_field=None, max_length=100,null=True, blank=True, verbose_name='Category Image')
	category_status = models.BooleanField(default=True)
	create_at = models.DateTimeField(auto_now_add=True)
	update_at = models.DateTimeField(auto_now=True)


	def __str__(self):
		return self.name



class News(models.Model):
	class Meta:
		verbose_name='News'
		verbose_name_plural='News'

	news_category = models.ForeignKey(News_Category, on_delete=models.CASCADE)
	title = models.CharField(max_length=150)
	keywords = models.CharField(blank=True, max_length=255)
	description = models.CharField(blank=True, max_length=255)
	slug = models.SlugField(null=False, unique=True)
	content = models.TextField(max_length=1000)
	pub_status = models.BooleanField(default=True, verbose_name='Publishing Status')
	create_at = models.DateTimeField(auto_now_add=True)
	update_at = models.DateTimeField(auto_now=True)

	def _str_(self):
		return self.title


def upload_news_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'news_upload/news/{0}/{1}'.format(instance.cnic.name, filename)


class News_Image(models.Model):
    class Meta:

        verbose_name = 'News Image'
        verbose_name_plural = 'News Images'

    news = models.ForeignKey(News, on_delete=models.CASCADE)
    image_title = models.CharField(max_length=150, blank=True)
    image =  image = models.ImageField(upload_to=upload_news_path, height_field=None, width_field=None, max_length=100,null=False, blank=False, verbose_name='News Image')

    def _str_(self):
        return self.image_title







