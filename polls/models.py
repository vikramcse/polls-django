from django.db import models
from django.utils import timezone
import datetime

# Each field is represented by an instance of a Field class eg CharField, DateTimeField ...
class Question(models.Model):
	# database will use question_text, pub_date as the column name
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):			# __unicode__ on Python 2
    	return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __unicode__(self):              # __unicode__ on Python 2
        return self.choice_text