from django.contrib import admin
from .models import Student,Classes,Classroom
# Register your models here.
admin.site.register(Student) # register use default setting
admin.site.register(Classes)
# admin.site.register(Classroom)

"""customize model panel"""
class ClassroomAdmin(admin.ModelAdmin):
    # fields to show in edit form
    fields = ('room_number', 'room_capacity',)
    # custom actions
    # actions = [upgrade_to_premium,]
    # field to search with default search view
    search_fields = ('room_number',)
    # display columns in list view, show model's __str__ if no setting
    # room_space is a custom field to show capacity in words
    # room_floor shows the floor by room number (the first number)
    list_display = ('room_number','room_space','room_floor')
    # readonly fields in add/edit form
    # readonly_fields = ('room_number',)

    # customize display list columns
    def room_space(self,obj):
        return "Big" if obj.room_capacity > 30 else "Small"
    def room_floor(self,obj):
        return obj.room_number[0]

admin.site.register(Classroom, ClassroomAdmin)