from django.db import models
from DjangoUeditor.models import UEditorField

# Create your models here.
class Article(models.Model):
    title = models.CharField(u'标题',max_length=30)
    context = UEditorField(u'内容', height=300, width=1000,
                           default=u'', blank=True, imagePath='upload/images/', toolbars='besttome')
    def __str__(self):
        return self.title