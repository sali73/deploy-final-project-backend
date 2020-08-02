from django.contrib import admin
from .models import Students ,Offering , Course , Instructor
# Register your models here.
admin.site.register(Students)
admin.site.register(Offering)
admin.site.register(Course)
admin.site.register(Instructor)