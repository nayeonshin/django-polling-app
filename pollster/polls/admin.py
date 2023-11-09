from django.contrib import admin

from .models import Choice, Question

admin.site.site_header = "Pollster Admin"
admin.site.site_title = "Pollster Admin Area"
admin.site.index_title = "Welcome to the Pollster Admin Area"


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        (
            "Date Information", {
                "fields": ["publication_date"],
                "classes": ["collapse"]
            }
        ),
    ]
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)
