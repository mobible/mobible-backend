from django.contrib import admin
from dbs.models import Journey, Verse


class VerseInline(admin.StackedInline):
    model = Verse
    extra = 1


class JourneyAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    list_filter = ('created_at', 'updated_at')
    read_only_fields = ('created_at', 'updated_at')

    inlines = [
        VerseInline,
    ]

admin.site.register(Journey, JourneyAdmin)
# admin.site.register(Verse)
