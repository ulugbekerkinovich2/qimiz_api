from django.db import models


# Create your models here.


class DachaKategory(models.Model):
    name_uz = models.CharField(max_length=512, default='kategoriya kitilmagan')
    name_ru = models.CharField(max_length=512, default='kategoriya kitilmagan')
    objects = models.Manager()

    def __str__(self):
        return f'{self.name_uz} - {self.name_ru}'

    class Meta:
        verbose_name_plural = 'Kategorya'


class QimizOlishZonaDachalari(models.Model):
    category = models.ForeignKey(DachaKategory, on_delete=models.CASCADE, related_name='category_uz', null=True)
    title_uz = models.CharField(max_length=128, default='matn kiritilmagan')
    title_ru = models.CharField(max_length=128, default='matn kiritilmagan')
    cost = models.IntegerField(default=1000000)
    text_uz = models.TextField(default='matn kiritilmagan')
    text_ru = models.TextField(default='текст не введен')
    image = models.ImageField(upload_to='images/')
    objects = models.Manager()

    def __str__(self):
        return f'{self.title_uz} - {self.title_ru}'

    class Meta:
        verbose_name_plural = 'Qimiz_Olish_Dacha_Zonalari'


class DachaVideo(models.Model):
    video = models.FileField(upload_to='videos/')
    objects = models.Manager()

    def __str__(self):
        return self.video.name

    class Meta:
        verbose_name_plural = 'Dacha_Video'


class MijozlarFikrlariAudio(models.Model):
    audio_file = models.FileField(upload_to='audio_files/')
    objects = models.Manager()

    def __str__(self):
        return self.audio_file.name

    class Meta:
        verbose_name_plural = 'Mijozlar_Fikri_Audio'


class MijozlarFikrlariImage(models.Model):
    image_file = models.ImageField(upload_to='screenshots/')
    objects = models.Manager()

    def __str__(self):
        return self.image_file.name

    class Meta:
        verbose_name_plural = 'Mijozlar_Fikrlari_ScreenShot'


class Comments(models.Model):
    title_uz = models.CharField(max_length=128, default='matn kiritilmagan')
    title_ru = models.CharField(max_length=128, default='matn kiritilmagan')
    text_uz = models.TextField(default='matn kiritilmagan')
    text_ru = models.TextField(default='matn kiritilmagan')
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    objects = models.Manager()

    def __str__(self):
        return f'{self.title_uz} - {self.title_ru}'

    class Meta:
        verbose_name_plural = 'Comments'


class Form(models.Model):
    name = models.CharField(max_length=128, default='matn kiritilmagan')
    phone = models.CharField(max_length=128, default='matn kiritilmagan')
    objects = models.Manager()

    def __str__(self):
        return f'{self.name} - {self.phone}'

    class Meta:
        verbose_name_plural = 'Form'


class About(models.Model):
    title_uz = models.CharField(max_length=512, default='matn kiritilmagan')
    title_ru = models.CharField(max_length=512, default='matn kiritilmagan')
    text_uz = models.TextField(default='matn kiritilmagan')
    text_ru = models.TextField(default='matn kiritilmagan')
    objects = models.Manager()

    def __str__(self):
        return self.title
