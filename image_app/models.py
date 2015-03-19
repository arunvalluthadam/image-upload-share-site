from django.db import models
from sorl.thumbnail import ImageField
from django.contrib.auth.models import User

# Create your models here.
class Item(models.Model):
	image = ImageField(upload_to="images", null=True, blank=True)
	user = models.ForeignKey(User, null=True, blank=True)

	# def __unicode__(self):
	# 	return user #.username


class Comments(models.Model):
	item = models.ForeignKey(Item, null=True, blank=True)
	name = models.CharField(verbose_name=u'Name', max_length=200)
	email = models.EmailField(verbose_name=u'Email', null=True, blank=True)
	content = models.TextField(verbose_name=u'Designation', null=True, blank=True)

	def __unicode__(self):
		return self.name
