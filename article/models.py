# -*- coding: utf-8 -*-				#для русского языка
from django.db import models
import datetime
# Create your models here.
class Article(models.Model):
	class Meta():
		db_table = "article"

	article_title = models.CharField(max_length = 200)
	article_text = models.TextField()
	article_date = models.DateTimeField()
	article_likes = models.IntegerField(default=0)#blank=True null=true
	def __str__(self):
		return self.article_title
	

	
class Comments(models.Model):
	class Meta():
		db_table = "comments"
	"""def __init__(self, arg):
		super(Comments, self).__init__()
		self.arg = arg
	"""
	"""def __unicode__(self):
		return self.comments_text"""
	comments_text = models.TextField(verbose_name="Текст коммента")
	comments_article = models.ForeignKey(Article)