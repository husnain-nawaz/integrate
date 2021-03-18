from django.db import models

# Create your models here.

class Blog(models.Model):
    name = models.CharField(max_length=30)
    post_title = models.CharField(max_length=150)
    post_image = models.ImageField(upload_to='images/')
    post_background_image = models.ImageField(upload_to='images/background/')
    post_main = models.TextField()
    post_secondary = models.CharField(max_length=120)
    date = models.DateField()

    def summary(self):
        return self.post_main[:120]

    def __str__(self):
        return self.name




