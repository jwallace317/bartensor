from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

class Friend_request(models.Model):
    profile_FK = models.ForeignKey(Profile, on_delete=models.PROTECT, related_name='profilerequest1')
    request_FK = models.ForeignKey(Profile, on_delete=models.PROTECT, related_name='profilerequest2')

    def __str__(self):
        return str(self.profile_FK) + " requested " + str(self.request_FK)

class Friend(models.Model):
    profile_FK = models.ForeignKey(Profile, on_delete=models.PROTECT, related_name='profile1')
    friend_FK = models.ForeignKey(Profile, on_delete=models.PROTECT, related_name='profile2')

    def __str__(self):
        return str(self.profile_FK) + " accepted " + str(self.friend_FK) + "'s request"


class Drinks(models.Model):
    drink_hash = models.CharField(max_length=64, default="emptydrink", unique=True)
    image = models.ImageField(default='default.jpg', upload_to='drink_pics')

    def __str__(self):
        return str(self.id) + ", " + str(self.drink_hash)


class Drink_names(models.Model):
    drink_FK = models.ForeignKey(Drinks, on_delete=models.PROTECT)
    drink_name = models.CharField(max_length=32)

    def __str__(self):
        return str(self.id) + ", " + str(self.drink_FK.drink_hash) + ", " + str(self.drink_name)


class Profile_to_liked_drink(models.Model):
    profile_FK = models.ForeignKey(Profile, on_delete=models.PROTECT)
    drink_FK = models.ForeignKey(Drinks, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.id) + ", " + str(self.profile_FK.user.username) + ", " + str(self.drink_FK.drink_hash)

class Profile_to_disliked_drink(models.Model):
    profile_FK = models.ForeignKey(Profile, on_delete=models.PROTECT)
    drink_FK = models.ForeignKey(Drinks, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.id) + ", " + str(self.profile_FK.user.username) + ", " + str(self.drink_FK.drink_hash)

