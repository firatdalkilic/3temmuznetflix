from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profiles(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    isim = models.CharField(max_length=100, verbose_name='İsim')
    resim = models.FileField(upload_to='profiles/', verbose_name='Profil Resmi')

    def __str__(self):
        return self.isim
    
class Kullanici(models.Model):
    isim = models.CharField(max_length=100)
    soyisim = models.CharField(max_length=100)
    email = models.CharField(max_length=200, null=True)
    resim = models.FileField(upload_to='kullanicilar/', verbose_name='Profil Resmi')
    tel = models.CharField(max_length=200,default=0)
    dogum = models.DateField()
    olusturulma_tarih = models.DateField(editable=False, auto_now_add= True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.isim