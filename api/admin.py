from django.contrib import admin
from .models import Doctor, Direction




class DoctorAdmin (admin.ModelAdmin):
    list_display = ["name", "slag","description" ,"date" ,"years_of_experience" ,"number_sort"]
    filter_horizontal = ['directions']

    class Meta:
        model = Doctor


admin.site.register(Doctor, DoctorAdmin)

class DirectionAdmin (admin.ModelAdmin):
    list_display = ["name", "slag", "number_sort"]

    class Meta:
        model = Direction


admin.site.register(Direction, DirectionAdmin)



