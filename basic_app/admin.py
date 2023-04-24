from django.contrib import admin

from basic_app import models

# Register your models here.
admin.site.register(models.DachaKategory)
admin.site.register(models.QimizOlishZonaDachalari)
admin.site.register(models.DachaVideo)
admin.site.register(models.MijozlarFikrlariAudio)
admin.site.register(models.MijozlarFikrlariImage)
admin.site.register(models.Comments)
admin.site.register(models.About)
admin.site.register(models.Form)


# class AdminSite(admin.AdminSite):
admin.site.site_header = 'Qimiz'
admin.site.site_title = 'Qimiz olish Dachalari'
admin.site.index_title = 'Dacha'


# my_admin_site = AdminSite(name='myadmin')
