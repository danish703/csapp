from django.contrib import admin
from .models import Course,Subject,Notes,LabManual,OldQuestion,PractiseQuestion,Book
# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    list_display = ['id','course_name']
    search_fields = ['course_name']
admin.site.register(Course,CourseAdmin)

class SubjectAdmin(admin.ModelAdmin):
    list_display = ['subject_name','subject_number','credit_hours','nature','course','semester']
    search_fields = ['subject_name','subject_number',]
    list_filter = ['course','semester']
admin.site.register(Subject,SubjectAdmin)

class OldQuestionAdmin(admin.ModelAdmin):
    list_display = ['title','year','subject']
    search_fields = ['title','year']
    list_filter = ['year','subject']

admin.site.register(OldQuestion,OldQuestionAdmin)

class NotesAdmin(admin.ModelAdmin):
    list_display = ['title','link','subject']
    search_fields = ['title',]
    list_filter = ['subject']
admin.site.register(Notes,NotesAdmin)

class LabManualAdmin(admin.ModelAdmin):
    list_display = ['title','link','subject']
    search_fields = ['title',]
    list_filter = ['subject']
admin.site.register(LabManual,LabManualAdmin)

class PractiseQuestionAdmin(admin.ModelAdmin):
    list_display = ['title','link','subject']
    search_fields = ['title',]
    list_filter = ['subject']
admin.site.register(PractiseQuestion,PractiseQuestionAdmin)

class BookAdmin(admin.ModelAdmin):
    list_display = ['title','link','subject']
    search_fields = ['title',]
    list_filter = ['subject']
admin.site.register(Book,BookAdmin)
