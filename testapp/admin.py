from django.contrib import admin
from testapp.models import hydjobs, babglorejobs, chennaijobs, punejobs, noidajobs

# Register your models here.


class hydjobsAdmin(admin.ModelAdmin):
    list_display = ['date', 'company', 'title',
                    'eligibility', 'address', 'email', 'phonenumber']


class babglorejobsAdmin(admin.ModelAdmin):
    list_display = ['date', 'company', 'title',
                    'eligibility', 'address', 'email', 'phonenumber']


class chennaijobsAdmin(admin.ModelAdmin):
    list_display = ['date', 'company', 'title',
                    'eligibility', 'address', 'email', 'phonenumber']


class punejobsAdmin(admin.ModelAdmin):
    list_display = ['date', 'company', 'title',
                    'eligibility', 'address', 'email', 'phonenumber']


class noidajobsAdmin(admin.ModelAdmin):
    list_display = ['date', 'company', 'title',
                    'eligibility', 'address', 'email', 'phonenumber']


admin.site.register(hydjobs, hydjobsAdmin)
admin.site.register(chennaijobs, chennaijobsAdmin)
admin.site.register(babglorejobs, babglorejobsAdmin)
admin.site.register(punejobs, punejobsAdmin)
admin.site.register(noidajobs, noidajobsAdmin)
