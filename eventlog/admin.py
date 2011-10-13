from django.contrib import admin

from eventlog.models import Log


class LogAdmin(admin.ModelAdmin):
    list_filter = ["action"]
    list_display = ["timestamp", "user", "action", "extra"]
    search_fields = ["user__username"]


admin.site.register(Log, LogAdmin)
