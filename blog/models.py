from django.conf import settings
from django.db import models
from django.utils import timezone
#The above are lines that add some bits from other files.
#So instead of copying and pasting the same things in every file,we can include some parts with from ... import ... .

class Post(models.Model):  # this line defines the model (it is an object )
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) #this is a link to another model.
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
