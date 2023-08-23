from django.contrib import admin
from .models import Question


# Register your models here.

# @admin.site.register(Question)

#       or

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id','question_text','publication_date']