from django.db import models
# my first model
# Create your models here.
class KirrURL(models.Model):
    url=models.CharField(max_length=220,)
    shortcode=models.CharField(max_length=20,unique=True)
    def __str__(self):
        return str(self.url)

    def __unicode__(self):
        return str(self.url)


'''
Always run these commands after making any change in the code
python manage.py makemigration
python manage.py migrate
'''
