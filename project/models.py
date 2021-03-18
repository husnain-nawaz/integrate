from django.db import models

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=30)
    post_title = models.CharField(max_length=150)
    post_image = models.ImageField(upload_to='images/project/products/')
    post_catagory_image1 = models.ImageField(upload_to='images/project/catagory/')
    post_catagory_image2 = models.ImageField(upload_to='images/project/catagory/')
    post_catagory_image3 = models.ImageField(upload_to='images/project/catagory/')
    post_background_image1 = models.ImageField(upload_to='images/project/background/')
    post_background_image2 = models.ImageField(upload_to='images/project/background/')
    post_background_image3 = models.ImageField(upload_to='images/project/background/')
    post_background_image4 = models.ImageField(upload_to='images/project/background/')
    post_background_image5 = models.ImageField(upload_to='images/project/background/')
    post_main = models.TextField()
    post_secondary = models.CharField(max_length=120)
    date = models.DateField()


    def summary(self):
        return self.post_main[:120]

    def __str__(self):
        return self.name


class project_formal(models.Model):
    name = models.CharField(max_length=30)
    post_title = models.CharField(max_length=150)
    post_image = models.ImageField(upload_to='images/project/products/formal/')
    post_main = models.TextField()
    date = models.DateField()


    def summary(self):
        return self.post_main[:120]

    def __str__(self):
        return self.post_title


class project_casual(models.Model):
    name = models.CharField(max_length=30)
    post_title = models.CharField(max_length=150)
    post_image = models.ImageField(upload_to='images/project/products/casual/')
    post_main = models.TextField()
    date = models.DateField()

    def summary(self):
        return self.post_main[:120]

    def __str__(self):
        return self.post_title


class project_reviews(models.Model):
    name = models.CharField(max_length=30)
    title = models.CharField(max_length=120)
    profile_image = models.ImageField(upload_to='images/project/reviews/')
    comment = models.TextField(max_length=270)
    date = models.DateField()

    def __str__(self):
        return self.name


# base.html footer class
# can remove
class footer(models.Model):
    brand_name = models.CharField(max_length=50)
    text = models.TextField(max_length=270)
    facebook_link = models.CharField(max_length=80)
    instagram_link = models.CharField(max_length=80)
    email = models.CharField(max_length=80)
    phone = models.CharField(max_length=20)
    complain_phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    brand_name_full = models.CharField(max_length=50)

    def __str__(self):
        return self.brand_name




